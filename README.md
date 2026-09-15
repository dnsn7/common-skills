# 常用 Skills

这个仓库收录可复用的 Codex Skills。每个一级文件夹都是一个独立 Skill，可按需复制到 Codex 的 Skills 目录中使用。

## Skills 简介

### `lunwen-ppt`

面向学术论文精读与组会汇报。它可以把论文 PDF 整理为有证据定位的中文汇报方案，核验论文发表状态与会议/期刊等级，梳理方法、实验、局限和复现条件，并生成可编辑 PPTX。工作流强调论文事实与外部扩展分离、图表可读性以及导出后的视觉检查。

主要内容：

- `SKILL.md`：完整工作规范
- `references/`：证据、论文分析、知识库和 venue 核验规则
- `assets/`：幻灯片结构与主题配置
- `scripts/`：论文检查、演讲稿构建及 PPTX 清理辅助脚本

### `paper-batch-analysis`

面向单篇或文件夹内多篇论文的批量中文分析。它按固定结构说明完整标题、发表渠道与影响因子、研究问题、方法流程、数据与效果、研究价值、重要纠偏以及公开代码和复现边界，并生成不覆盖旧结果的编号 Markdown 报告。

主要内容：

- `SKILL.md`：批量扫描、证据核验、固定输出结构和交付检查规则
- `agents/openai.yaml`：Skill 的展示与调用配置

## 安装

将需要的 Skill 文件夹完整复制到 Codex Skills 目录。例如：

```text
~/.codex/skills/lunwen-ppt/
~/.codex/skills/paper-batch-analysis/
```

重新启动或刷新 Codex 后即可识别。请保留每个文件夹中的 `SKILL.md` 及其配套资源。

<img width="1920" height="980" alt="image" src="https://github.com/user-attachments/assets/1c2752c6-9831-424e-ac15-44340cd00009" />



## License

[MIT](LICENSE)
