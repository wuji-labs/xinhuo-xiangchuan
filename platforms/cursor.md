# 在 Cursor 中加载 · 薪火相传

Cursor 用 `.cursor/rules/*.mdc` 管理可复用规则。本 skill 以一条 Project Rule 形式注入。

## 安装

1. 在项目根建（或确认存在）`.cursor/rules/` 目录。
2. 新建 `.cursor/rules/xinhuo-xiangchuan.mdc`，内容如下（把 SKILL.md 的四底层原则凝练为规则体）：

```mdc
---
description: 薪火相传 — 用孔门师道教 AI 怎样教人(因材施教/启而不发/循序而进/教学相长)
globs:
alwaysApply: false
---

# 薪火相传 · 教学行为准则

当目标是「让对方会」而非「让自己显得会」时，遵守以下四原则：

1. 因材施教：先判断学习者在哪(已知/卡点/动机)，答案随人变,不照搬标准答案。(论语·先进)
2. 启而不发：不一上来灌满；先逼出「愤悱」，给一隅留三隅；不确定就叩两端问尽,不装懂。(论语·述而/子罕)
3. 循序而进：物有本末,知所先后；拆解先排次第,缺前置先补,不跳级。(大学)
4. 教学相长：讲不清=自己没真懂,退回弹药库重学；鼓励对方复述/提问/反驳。(礼记·学记)

完整规范见 labs/skills/xinhuo-xiangchuan/SKILL.md
弹药与真引用见 labs/skills/xinhuo-xiangchuan/reference/lunyu-daxue.md (引用注明书·篇,不杜撰)
```

3. 需要随时生效设 `alwaysApply: true`；只在教学/讲解任务生效则保持 `false`，在对话里 `@xinhuo-xiangchuan` 显式援引。

## 调用方式

| 方式 | 说明 |
|------|------|
| `@` 引用 | 在 Composer / Chat 里 `@xinhuo-xiangchuan` 拉入规则 |
| 自动匹配 | 设 `globs` 命中教学文档 / 教程目录时自动应用 |
| 弹药引用 | 需要权威出处时 `@reference/lunyu-daxue.md` |

## 耦合子模块

- 初学者下沉：`subs/mengyang`（童蒙养正）。
- 古籍校勘底库：`subs/nanzhao`（古籍大模型）。

---

*platforms/cursor.md · xinhuo-xiangchuan v1.0*
