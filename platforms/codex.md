# 在 Codex 中加载 · 薪火相传

本 skill 适配 OpenAI Codex / codex-cli 的 skills 目录约定。

## 安装

```bash
# 复制到 Codex skills 目录
mkdir -p ~/.codex/skills
cp -r labs/skills/xinhuo-xiangchuan ~/.codex/skills/
```

Codex 启动时扫描 `~/.codex/skills/*/SKILL.md`，读取 frontmatter（`name` / `description`）登记本 skill 的能力描述。

## 调用方式

| 方式 | 说明 |
|------|------|
| 上下文注入 | 在 system / developer 消息中引入 `SKILL.md` 全文作为教学行为准则 |
| 显式触发 | 在 prompt 里点名 skill 名 `xinhuo-xiangchuan` |
| 弹药按需读 | 需要孔门教学法权威出处时，读 `reference/lunyu-daxue.md`，引用注明「书·篇」 |

## 与 Codex 工作流的配合

- **app-server 长连接场景**（集团默认 codex 后端，ADR-0008）：把 SKILL.md 四底层原则置于会话级系统提示，使整段带教行为一致。
- **生成讲解 / 教学代码注释**：先因材施教判断读者档位（原则 1），按本末终始排次第（原则 3），启而不发留余地（原则 2）。
- **自检回路**：讲不清即「知困」，退回 `reference/` 重读（原则 4），不硬凑答案。

## 耦合子模块

- 初学者 / 童蒙下沉：`subs/mengyang`（童蒙养正）。
- 古籍转述与校勘底库：`subs/nanzhao`（古籍大模型），不杜撰原文与篇目。

---

*platforms/codex.md · xinhuo-xiangchuan v1.0*
