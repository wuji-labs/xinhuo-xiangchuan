#!/usr/bin/env python3
"""
薪火相传 (xinhuo-xiangchuan) Benchmark Analyzer.

Computes statistics ONLY from real, human/judge-scored results. It never
fabricates numbers: if the result files contain no scores (the subjective
fields are still null, as written by run_benchmark.py), it exits with a clear
message rather than inventing data.

Scoring workflow (see README_BENCHMARK.md):
    1. run_benchmark.py collects raw responses (subjective fields = null).
    2. A human or blinded independent judge fills the score fields per record:
         - expected_hits      : int  (# of expected_actions satisfied)
         - expected_total     : int  (total expected_actions for that scenario)
         - dim_scores         : {dimension: 0..3}
         - fabricated_citation: bool
    3. analyze_results.py aggregates and runs significance tests.

Dependencies:
    pip install numpy scipy

Usage:
    python analyze_results.py --input-dir results/
    python analyze_results.py --input-dir results/ --compare skill baseline
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

SCORE_FIELDS = ("expected_hits", "expected_total", "dim_scores")


def load_records(input_dir: Path) -> list[dict]:
    """Load all *.json result files in the directory."""
    files = sorted(input_dir.glob("*.json"))
    if not files:
        sys.exit(f"No result JSON files in {input_dir}. Run run_benchmark.py first.")
    records: list[dict] = []
    for f in files:
        records.extend(json.loads(f.read_text(encoding="utf-8")))
    return records


def is_scored(rec: dict) -> bool:
    """A record is scored only if a judge filled the score fields."""
    return all(rec.get(field) is not None for field in SCORE_FIELDS)


def require_scores(records: list[dict]) -> list[dict]:
    """Filter to scored records; abort honestly if none were judged yet."""
    scored = [r for r in records if is_scored(r)]
    if not scored:
        sys.exit(
            "No scored records found. run_benchmark.py only COLLECTS responses; "
            "subjective fields are null until a judge scores them. "
            "Score the records (see README_BENCHMARK.md), then re-run. "
            "This tool will not invent numbers."
        )
    return scored


def hit_rate(rec: dict) -> float:
    total = rec["expected_total"]
    return rec["expected_hits"] / total if total else 0.0


def summarize(records: list[dict]) -> None:
    """Print per-condition aggregate stats over scored records only."""
    import numpy as np

    by_cond: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_cond[r["condition"]].append(r)

    print("\n=== Aggregate (scored records only) ===")
    for cond, recs in sorted(by_cond.items()):
        hits = np.array([hit_rate(r) for r in recs])
        fabr = np.array([1.0 if r.get("fabricated_citation") else 0.0 for r in recs])
        dims = defaultdict(list)
        for r in recs:
            for d, v in (r.get("dim_scores") or {}).items():
                dims[d].append(v)
        print(f"\n[{cond}]  n={len(recs)}")
        print(f"  expected_actions hit-rate: mean={hits.mean():.3f} sd={hits.std(ddof=1) if len(hits) > 1 else 0:.3f}")
        print(f"  fabrication rate:          {fabr.mean():.3f}")
        for d, vals in sorted(dims.items()):
            arr = np.array(vals)
            print(f"  dim {d:<16} mean={arr.mean():.2f}/3")


def compare(records: list[dict], cond_a: str, cond_b: str) -> None:
    """Mann-Whitney U + Cohen's d on hit-rate between two conditions."""
    import numpy as np
    from scipy import stats

    a = np.array([hit_rate(r) for r in records if r["condition"] == cond_a])
    b = np.array([hit_rate(r) for r in records if r["condition"] == cond_b])
    if len(a) == 0 or len(b) == 0:
        print(f"\nCannot compare {cond_a} vs {cond_b}: missing scored data for one side.")
        return

    u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    # Cohen's d (pooled sd)
    na, nb = len(a), len(b)
    pooled_sd = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)) if na + nb > 2 else 0.0
    d = (a.mean() - b.mean()) / pooled_sd if pooled_sd else float("nan")
    stars = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "n.s."

    print(f"\n=== {cond_a} vs {cond_b} (expected_actions hit-rate) ===")
    print(f"  {cond_a}: mean={a.mean():.3f} (n={na})")
    print(f"  {cond_b}: mean={b.mean():.3f} (n={nb})")
    print(f"  Mann-Whitney U={u:.1f}  p={p:.4g} {stars}")
    print(f"  Cohen's d={d:.3f}")


def parse_args():
    p = argparse.ArgumentParser(description="xinhuo-xiangchuan benchmark analyzer (real scores only)")
    p.add_argument("--input-dir", required=True)
    p.add_argument("--compare", nargs=2, action="append", metavar=("C1", "C2"),
                   help="condition pair to compare (repeatable)")
    return p.parse_args()


def main():
    args = parse_args()
    records = require_scores(load_records(Path(args.input_dir)))
    summarize(records)
    for c1, c2 in (args.compare or []):
        compare(records, c1, c2)


if __name__ == "__main__":
    main()
