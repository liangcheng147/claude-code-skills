---
name: skill-dispatcher
description: "Understand user intent and route tasks to the right skills, coordinating multiple skills when a request is complex. Use this skill when a user request could benefit from a specialized skill — especially multi-step tasks, vague requests, or tasks combining design + implementation + review. It analyzes the goal, breaks it into sub-tasks, maps each to the best skill, and presents an execution plan. Works as a coordinator layer above other skills: it decides WHO does WHAT, then lets each skill handle the HOW."
---

# Skill Dispatcher

Understand what the user wants, figure out which skills should handle it, and coordinate them.

The value of this skill is preventing two failure modes:
1. **Missed skills**: A task that would benefit from a skill gets handled generically, producing lower quality results.
2. **Wrong skill order**: Multiple skills are needed but invoked in the wrong sequence (e.g., implementing before clarifying requirements).

This skill does NOT execute tasks. It analyzes, plans, and delegates.

## When This Skill Runs

This skill triggers on requests that could benefit from specialized skills. It does NOT need to run on every single request — simple, direct tasks (like "read this file" or "what is 2+2") don't need routing.

**Good triggers**: multi-step tasks, vague requests, tasks combining multiple concerns, requests matching domain-specific skills, "帮我做一个...", creative/building work.

**Skip**: trivial questions, direct file reads, explicit /slash-command invocations, tasks where the right skill is obvious and already invoked.

## Workflow

### Step 0: Skill Freshness Check (First Invocation Only)

On the FIRST request in a conversation, check if skills have changed since last session:

```
自上次对话以来，你是否新增、删除或更新了 skill？
A. 没有，使用当前注册表（推荐）
B. 有变化，请先扫描更新
```

- **A** → Use the static registry below, proceed to Step 1
- **B** → Run dynamic scan (see "Dynamic Scan Flow"), then proceed to Step 1

On SUBSEQUENT requests in the same conversation, skip this step and go directly to Step 1.

### Step 1: Analyze Intent

Understand what the user ultimately wants. Identify:
- **Goal**: the end result they care about
- **Task type**: coding, design, document, research, config, review, creative
- **Key entities**: files, formats, technologies mentioned
- **Complexity**: single-step or multi-step?

### Step 2: Choose Mode

**Single-skill** — the task clearly maps to one skill with no dependencies:
- Match against registry → inform → invoke
- Note: If the matched skill is a Tier 1 gate (brainstorming, task-clarifier), it acts as a pre-step. After it completes, re-evaluate whether additional skills are needed for the actual execution.

**Multi-skill** — the task has multiple phases or combines concerns:
- Proceed to Step 3

### Step 3: Multi-Skill Decomposition

#### 3.1 Break into sub-tasks

Each sub-task should have one clear purpose and produce one concrete output.

#### 3.2 Map to skills

For each sub-task, find the best skill from the registry.

#### 3.3 Determine order

Which sub-tasks must happen before others? Typically:
- Clarification before design
- Design before implementation
- Implementation before review

#### 3.4 Present the plan

```
执行计划（共 N 步）：

步骤 1: [what to do]
  → 使用: [skill-name]
  → 产出: [concrete output]

步骤 2: [what to do]
  → 使用: [skill-name]
  → 产出: [concrete output]
  → 前置: 需要步骤 1 的产出

是否按此计划执行？
```

The user can approve, skip steps, reorder, or substitute skills.

#### 3.5 Execute

Execute each step by invoking the assigned skill. Each step runs independently — pass context from previous steps by including relevant information in the skill invocation prompt, not through file-based data passing.

After all steps complete:

```
执行完成：
✅ 步骤 1: [result summary]
✅ 步骤 2: [result summary]
```

## Skill Registry

The static registry is maintained in `references/skill-registry.md`. It maps task patterns to skills with priority numbers for conflict resolution.

Load the registry at the start of Step 2 (Choose Mode) when matching tasks to skills.

## Dynamic Scan Flow

When the user indicates skills have changed:

### 1. Scan directories

Read SKILL.md files from:
- `~/.claude/skills/` (symlinks)
- `~/.cc-switch/skills/` (actual files)
- `~/.agents/skills/` (actual files)

Extract `name` and `description` from each.

### 2. Add built-in skills

These are always available but not in skill directories:
update-config, keybindings-help, verify, code-review, fewer-permission-prompts, loop, claude-api, run, init, review, security-review

### 3. Rebuild registry

For each skill: assign tier, derive trigger conditions, set priority.

### 4. Report changes

```
技能注册表已更新：
- 新增：[list]
- 移除：[list]
- 共计：[total] 个 skill
```

Then continue to Step 1.

## Maintenance

The static registry is the default. Update it when:
- Dynamic scan reveals changes
- Skills are installed/removed via `npx skills`

The dynamic scan is the primary up-to-date mechanism. The static registry avoids scanning on every request.
