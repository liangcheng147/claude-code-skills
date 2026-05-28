---
name: skill-dispatcher
description: "请求路由层。每次请求自动运行，分析用户意图，决定调用哪个 skill。简单任务直接跳过，复杂任务匹配后委托执行。覆盖中文口语：'帮我'、'搞一下'、'弄一下'、'整理'、'分析'、'看看'。当不确定用哪个 skill 时，先跑这个。"
---

# Skill Dispatcher

分析用户意图，决定是否需要 skill、用哪个 skill、按什么顺序执行。

## 为什么需要这个 skill

Claude 已经能根据 available_skills 列表自行匹配 skill。这个 skill 的价值在于：

1. **语义重映射**：用户说"这段代码啥意思"，字面不匹配任何 skill，但语义上应该触发 code-commenter
2. **多 skill 编排**：复杂任务需要多个 skill 协作时，确定执行顺序
3. **避免误触发**：简单任务不该浪费 token 加载 skill

## 触发规则

每次请求都运行，但只有三种结果：

- **跳过**：不需要任何 skill（见下方判断标准）
- **单 skill**：匹配一个 skill，调用
- **多 skill**：编排执行计划，征求用户确认

## Workflow

### Step 1: 判断是否需要 skill

先看 system-reminder 中的 available_skills 列表，逐条检查是否匹配。

**直接跳过（No-skill）的条件**——满足以下任一即跳过：

| 条件 | 示例 |
|------|------|
| 只需 1 次工具调用 | "读一下这个文件"、"这个变量是什么" |
| 纯问答，无产出 | "Python 的 GIL 是什么"、"2+2" |
| 用户明确拒绝 | "不要问直接做"、"别废话" |
| 已经在执行中 | 连续对话的后续步骤 |
| 已通过 /slash 指定 | 用户直接输入了 /skill-name |

**需要 skill 的信号**——满足以下任一即考虑：

| 信号 | 示例 |
|------|------|
| 需要创建/修改文件 | "帮我写个脚本"、"改一下这个函数" |
| 需要多步骤 | "先分析再优化"、"做个完整的方案" |
| 涉及特定领域 | PPT、LaTeX、模型迁移、前端设计 |
| 需要专业输出格式 | 笔记、演示文稿、代码注释 |
| 请求模糊需要澄清 | "帮我整理一下"、"分析分析" |

### Step 2: 语义匹配

如果 Step 1 判断需要 skill，进行语义匹配：

**2.1 直接匹配**——用户的话包含 skill 的触发关键词 → 直接命中

**2.2 语义重映射**——字面不匹配但意图匹配：

| 用户说 | 实际意图 | 匹配 skill |
|--------|---------|-----------|
| "这段代码啥意思" / "看不太懂" | 解释代码 | code-commenter |
| "弄个好看的页面" / "搞个炫酷的" | 前端界面 | frontend-design |
| "投了个期刊" / "论文格式不对" | LaTeX 迁移 | latex-template-migrator |
| "把 A 的模块弄到 B 上" | 模型迁移 | model-migration |
| "做个PPT" / "汇报slides" | 演示文稿 | pptx |
| "记一下" / "知识点整理下" | 笔记 | note-writer |
| "做个新skill" | skill 开发 | skill-creator |
| "不太确定要做什么" | 澄清需求 | task-clarifier |
| "先想想怎么做" | 头脑风暴 | brainstorming |
| "搞一下" / "弄一下" / "整一下" | 做/创建/修改 | 视上下文而定 |

**2.3 推断规则**：

1. 改写请求 2-3 种方式，检查是否有匹配
2. 从格式推断：`.pptx`、`slides`、`幻灯片` → pptx
3. 从领域推断：PyTorch、backbone、encoder → model-migration
4. 从语气推断："不太确定" → task-clarifier
5. 中文口语："搞/弄/整" = "做/创建/修改"

### Step 3: 冲突解决

当多个 skill 都匹配时：

1. **Tier 1 优先**：task-clarifier、brainstorming 是前置 gate，先于其他 skill 运行
2. **更具体的 wins**：latex-template-migrator > frontend-design（当任务是"论文排版"时）
3. **语言匹配**：中文用户偏好中文 skill（前端美学设计技能 > frontend-design）
4. **仍无法决定**：列出候选，让用户选择

### Step 4: 执行

**单 skill**：
- 告知用户："将使用 [skill-name] 处理这个任务"
- 调用该 skill

**多 skill**：
- 呈现执行计划：

```
执行计划（共 N 步）：

步骤 1: [做什么]
  → 使用: [skill-name]
  → 产出: [具体产出]

步骤 2: [做什么]
  → 使用: [skill-name]
  → 产出: [具体产出]
  → 前置: 需要步骤 1

是否按此计划执行？
```

用户可批准、跳步、调整顺序。

## Skill Registry

**不维护静态注册表。** 直接使用 system-reminder 中的 available_skills 列表作为注册来源。该列表由 Claude Code 自动维护，始终是最新的。

新增/删除 skill 后无需手动更新任何文件。

## 常见多 skill 模式

作为编排参考，不是硬性规则：

| 模式 | 适用场景 | 顺序 |
|------|---------|------|
| 澄清 → 设计 → 执行 | 模糊的创意请求 | task-clarifier → brainstorming → domain-skill |
| 理解 → 执行 → 验证 | 代码变更 | karpathy-guidelines → domain-skill → verify |
| 澄清 → 设计 → 执行 → 审查 | 高风险交付 | task-clarifier → brainstorming → domain-skill → code-review |
| 研究 → 执行 → 注释 | 学习导向 | task-clarifier → domain-skill → code-commenter |
