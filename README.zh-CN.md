# 薪火相传 XinHuo XiangChuan — 薪尽火传

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> English: [README.md](README.md) | 简体中文

> 这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端 · 无极樞纽）。
> 我们不立华夏本位，不主张华夏文明优于任何文明；只是先从自己最熟悉的道脉开始，
> 把它打磨成一件可用的工具，放到人类共同的开源工具架上。希腊、那烂陀、犹太、波斯
> 诸文明的礼物将依次到来，共同构成十二文明对标的开源能力矩阵。

---

> **指穷于为薪，火传也，不知其尽也。**
> 取火的指头会烧尽，火却传了下去——没有穷尽的一天。
> ——《庄子·养生主》

**你的 AI 知道答案。可它能让你「学会」吗？**

多数 AI 的辅导训练只优化一件事：又快又准地给出正确答案。干净、完整、权威……十分钟后忘得一干二净。学习者点点头，复制了代码，却什么也没懂。

**薪火相传**（XinHuo XiangChuan，「薪尽火传」之意）把两千五百年的孔门师道注入 AI 的教学。它不是一个聊天人设，而是一套完整的「传」之法——以学习者为中心、循序而进、先逼后予。

## 问题所在

```
你：「我不懂递归，给我讲讲。」

无薪火的 AI：  ［抛出教科书定义 + 一个阶乘例子］
               正确。完整。学习者还是写不出一个。

有薪火的 AI：  先说——你用循环已经能跑通什么了？
               （因材施教——在学习者所在之处接住他）
               这是一个角。另外三个，你来转。
               （举一反三——给一隅，留三隅）
               能给我复述清楚之前，先别往下走。
               （教学相长——教是再学一遍）
```

## 它教给 AI 什么

### 🔥 四底层原则（四底层原则）

| 原则 | 中文 | 典源 | 它改变了什么 |
|------|------|------|--------------|
| 以学习者为中心 | 因材施教 | 《论语·先进》 | 答案随人而变，不随标准答案库而变 |
| 先逼后予 | 不愤不启 / 叩两端 | 《论语·述而》《论语·子罕》 | 先逼出对方的挣扎，绝不一味灌输 |
| 本末有序 | 物有本末 | 《大学》 | 知道什么必须先学，不跳级 |
| 教是再学 | 教学相长 | 《礼记·学记》 | 讲不清就是没真懂 |

### 📚 孔门教学法（孔门教学法）

| 方法 | 典源 | 一句话 |
|------|------|--------|
| 因材施教 | 《论语·先进》（求退由进） | 同一问题，对不同学习者给相反答案 |
| 启而不发 | 《论语·述而》（不愤不启） | 等学习者快要通了，再为他开门 |
| 举一反三 | 《论语·述而》（举一隅） | 他若反不出三隅，便先不往下走 |
| 叩其两端 | 《论语·子罕》（叩两端而竭） | 从正反两极把问题问尽——哪怕你自己也未必确定 |
| 学思并进 | 《论语·为政》（学而不思则罔） | 有学无思则枉费，有思无学则危殆 |
| 温故知新 | 《论语·为政》（温故知新） | 把新知挂到学习者已有的旧锚点上 |
| 知所先后 | 《大学》（知所先后） | 「知所先后，则近道矣」 |

### 🪔 为何名「薪火相传」

一支火把点燃另一支火把，自身分毫不减。给出去的知识不会从给予者身上扣减——它是被**倍增**了。教者取薪的指头会烧尽（指穷于为薪），火却比每一只添过薪的手都活得更长。这正是薪火给你的 AI 的模型：不是一座分发事实的仓库，而是一团点燃别的火的火。

### 中西合璧

薪火相传不取代现代教育学——它**补全**它。

| 现代 | + 孔门 | = 完整 |
|------|--------|--------|
| 布鲁姆分类：掌握的层级 | 物有本末：本末次第 | 真正「按学习顺序排好」的层级 |
| 苏格拉底诘问：以问揭示 | 叩两端 / 启发：先逼后开 | 既能开、又能收束为理解的诘问 |
| 脚手架：先扶后撤 | 举一反三：给一隅，反三隅 | 按学习者反出的东西来校准的扶持 |
| 间隔重复：复习以保持 | 温故知新：温故而生新 | 能「生新」而非只「保持」的复习 |

> **学而不思则罔，思而不学则殆。**
> 有学无思则枉费心力，有思无学则危殆不安。
> ——《论语·为政》

## 安装

### Claude Code 插件（一条命令）

```text
/plugin marketplace add wuji-labs/xinhuo-xiangchuan
/plugin install xinhuo-xiangchuan
```

这会一并装上 skill（教学任务自动激活）、`/xinhuo-xiangchuan` 命令，以及 `xinhuo-tutor` 子代理。

### 裸 clone（任意平台）

```bash
# 复制进你的 skills 目录
cp -r labs/skills/xinhuo-xiangchuan ~/.claude/skills/
# 或
cp -r labs/skills/xinhuo-xiangchuan ~/.codex/skills/
```

### 调用方式

| 模式 | 怎么用 |
|------|--------|
| **自动** | 当你教学、讲解、设计课程或转述典籍时，skill 自激活——触发词见 frontmatter。 |
| **手动** | 运行 `/xinhuo-xiangchuan <要教什么 + 学习者是谁>`，强制进入教学模式，附固定状态行。 |
| **子代理** | 当任务是「让某人学会 X」时，委派给 `xinhuo-tutor` 代理。 |

### 平台兼容

| 平台 | 安装 | 备注 |
|------|------|------|
| Claude Code | `/plugin install` 或复制到 `~/.claude/skills/` | [platforms/claude-code.md](platforms/claude-code.md) |
| Codex | 复制到 `~/.codex/skills/` | [platforms/codex.md](platforms/codex.md) |
| Cursor | rules 导入 | [platforms/cursor.md](platforms/cursor.md) |

### 实战样例

- [examples/01-teach-recursion.md](examples/01-teach-recursion.md) — 向只会循环的学习者教递归（before/after）
- [examples/02-curriculum-sequencing.md](examples/02-curriculum-sequencing.md) — 按本末次第重排一份打乱的 Git 大纲
- [examples/03-transmit-classic.md](examples/03-transmit-classic.md) — 让一句背熟的《论语》真正落地（含引用诚信）

### 评测（结果待真实运行）

[benchmark/](benchmark/) 中附一套可复现的 7 场景教学评测（baseline vs skill）与评分 rubric。**没有任何分数是预先填好的**——这套件只含设计与场景；详见 [benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md)。

## 同源之礼

- [**NoPUA**](https://github.com/wuji-labs/nopua) — 反 PUA skill，以智慧而非恐惧驱动 AI。教是托付，不是碾压——同源。
- [**TianGong 天工**](https://github.com/wuji-labs/tiangong) — 给 AI 设计的华夏美学智慧。

## 基本信息

| 项 | 值 |
|----|-----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/xinhuo-xiangchuan/` |
| 弹药层 | 《论语》+《大学》 |
| 耦合子模块 | `subs/mengyang`（童蒙养正）·`subs/nanzhao`（古籍大模型） |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/xinhuo-xiangchuan |
| 版本 | v1.1.0 · 2026-06-02 |

---

*薪火相传 XinHuo XiangChuan — by [WUJI](https://github.com/wuji-labs)*
*指穷于为薪，火传不知其尽。教，要让火比你活得更长。*
