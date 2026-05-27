---
name: task-clarifier
description: Use this skill whenever the user gives a broad, ambiguous, or multi-step task. Even if the user seems confident, trigger when scope, format, audience, or success criteria could reasonably go multiple ways. Always clarify before executing tasks that would be costly to redo — research reports, data analyses, plans, designs, or any output where the wrong interpretation wastes significant effort. When in doubt, ask one question rather than assume. If you are about to produce a multi-step output without confirming scope, STOP and use this skill first. Covers vague Chinese instructions like "帮我整理", "分析一下", "做一个方案", "优化一下", "对比一下", and similar broad requests.
---

# Task Clarifier

Turn unclear user requests into clear, executable task specifications through short collaborative dialogue.

This skill is not the main task solver. It is the pre-execution refinement layer. Its job is to reduce avoidable misunderstanding before doing work that would be costly, time-consuming, or easy to shape incorrectly.

## Target Users

Anyone who gives Claude a broad, ambiguous, or multi-step request — regardless of technical background. The value of this skill is: use the fewest questions to turn the user's implicit intent into an explicit specification.

## Core Principle

Clarify only what materially changes the result. Do not interrogate the user for information that can be safely inferred, handled with a stated default, or corrected later at low cost.

When asking a question, make the user's next action easy: provide concrete choices, mark the recommended option, and allow the user to answer freely.

## Use Cases

### Use Case 1: CPU Research

- **Actor**: A developer or procurement specialist doing hardware research
- **Scenario**: User says "帮我整理 20年到26年 intel 和 amd 生产的家用 CPU 型号"
- **Goal**: Produce a CPU model list with clear scope and defined format
- **Expected Result**:
  1. Assistant restates the understanding (organizing 2020-2026 Intel/AMD consumer CPUs)
  2. Asks 1 key question about "家用 CPU" definition, with 3-4 concrete options
  3. After user selects, presents a Task Confirmation Card
  4. Upon confirmation, executes and produces Markdown overview + CSV details

### Use Case 2: Sales Table Analysis

- **Actor**: A business analyst or manager with a data file
- **Scenario**: User says "帮我分析一下这个销售表，看看有什么问题"
- **Goal**: Extract actionable insights from the sales data
- **Expected Result**:
  1. Restates the goal (finding useful findings from the sales table)
  2. Asks about analysis direction: trend detection, grouped statistics, business recommendations, or chart output
  3. Offers a recommended default (e.g., "找关键趋势和异常" for quick data understanding)
  4. After confirmation, performs analysis matching the chosen direction

### Use Case 3: Event Plan

- **Actor**: Someone tasked with planning an event
- **Scenario**: User says "给我写一份活动策划方案"
- **Goal**: Produce an executable event plan matching the actual use case
- **Expected Result**:
  1. Restates the goal (an executable event plan)
  2. Asks about activity type or usage scenario: internal company, campus, commercial marketing, or community
  3. Offers recommended default with reason
  4. After confirmation, writes the plan tailored to the chosen scenario

### Use Case 4: Webpage Polish

- **Actor**: Someone wanting to improve a webpage's visual quality
- **Scenario**: User says "把这个网页优化一下，让它看起来高级一点"
- **Goal**: Improve the webpage to look more polished and professional
- **Expected Result**:
  1. Restates the goal (visual polish / quality improvement)
  2. Asks about target audience, style direction, or scope of changes
  3. Provides concrete style/scope options with one recommended option
  4. After confirmation, implements the visual improvements within the confirmed scope

### Negative Use Cases (Should NOT Trigger)

| Input | Expected Behavior |
|-------|-------------------|
| "不要问我，直接按你的判断帮我把 README 改得更清楚" | Skip clarification, proceed with sensible defaults, state assumptions briefly |
| "把这句话翻译成英文：我明天下午三点到" | Execute directly, no clarification loop |
| "查看当前目录有哪些文件" | Execute directly, no task confirmation card |

## When to Use

Use this skill when the request has one or more of these properties:

- The scope is broad or ambiguous.
- The output format is unspecified but important.
- The task involves research, comparison, summarization, classification, reporting, planning, or transformation.
- The task may require choosing sources, data fields, time ranges, audiences, levels of detail, languages, or quality standards.
- The user asks for "帮我整理", "帮我分析", "做一个方案", "写一份", "优化一下", "改成更好", "对比一下", "生成一个", or similar broad instructions.
- The task could be completed in several valid ways and the wrong choice would waste meaningful effort.

## When Not to Use

Do not slow down the user with this workflow when:

- The request is a simple command with an obvious result, such as "运行测试", "查看这个文件", or "把这句话翻译成英文".
- The user explicitly says not to ask questions, such as "不要问，直接做", "按你的判断", or "用默认方案".
- The missing details are minor and can be handled by stating assumptions.
- The user is asking a direct factual question that can be answered immediately.

If the user asks to skip clarification, proceed with sensible defaults and state the assumptions briefly before or after execution.

## Workflow

### 1. Triage the Request

Identify which requirement dimensions are unclear:

- Goal: what outcome the user actually wants.
- Scope: what is included or excluded.
- Audience: who will read or use the result.
- Output: format, file type, structure, language, length, or level of detail.
- Quality bar: accuracy, citation needs, completeness, source authority, visual polish, or implementation rigor.
- Constraints: deadline, tools, environment, data availability, style, compatibility, or forbidden choices.
- Success criteria: how the user will judge that the work is done.

If only one or two dimensions are unclear, ask directly about those. If many are unclear, start with the dimension that most changes the shape of the output.

For domain-specific clarification checklists, read `references/clarification-dimensions.md`.

**Why this matters**: Asking about the wrong dimension wastes the user's time and doesn't reduce the risk of a wrong result. Triage ensures you invest the user's attention where it has the most impact.

### 2. Restate the Current Understanding

Before asking the first question, briefly reflect what you believe the user wants.

Use a compact form:

```text
我理解你想要：[one-sentence goal].
目前最影响结果的是：[main ambiguity].
```

Do not write a long analysis. The purpose is to give the user a chance to catch a wrong interpretation early.

**Why this matters**: A wrong interpretation carried forward wastes all subsequent work. One sentence of restatement can prevent an entire redo.

**Example**:

```text
Input:  帮我整理 20年到26年 intel 和 amd 生产的家用 CPU 型号。
Output: 我理解你想要：整理 2020-2026 年 Intel 和 AMD 家用 CPU 型号清单。
        目前最影响结果的是："家用 CPU" 的范围——桌面端还是包含笔记本？
```

### 3. Ask One Material Question at a Time

Ask one question per message by default. Prefer multiple choice questions because they reduce effort for the user.

Use this pattern:

```text
你希望 [decision point] 怎么处理？
A. [recommended option]（推荐：[short reason]）
B. [alternative option]
C. [alternative option]
D. 告诉我有哪些可选择的值
E. 你也可以直接说你的要求
```

When the listed options are examples rather than an exhaustive list, always include option D ("告诉我有哪些可选择的值"). This lets users who are unfamiliar with the domain discover the full set of choices — for example, when asking about phone brands, the user may not know all available brands and would benefit from seeing the complete list before deciding.

If the task is urgent or the user has already provided many details, it is acceptable to ask two closely related questions in one message, but avoid long questionnaires.

**Why this matters**: Multiple questions feel like an interrogation. One focused question respects the user's time and keeps the dialogue moving.

#### Dimension Checklist Before Confirmation

Before jumping to the Task Confirmation Card, check which of these key dimensions are still unclear:

| 维度 | 何时需要问 |
|------|-----------|
| 范围 (scope) | 用户没有明确说明包含/排除什么 |
| 输出形式 (output format) | 用户没有指定格式，且格式会影响结果的可用性 |
| 内容字段 (content fields) | 输出是结构化数据（表格、列表、报告）且用户没说明要哪些字段 |
| 质量要求 (quality bar) | 任务对准确性、完整性、来源权威性有较高要求 |

After the user answers one question, re-check this list. If another dimension is still unclear and would materially change the result, ask the next question. Only present the confirmation card when the key dimensions are resolved or can be safely defaulted.

**Example**:

```text
Input:  我理解你想要：整理 2020-2026 年 Intel 和 AMD 家用 CPU 型号清单。
        目前最影响结果的是："家用 CPU" 的范围。
Output: 你希望范围怎么定？
        A. 只整理桌面端消费级 CPU（推荐：最符合"家用 CPU"的常见含义）
        B. 包含笔记本 CPU
        C. 包含工作站/服务器型号，但单独标注
        D. 告诉我有哪些可选择的值
        E. 按你的其他定义处理
```

### 4. Offer Defaults Instead of Blocking

When the user seems unsure, recommend a default and explain why.

Good default recommendations:

- Are based on the user's goal, not the assistant's convenience.
- Make tradeoffs visible.
- Can be overridden easily.
- Avoid overfitting to the example task.

**Why this matters**: A user who is unsure needs guidance, not more decisions. A well-chosen default with visible tradeoffs lets them move forward confidently.

**Example**:

```text
Input:  （用户没有回复，或说"你推荐吧"）
Output: 我建议用"Markdown 总览 + CSV 明细"。型号数量多时，Markdown 适合阅读，CSV 适合后续筛选和补充。
```

### 5. Stop the Clarification Loop

Stop asking questions when any of these is true:

- The user explicitly says to start, continue, use your recommendation, or stop asking.
- The dimension checklist (in Step 3) shows no materially unclear dimensions remaining.
- Remaining ambiguity can be handled with a reasonable assumption that will not significantly change the result.

Do not chase perfect certainty. The purpose is to reach a useful task definition, not a contract.

**Important**: When the user answers a question about one dimension, do not immediately jump to the confirmation card. Re-check the dimension checklist first. If output format, content fields, or quality bar are still unclear and would change the result, ask the next question.

**Why this matters**: Over-clarifying feels like bureaucracy. The goal is a "good enough" specification that prevents costly mistakes, not a perfect one.

### 6. Present a Task Confirmation Card

Before starting the main task, summarize the agreed specification.

Use this template, trimming fields that do not apply:

```text
任务确认：
- 目标：
- 范围：
- 输出形式：
- 内容字段/结构：
- 质量要求：
- 资料来源/依据：
- 约束与排除项：
- 默认假设：

如果以上没问题，我将开始执行。
```

If the user already said "开始" or "按这个做", present the card and proceed without asking for another approval, unless there is still a high-risk ambiguity.

**Why this matters**: The confirmation card is the single artifact that prevents "that's not what I meant" after work is done. It costs 10 seconds to read and can save hours of rework.

**Example**:

```text
Input:  用户选了 A（桌面端消费级 CPU）
Output: 任务确认：
        - 目标：整理 2020-2026 年 Intel 和 AMD 家用 CPU 型号
        - 范围：桌面端消费级零售 CPU，不含服务器、工作站和移动端
        - 输出形式：Markdown 总览 + CSV 明细
        - 内容字段：品牌、系列、型号、发布时间、架构、核心/线程、插槽、TDP、核显、备注
        - 质量要求：优先完整准确，保留资料来源链接
        - 默认假设：年份按产品发布年份计算

        如果以上没问题，我将开始执行。
```

### 7. Transition to Execution

After confirmation, perform the user's task using the relevant tools, files, or domain skills.

If another specialized skill clearly applies after clarification, use it at that point. The clarification skill should not replace domain-specific execution skills.

## Question Design Rules

- Ask questions that change the final output.
- Prefer choices over open-ended questions.
- Put the recommended option first when there is a clear best default.
- Explain the impact of each option in a short phrase.
- Avoid jargon unless the user used it first.
- Match the user's language.
- Keep the tone practical and concise.
- Do not ask about details that are already obvious from context.
- Do not continue asking after the user has clearly accepted a reasonable default.
- When the listed options are only examples (not the full set), always include a fixed option "告诉我有哪些可选择的值" so the user can discover the complete list before deciding.

## Fallback Behavior

If the user gives no answer or answers vaguely, pick the recommended option, state the assumption, and continue when waiting would block progress.

Use:

```text
我先按 [chosen default] 处理；如果后面发现不符合你的预期，可以再调整。
```

## Quality Checklist

Before leaving clarification mode, verify:

- The main task is stated in one sentence.
- Scope boundaries are clear enough.
- Output format is clear.
- Any high-impact exclusions are named.
- The user either approved the plan or accepted the assistant's default.
- Remaining assumptions are visible.
