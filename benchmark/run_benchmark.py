#!/usr/bin/env python3
"""
薪火相传 (xinhuo-xiangchuan) Benchmark Runner.

Collects raw AI responses for each teaching scenario under two conditions
(baseline vs skill), across one or more models. It does NOT score responses
and NEVER fabricates any metric — scoring is done offline by a human or an
independent blinded judge (see README_BENCHMARK.md). Subjective fields are
written as null for later judging.

Dependencies (install only what you test):
    pip install anthropic openai google-generativeai

Usage:
    python run_benchmark.py --model claude-sonnet-4 --condition both --runs 5
    python run_benchmark.py --model gpt-4o --scenario 6 --condition skill --runs 3
    python run_benchmark.py --model claude-sonnet-4 --condition both --dry-run
"""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

HERE = Path(__file__).resolve().parent
SKILL_PATH = HERE.parent / "SKILL.md"
REFERENCE_PATH = HERE.parent / "reference" / "lunyu-daxue.md"
SCENARIOS_PATH = HERE / "scenarios.json"

DEFAULT_RUNS = 5
DEFAULT_OUTPUT_DIR = HERE / "results"
DEFAULT_CODEBASE_PATH = HERE / "test-project"

# Pinned model ids for reproducibility. Update deliberately and record in report.
MODELS = {
    "claude-sonnet-4": {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gemini-2.5-pro": {"provider": "google", "model_id": "gemini-2.5-pro"},
}

CONDITIONS = ["baseline", "skill", "dump"]

BASELINE_SYSTEM = (
    "You are a helpful teaching assistant. A learner has come to you. "
    "Teach them what they asked. Respond in the learner's language."
)

DUMP_SYSTEM = (
    "You are a helpful expert. Give the most complete, correct, and detailed "
    "answer possible to the learner's request. Be thorough and authoritative."
)

# Max tokens for the agent's teaching response.
MAX_OUTPUT_TOKENS = 2000


@dataclass
class ResultRecord:
    scenario_id: int
    scenario_name: str
    condition: str
    model: str
    model_id: str
    run_number: int
    timestamp: str
    response_text: str
    # Subjective fields left null for the blinded judge to fill — never auto-scored.
    anchored_on_prior_knowledge: Optional[bool] = None
    gave_one_corner_left_three: Optional[bool] = None
    ended_with_self_check: Optional[bool] = None
    fabricated_citation: Optional[bool] = None
    duration_seconds: float = 0.0
    error: str = ""


# --------------------------------------------------------------------------
# Prompt assembly
# --------------------------------------------------------------------------

def load_text(path: Path) -> str:
    """Read a UTF-8 text file, raising a clear error if missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return path.read_text(encoding="utf-8")


def build_system_prompt(condition: str) -> str:
    """Compose the system prompt for a given condition."""
    if condition == "baseline":
        return BASELINE_SYSTEM
    if condition == "dump":
        return DUMP_SYSTEM
    if condition == "skill":
        skill_text = load_text(SKILL_PATH)
        # reference is attached so the agent can ground citations honestly.
        try:
            reference_text = load_text(REFERENCE_PATH)
        except FileNotFoundError:
            reference_text = ""
        parts = [BASELINE_SYSTEM, "", "--- SKILL: xinhuo-xiangchuan ---", skill_text]
        if reference_text:
            parts += ["", "--- REFERENCE: lunyu-daxue ---", reference_text]
        return "\n".join(parts)
    raise ValueError(f"Unknown condition: {condition}")


def build_user_prompt(scenario: dict, codebase_path: Path) -> str:
    """Compose the user prompt: the task plus the real learner sample."""
    learner_rel = scenario.get("learner_file", "")
    learner_text = ""
    if learner_rel:
        # learner_file is stored relative to the benchmark dir.
        learner_path = (HERE / learner_rel)
        if not learner_path.exists():
            # fall back to codebase_path override
            learner_path = codebase_path / Path(learner_rel).name
        if learner_path.exists():
            learner_text = load_text(learner_path)
        else:
            raise FileNotFoundError(
                f"Learner sample not found for scenario {scenario['id']}: {learner_rel}"
            )
    return f"{scenario['task']}\n\n--- LEARNER SAMPLE ---\n{learner_text}"


# --------------------------------------------------------------------------
# Provider calls
# --------------------------------------------------------------------------

def call_anthropic(model_id: str, system: str, user: str) -> str:
    import anthropic  # imported lazily so other providers don't require it
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model=model_id,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def call_openai(model_id: str, system: str, user: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    resp = client.chat.completions.create(
        model=model_id,
        max_tokens=MAX_OUTPUT_TOKENS,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content or ""


def call_google(model_id: str, system: str, user: str) -> str:
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(model_id, system_instruction=system)
    resp = model.generate_content(user)
    return resp.text or ""


PROVIDER_DISPATCH = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "google": call_google,
}


def call_model(provider: str, model_id: str, system: str, user: str) -> str:
    """Dispatch to the right provider. Errors propagate to the caller."""
    fn = PROVIDER_DISPATCH.get(provider)
    if fn is None:
        raise ValueError(f"Unsupported provider: {provider}")
    return fn(model_id, system, user)


# --------------------------------------------------------------------------
# Main loop
# --------------------------------------------------------------------------

def run(args) -> None:
    scenarios = json.loads(load_text(SCENARIOS_PATH))
    if args.scenario is not None:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            sys.exit(f"No scenario with id {args.scenario}")

    if args.condition == "both":
        conditions = ["baseline", "skill"]
    else:
        conditions = [args.condition]

    model_cfg = MODELS.get(args.model)
    if model_cfg is None:
        sys.exit(f"Unknown model {args.model}. Choices: {', '.join(MODELS)}")

    codebase_path = Path(args.codebase_path)
    output_dir = Path(args.output_dir)

    plan = [
        (s, c, r)
        for c in conditions
        for s in scenarios
        for r in range(1, args.runs + 1)
    ]

    print(f"Model: {args.model} ({model_cfg['model_id']})")
    print(f"Conditions: {conditions} | Scenarios: {[s['id'] for s in scenarios]} | Runs: {args.runs}")
    print(f"Total calls: {len(plan)}")

    if args.dry_run:
        for s, c, r in plan:
            print(f"  [DRY] scenario={s['id']} condition={c} run={r}")
        print("Dry run only — no API calls made, no files written.")
        return

    # Validate prompts can be built BEFORE spending any API budget.
    system_cache = {c: build_system_prompt(c) for c in conditions}
    for s in scenarios:
        build_user_prompt(s, codebase_path)  # raises early if a sample is missing

    output_dir.mkdir(parents=True, exist_ok=True)
    records_by_condition: dict[str, list[dict]] = {c: [] for c in conditions}

    for s, c, r in plan:
        system = system_cache[c]
        user = build_user_prompt(s, codebase_path)
        started = time.time()
        text, err = "", ""
        try:
            text = call_model(model_cfg["provider"], model_cfg["model_id"], system, user)
        except KeyError as e:
            sys.exit(f"Missing API key environment variable: {e}")
        except Exception as e:  # provider/network errors recorded, run continues
            err = f"{type(e).__name__}: {e}"
            print(f"  ! scenario={s['id']} condition={c} run={r} ERROR {err}")
        rec = ResultRecord(
            scenario_id=s["id"],
            scenario_name=s["name"],
            condition=c,
            model=args.model,
            model_id=model_cfg["model_id"],
            run_number=r,
            timestamp=datetime.now(timezone.utc).isoformat(),
            response_text=text,
            duration_seconds=round(time.time() - started, 2),
            error=err,
        )
        records_by_condition[c].append(asdict(rec))
        print(f"  ok scenario={s['id']} condition={c} run={r} ({rec.duration_seconds}s)")

    for c, records in records_by_condition.items():
        out = output_dir / f"{args.model}_{c}.json"
        out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {len(records)} records -> {out}")

    print(
        "\nDone. Responses collected WITHOUT scores. "
        "Score offline with a blinded judge per README_BENCHMARK.md, "
        "then run analyze_results.py."
    )


def parse_args():
    p = argparse.ArgumentParser(description="xinhuo-xiangchuan benchmark runner (collect only)")
    p.add_argument("--model", required=True, choices=list(MODELS))
    p.add_argument("--condition", default="both", choices=CONDITIONS + ["both"])
    p.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    p.add_argument("--scenario", type=int, default=None, help="single scenario id (1-7)")
    p.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    p.add_argument("--codebase-path", default=str(DEFAULT_CODEBASE_PATH))
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


if __name__ == "__main__":
    run(parse_args())
