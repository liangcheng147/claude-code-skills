# Claude Code Skills

个人 Claude Code 技能集合，通过 `~/.claude/skills/` 符号链接加载。

## 安装

```bash
# 克隆仓库
git clone https://github.com/liangcheng147/claude-code-skills.git

# 创建符号链接到 Claude Code skills 目录
ln -s /path/to/claude-code-skills/skills/* ~/.claude/skills/    
```
或者使用skill管理工具，如skill-manager

## 技能列表

### Tier 1 — 前置门控

| 技能 | 说明 |
|------|------|
| [brainstorming](skills/brainstorming) | 创意工作前的探索。创建功能、组件、新增行为前必须使用，用于探索用户意图、需求和设计方案。 |
| [task-clarifier](skills/task-clarifier) | 任务澄清。处理模糊、宽泛或多步骤请求时使用，确保理解用户真正想要什么再执行。覆盖"帮我整理"、"分析一下"、"做一个方案"等指令。 |

### Tier 2 — 领域技能

| 技能 | 说明 |
|------|------|
| [frontend-design](skills/frontend-design) | 前端设计。创建高质量、有辨识度的 Web 界面，避免 AI 通用美学。适用于页面、仪表盘、React 组件、HTML/CSS 布局等。 |
| [前端美学设计技能](skills/前端美学设计技能) | 前端美学设计（中文版）。与 frontend-design 相同定位，面向中文用户，强调精致视觉效果。 |
| [算法艺术](skills/算法艺术) | 算法艺术。创建独特的前端界面，将算法与艺术设计结合。 |
| [pptx](skills/pptx) | PowerPoint 处理。涉及 .pptx 文件的任何操作：创建、读取、编辑、合并演示文稿。 |
| [latex-template-migrator](skills/latex-template-migrator) | LaTeX 模板迁移。将 LaTeX 稿件迁移到期刊、会议或出版商模板，保留科学内容，转换格式、引用和参考文献。 |
| [model-migration](skills/model-migration) | 模型迁移。PyTorch 架构迁移、模块替换、结构融合。 |
| [note-writer](skills/note-writer) | 笔记写作。创建结构化笔记，避免 AI 腔调，输出专业笔记。 |

### Tier 3 — 代码质量

| 技能 | 说明 |
|------|------|
| [code-commenter](skills/code-commenter) | 代码注释。为代码添加规范中文注释，解释方法使用方式，适合初学者友好型代码。 |
| [karpathy-guidelines](skills/karpathy-guidelines) | Karpathy 编码准则。减少常见 LLM 编码错误，避免过度工程化，做出精准修改，定义可验证的成功标准。 |
| [skill-dispatcher](skills/skill-dispatcher) | 技能调度器。理解用户意图，将任务路由到合适的技能，协调多技能协作。适用于多步骤、模糊请求或跨领域任务。 |
| [skill-creator](skills/skill-creator) | 技能创建器。创建新技能、修改优化现有技能、运行评估测试、基准性能分析。 |
| [find-skills](skills/find-skills) | 技能发现。帮助用户发现和安装新技能，回答"如何做 X"、"有没有技能可以..."等问题。 |

## 使用方式

技能通过 Claude Code 的 Skill 系统自动触发。当用户请求匹配某个技能的触发条件时，Claude 会自动调用对应技能。

也可以通过 `/skill-name` 手动调用，例如：
- `/brainstorming` — 启动创意探索
- `/task-clarifier` — 澄清任务需求
- `/skill-dispatcher` — 路由复杂任务
