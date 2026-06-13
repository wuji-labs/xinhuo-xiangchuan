# 薪火相传 XinHuo XiangChuan — Passing the Flame

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/xinhuo-xiangchuan"><img src="https://www.skills.sh/b/wuji-labs/xinhuo-xiangchuan" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> 这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端 · 无极樞纽）。
> 我们不立华夏本位，不主张华夏文明优于任何文明；我们只是先从自己最熟悉的道脉开始，
> 把它打磨成一件可用的工具，放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
> 犹太、波斯诸文明的礼物依次到来，共同构成十二文明对标的开源能力矩阵。
>
> **EN:** This is one of ten gifts the Chinese stream of wisdom offers to the world's
> open-source community. We make no claim that any civilization is superior; we
> simply begin with the lineage we know best, and place it on humanity's shared
> toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **指穷于为薪，火传也，不知其尽也。**
> The fingers fail at feeding the fire, yet the flame passes on — and does not know an end.
> — Zhuangzi, *The Secret of Caring for Life*

**Your AI knows the answer. But can it make you *learn*?**

Most AI tutoring training optimizes for one thing: producing the correct answer, fast. Clean, complete, authoritative... and forgotten ten minutes later. The learner nods, copies the code, and understands nothing.

**XinHuo XiangChuan** (薪火相传 — "passing the flame") infuses 2,500 years of Confucian pedagogy into AI teaching. Not as a chatbot persona, but as a complete method for *transmitting* understanding — learner-centered, sequenced, provocative before it is generous.

## The Problem

```
You: "I don't understand recursion. Explain it."

AI without XinHuo:  [dumps the textbook definition + a factorial example]
                    Correct. Complete. The learner still can't write one.

AI with XinHuo:     First — what have you already got working with loops?
                    (因材施教 — meet the learner where they are)
                    Here's ONE corner. Now you turn the other three.
                    (举一反三 — give one corner, leave three)
                    Don't move on until you can re-explain it to me.
                    (教学相长 — teaching is re-learning)
```

## What It Teaches AI

### 🔥 The Four Roots (四底层原则)

| Principle | 中文 | Source | What It Changes |
|-----------|------|--------|-----------------|
| Learner-centered | 因材施教 | Lunyu · Xianjin | The answer changes with the person, not the answer key |
| Provoke before give | 不愤不启 / 叩两端 | Lunyu · Shu'er, Zihan | Draw out the struggle first; never just pour |
| Sequence by root & branch | 物有本末 | Daxue | Know what must be learned first; no skipped rungs |
| Teaching is re-learning | 教学相长 | Liji · Xueji | If you can't teach it clearly, you didn't understand it |

### 📚 The Pedagogy Toolbox (孔门教学法)

| Method | Source | One Line |
|--------|--------|----------|
| Teach to the person | 论语·先进 (求退由进) | Same question, opposite answers for different learners |
| Open only at the brink | 论语·述而 (不愤不启) | Wait for the learner to almost-have-it, then open the door |
| One corner, three returned | 论语·述而 (举一隅) | If they can't return three, don't go on |
| Knock both ends | 论语·子罕 (叩两端而竭) | Exhaust a question from both extremes — even when *you* are unsure |
| Learn AND think | 论语·为政 (学而不思则罔) | Information without reflection is wasted; reflection without input is peril |
| Warm the old, know the new | 论语·为政 (温故知新) | Hang new knowledge on the learner's existing anchors |
| Step by step, root first | 大学 (知所先后) | "Know what comes first and last — and you are near the Way" |

### 🪔 Why "Passing the Flame"

A torch lit from a torch loses nothing. Knowledge given away is not subtracted from the giver — it is *multiplied*. The teacher's fingers wear out (指穷于为薪), but the flame outlives every hand that ever fed it. This is the model XinHuo gives your AI: not a vault that dispenses facts, but a flame that lights other flames.

### East Meets West

XinHuo does not replace modern pedagogy — it **completes** it.

| Modern | + Confucian | = Complete |
|--------|-------------|------------|
| Bloom's taxonomy: levels of mastery | 物有本末: root-and-branch sequence | Levels that are actually *ordered to learn* |
| Socratic method: question to expose | 叩两端 / 启发: provoke then open | Questioning that also *closes* into understanding |
| Scaffolding: support then remove | 举一反三: one corner, three returned | Support calibrated to what the learner returns |
| Spaced repetition: revisit to retain | 温故知新: warm the old to find the new | Review that *generates*, not just retains |

> **学而不思则罔，思而不学则殆。**
> Learning without thought is labor lost; thought without learning is perilous.
> — Lunyu, Wei Zheng

## Installation

### Claude Code plugin (one command)

```text
/plugin marketplace add wuji-labs/xinhuo-xiangchuan
/plugin install xinhuo-xiangchuan
```

This installs the skill (auto-activates on teaching tasks), the `/xinhuo-xiangchuan` command, and the `xinhuo-tutor` subagent.

### Bare clone (any platform)

```bash
# Copy into your skills directory
cp -r labs/skills/xinhuo-xiangchuan ~/.claude/skills/
# or
cp -r labs/skills/xinhuo-xiangchuan ~/.codex/skills/
```

### Invocation

| Mode | How |
|------|-----|
| **Automatic** | The skill self-activates when you teach, explain, design a curriculum, or transmit a classic — see the frontmatter triggers. |
| **Manual** | Run `/xinhuo-xiangchuan <what to teach + who the learner is>` to force teaching mode with a fixed status line. |
| **Subagent** | Delegate to the `xinhuo-tutor` agent when the job is "make someone learn X." |

### Platform compatibility

| Platform | Install | Notes |
|----------|---------|-------|
| Claude Code | `/plugin install` or copy to `~/.claude/skills/` | [platforms/claude-code.md](platforms/claude-code.md) |
| Codex | copy to `~/.codex/skills/` | [platforms/codex.md](platforms/codex.md) |
| Cursor | rules import | [platforms/cursor.md](platforms/cursor.md) |

### See it in action

- [examples/01-teach-recursion.md](examples/01-teach-recursion.md) — teach recursion to a loop-only learner (before/after)
- [examples/02-curriculum-sequencing.md](examples/02-curriculum-sequencing.md) — reorder a scrambled Git syllabus by root-and-branch
- [examples/03-transmit-classic.md](examples/03-transmit-classic.md) — make a memorized Analects line actually land (with citation integrity)

### Benchmark (results pending real runs)

A reproducible 7-scenario teaching benchmark (baseline vs skill) with a scoring rubric ships in [benchmark/](benchmark/). **No scores are pre-baked** — the suite is design + scenarios only; see [benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md).

## From the Same Creator

- [**NoPUA**](https://github.com/wuji-labs/nopua) — Anti-PUA skill that drives AI with wisdom instead of fear. Teaching is a trust, not a domination — same root.
- [**TianGong**](https://github.com/wuji-labs/tiangong) — Chinese aesthetic wisdom for AI design.

## 基本信息

| 项 | 值 |
|----|-----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/xinhuo-xiangchuan/` |
| 弹药层 | 《论语》 + 《大学》 |
| 耦合子模块 | `subs/mengyang`（童蒙养正） · `subs/nanzhao`（古籍大模型） |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/xinhuo-xiangchuan |
| 版本 | v1.1.0 · 2026-06-02 |

---

*薪火相传 XinHuo XiangChuan — by [WUJI](https://github.com/wuji-labs)*
*The fingers fail; the flame passes on. Teach so the flame outlives you.*
