# 在 Claude Code 中加载 · 薪火相传

本 skill 适配 Claude Code 的 Agent Skills 机制（`SKILL.md` + frontmatter）。

## 安装

```bash
# 项目级（推荐：随仓库走，团队共享）
mkdir -p .claude/skills
cp -r labs/skills/xinhuo-xiangchuan .claude/skills/

# 或用户级（个人全局可用）
cp -r labs/skills/xinhuo-xiangchuan ~/.claude/skills/
```

Claude Code 会自动发现 `SKILL.md` 的 frontmatter（`name: xinhuo-xiangchuan` / `description`），并在对话语境匹配「教学 / 讲解 / 带教 / 设计学习路径」时自动加载。

## 调用方式

| 方式 | 说明 |
|------|------|
| 自动触发 | 当你请求「教我 X」「帮我讲清楚 Y」「设计一份学习路径」时，Claude 依据 `description` 自动援引本 skill |
| 显式触发 | 在 prompt 里点名：「用 xinhuo-xiangchuan 的方式教我递归」 |
| 弹药调用 | Claude 需要权威出处时，读 `reference/lunyu-daxue.md`，引用注明「书·篇」 |

## 与 Claude Code 工作流的配合

- **Code review 带教**：在 review 注释里，不直接给改法，先「举一隅」点出方向，让作者「反三隅」——见 SKILL.md 原则 2。
- **解释代码 / 概念**：先判断对方已知（原则 1 因材施教），再按「本末终始」排讲解次第（原则 3）。
- **自检**：若 Claude 讲不清，触发「教然后知困」（原则 4），退回 `reference/` 重读再讲，而非硬编。

## 耦合子模块

- 面向初学者下沉讲法：参 `subs/mengyang`（童蒙养正）。
- 转述古籍 / 需要校勘：底库走 `subs/nanzhao`（古籍大模型），避免造引用。

---

*platforms/claude-code.md · xinhuo-xiangchuan v1.0*
