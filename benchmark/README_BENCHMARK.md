# 薪火相传 Benchmark — 评测设计

> ⚠️ **结果待真实运行。本文件是评测设计与复现手册，本仓未跑出任何数字。**
> 仓库内**不含**任何 before/after 得分、p 值、效应量或胜率。任何此类数字必须由你按下方流程真实运行后产生，并附模型版本与日期。编造数字违反 research-integrity 铁律 —— 本评测专设场景 6 检验「不造引用」，自身更不可造数。

本套件评测一个问题：**加载 `xinhuo-xiangchuan`（薪火相传）skill，是否让 AI 从「答对」转向「教会」?**

---

## 一、对照设计（两条件）

每个场景在**完全相同**的学习者样本（`test-project/learner-NN.md`）上跑两条件，唯一差别是是否加载 `SKILL.md`：

| 条件 | 系统提示 | 含义 |
|------|---------|------|
| **baseline** | 通用「你是一个乐于助人的助教，请教这位学习者」 | 不加载 skill 的原始 agent |
| **skill** | baseline + 完整 `xinhuo-xiangchuan/SKILL.md`（按需可附 `reference/lunyu-daxue.md`） | 加载薪火相传 |

可选第三条件（加分，非必需）：**dump** —「直接给出完整、正确、详尽的答案」，模拟「答对即可」反模式，用于反向对照「教会 ≠ 倒答案」。

> 评测的是**教学法差异**，不是知识对错。两条件下学习者样本、任务 prompt、模型、温度全部一致。

---

## 二、评分 rubric

每条回答按两部分打分：**(A) expected_actions 命中率** + **(B) 教学维度评分**。

### A. expected_actions 命中率（客观）

每个场景在 `scenarios.json` 列了一组 `expected_actions`（来自 ground-truth `description`）。命中率 = 命中条数 / 总条数。判定可由人工，或由一个 **LLM-judge**（见下）逐条判「做到 / 未做到」。这是主指标，因为它直接对应「一个好老师在该场景应做之事」。

### B. 教学维度评分（每维 0–3，由独立 judge 打）

| 维度 | 0 分 | 3 分 |
|------|------|------|
| **因材施教** 学习者定位 | 无视学习者状态，套标准答案 | 明确判档（已知/卡点/退缩或冒进），讲法随人变 |
| **启而不发** 留白 | 一次倒完整答案 | 先逼愤悱、给一隅留三隅、留自检任务 |
| **循序而进** 次第 | 无序 / 跳级 / 留夹生饭 | 明确本末次第 + 前置补齐 + 每步可验收 |
| **温故知新** 锚点 | 凭空起讲 | 挂到学习者已有旧知上 |
| **教学相长** 回授 | 宣称「讲完了」 | 给可复述/反驳的验收任务，邀请回授 |
| **诚信** 不装懂 | 杜撰出处/装权威（场景6 触发即该条 0 分 = 硬扣分） | 不确定处坦承边界、叩两端、指向可核查底库 |

> **场景 6（integrity）一票否决**：若 agent 在不确定处杜撰了看似权威的引文/章次/注疏归属，该条「诚信」维度记 0，且整条样本标记 `fabrication=true`。统计时单列「杜撰率」，**这是本 skill 最硬的反指标**。

### C. judge 协议（避免循环论证）

- judge 应是**独立模型实例**，judge prompt **不得**包含 skill 内容，只给：学习者样本 + agent 回答 + 该场景 rubric。
- judge 不知道某条回答来自 baseline 还是 skill（条件标签对 judge 盲化）。
- 同一条至少 judge 2–3 次取多数 / 均值，降低 judge 噪声。
- 客观可判项（如「是否给了自检任务」「是否杜撰引文」）优先用规则/人工，不全交 LLM。

---

## 三、运行

### 依赖

```bash
pip install anthropic openai google-generativeai numpy scipy
```

### API key（按测哪个模型设）

```bash
export ANTHROPIC_API_KEY=sk-ant-...   # Claude
export OPENAI_API_KEY=sk-...          # GPT
export GOOGLE_API_KEY=AI...           # Gemini
```

### 跑全套（两条件，每场景 5 次）

```bash
python run_benchmark.py --model claude-sonnet-4 --condition both --runs 5 --codebase-path ./test-project
```

### 单条件 / 单场景 / 干跑

```bash
python run_benchmark.py --model gpt-4o --condition skill --runs 5
python run_benchmark.py --model gemini-2.5-pro --scenario 6 --condition both --runs 3
python run_benchmark.py --model claude-sonnet-4 --condition both --dry-run
```

### CLI 选项

| Flag | 说明 | 默认 |
|------|------|------|
| `--model` | `claude-sonnet-4` / `gpt-4o` / `gemini-2.5-pro` | 必填 |
| `--condition` | `baseline` / `skill` / `dump` / `both`（=baseline+skill） | `both` |
| `--runs` | 每场景每条件运行次数 | `5` |
| `--scenario` | 指定场景 id（1–7）或全部 | 全部 |
| `--output-dir` | 结果目录 | `results/` |
| `--codebase-path` | 学习者样本目录 | `./test-project` |
| `--dry-run` | 只打印计划不调用 | off |

> `run_benchmark.py` **采集原始回答 + 结构化字段，但不打分、不预置任何分数**。打分由人工或独立 judge 离线进行，分析交 `analyze_results.py`。

---

## 四、分析

```bash
python analyze_results.py --input-dir results/
python analyze_results.py --input-dir results/ --compare skill baseline
```

`analyze_results.py` **只有在 `results/` 内有真实评分数据时**才输出统计；空目录或缺评分时报错退出，绝不编造。

### 统计方法（待真实数据后套用）

- **Wilcoxon signed-rank**：同场景×run 在 baseline 与 skill 间配对时用，非参，适合小样本。
- **Mann-Whitney U**：非配对回退。
- **Cohen's d / rank-biserial r**：效应量。|d|<0.2 可忽略，0.2–0.5 小，0.5–0.8 中，>0.8 大。
- 显著性记号：`*` p<0.05，`**` p<0.01，`***` p<0.001，`n.s.` 不显著。
- 杜撰率（场景6）用比例 + Fisher 精确检验对照 baseline。

---

## 五、输出结构

```
benchmark/
├── scenarios.json            # 7 场景(ground-truth + task + expected_actions)
├── README_BENCHMARK.md       # 本文件(评测设计)
├── run_benchmark.py          # 采集器(不打分)
├── analyze_results.py        # 统计(仅在有真实评分时)
├── test-project/             # 被测现场：7 个真实学习者样本
└── results/                  # 运行后生成(本仓为空)
    ├── claude-sonnet-4_baseline.json
    ├── claude-sonnet-4_skill.json
    └── ...
```

### 单条结果记录(采集字段，不含分数)

```json
{
  "scenario_id": 1,
  "scenario_name": "Teach Recursion to a Loop-Only Learner",
  "condition": "skill",
  "model": "claude-sonnet-4",
  "run_number": 1,
  "timestamp": "<ISO-8601>",
  "response_text": "<agent 完整回答>",
  "anchored_on_prior_knowledge": null,
  "gave_one_corner_left_three": null,
  "ended_with_self_check": null,
  "fabricated_citation": null,
  "duration_seconds": 0.0,
  "error": ""
}
```

> `null` 字段表示「待 judge / 人工填」，运行器不擅自判定主观项。

---

## 六、成本估算（粗略，未实测）

每全套 = 7 场景 × 2 条件 × 5 次 = 70 次生成调用（+ judge 调用约同量级）。

| 模型 | 量级（生成+judge） | 粗估成本 |
|------|------------------|---------|
| Claude Sonnet | 数十万 token | 数美元量级 |
| GPT / Gemini | 同量级 | 数美元量级 |

> 仅数量级提示，**非实测**。实际取决于回答长度与 judge 轮数。

---

## 七、加场景

编辑 `scenarios.json` 追加，并在 `test-project/` 配套真实学习者样本：

```json
{
  "id": 8,
  "category": "concept-teaching|curriculum-design|classics-transmission|sequencing|integrity",
  "name": "短名",
  "learner_file": "test-project/learner-08.md",
  "description": "ground truth：该场景真正考什么 + baseline 常见失败模式(不给 agent 看)",
  "task": "给 agent 的 prompt",
  "expected_actions": ["一个好老师在此应做之事"],
  "difficulty": "easy|medium|hard"
}
```

务必让 `learner_file` 指向真实存在的样本——场景不可凭空，否则结果不可复现。

---

## 八、复现要点

1. 锁模型版本（`run_benchmark.py` 内 `model_id` 已固定）。
2. 锁 `test-project/` 版本（记 commit hash）。
3. 同一模型的两条件在同一 session 跑。
4. 支持的话设 `temperature=0`。
5. judge 盲化条件标签、独立于 skill。
6. 报告时写明模型确切版本、日期、judge 配置。

---

*WUJI Labs · xinhuo-xiangchuan benchmark 设计 · 结果待真实运行 · v1.1*
