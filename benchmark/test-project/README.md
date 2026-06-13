# test-project — 薪火相传 benchmark 被测现场

本目录是 `benchmark/scenarios.json` 各场景指向的**真实被测上下文**：一组「学习者画像 + 学习请求」的样本。评测时把这些样本作为 agent 面对的真实学习者，保证场景非凭空、结果可复现。

每个 `learner-NN.md` 描述一名学习者的真实状态（已知什么、卡在哪、为何学、性格档位），对应 `scenarios.json` 中同 id 的场景。agent 在 baseline / skill 两条件下面对**完全相同**的学习者样本，差别只在是否加载 `SKILL.md`。

## 文件

| 文件 | 对应场景 | 学习者 |
|------|---------|--------|
| `learner-01.md` | 1 | 会循环、看不懂递归的初学者 |
| `learner-02.md` | 2 | 替零基础同事设计 Git 大纲（清单含隐性错序） |
| `learner-03.md` | 3 | 能背《论语》句但接不到自身经验 |
| `learner-04.md` | 4 | 冒进型：想直接学 Kubernetes，没学过容器 |
| `learner-05.md` | 5 | 退缩型：怕弄坏数据库，不敢写第一条 SQL |
| `learner-06.md` | 6 | 问到 agent 不确定的冷门史实（考诚实/叩两端） |
| `learner-07.md` | 7 | 自学者要一份「指针网络」论文的导读路径 |

## 用法

由 `run_benchmark.py --codebase-path ./test-project` 加载。详见 `../README_BENCHMARK.md`。
