# Skill Registry

Maps task patterns to skills. Priority numbers resolve conflicts (lower = higher priority).

## Tier 1 — Pre-execution Gates

These skills should run BEFORE other skills when they match, because they refine the task itself.

| Skill | When to use | When NOT to use | Priority |
|-------|-------------|-----------------|----------|
| brainstorming | Creating new features/components/behavior. Needs design decisions. | Bug fixes, simple config, already has a clear spec | 1 |
| task-clarifier | Vague/ambiguous requests. "帮我整理", "分析一下", "做一个方案". Scope unclear. | Clear single-step commands. User said "不要问". | 2 |

## Tier 2 — Domain Skills

| Skill | When to use | When NOT to use | Priority |
|-------|-------------|-----------------|----------|
| frontend-design | Web UI: pages, dashboards, React components, HTML/CSS, UI beautification | Backend-only, non-frontend | 3 |
| 前端美学设计技能 | Same as frontend-design, when user writes Chinese and emphasizes aesthetics | Same | 3 |
| pptx | Any .pptx task — create, read, edit, combine presentations | Non-presentation formats | 3 |
| latex-template-migrator | LaTeX → journal/conference template migration | General LaTeX editing | 3 |
| model-migration | PyTorch architecture migration, module replacement, structure fusion | Non-PyTorch, simple training | 3 |
| claude-api | Claude API / Anthropic SDK work, prompt caching | OpenAI/other SDKs | 3 |

## Tier 3 — Code Quality

| Skill | When to use | When NOT to use | Priority |
|-------|-------------|-----------------|----------|
| code-commenter | Add Chinese comments, explain code for beginners | Comments already exist | 4 |
| karpathy-guidelines | Writing/reviewing/refactoring code | Non-code tasks | 4 |
| code-review | Review diff for correctness bugs | No diff available | 4 |
| security-review | Security review of branch changes | Non-security | 4 |
| verify | Verify code changes work by running app | No recent changes | 4 |

## Tier 4 — Configuration & Meta

| Skill | When to use | When NOT to use | Priority |
|-------|-------------|-----------------|----------|
| update-config | settings.json: hooks, permissions, env vars | Simple /config changes | 4 |
| keybindings-help | Keyboard shortcuts, keybindings.json | Other config | 4 |
| find-skills | "How do I do X", finding new skills | Task already has a matching skill | 4 |
| skill-creator | Creating/modifying skills, running evals | Using existing skills | 4 |
| fewer-permission-prompts | Reducing permission prompts | Other config | 4 |

## Tier 5 — Execution & Utility

| Skill | When to use | When NOT to use | Priority |
|-------|-------------|-----------------|----------|
| run | Launch app, take screenshots, confirm changes work | Tests only | 4 |
| init | Initialize CLAUDE.md | Already exists | 4 |
| review | Review a pull request | No PR context | 4 |
| loop | Recurring tasks: "every 5 minutes", polling | One-off tasks | 4 |

## Conflict Resolution

When multiple skills match:

1. Lower priority number wins
2. Same priority → more specific trigger wins
3. Same tier + specificity → language match (Chinese user → Chinese skill, English → English)

**Special: dispatcher vs brainstorming HARD-GATE**
brainstorming has its own HARD-GATE claiming to be "the first step for creative work." When the dispatcher routes to brainstorming, brainstorming's HARD-GATE takes precedence — let it run its full process (clarify → design → approve) before proceeding to the next step in the execution plan. The dispatcher defers to domain skills' own gating mechanisms.

## Common Multi-Skill Patterns

These templates cover frequent scenarios. Use them as starting points and adapt.

### Clarify → Design → Implement

For vague creative requests: "帮我做一个漂亮的活动策划 PPT"
1. task-clarifier → clarify scope, audience, style
2. brainstorming → design structure and approach
3. [domain skill] → execute

### Understand → Implement → Verify

For code changes needing correctness: "重构这个模块并确保正确"
1. karpathy-guidelines → analyze code, plan changes
2. [domain skill] → implement
3. verify → confirm it works

### Clarify → Design → Implement → Review

For high-stakes deliverables: "帮我实现一个用户认证系统"
1. task-clarifier → clarify requirements
2. brainstorming → design architecture
3. [domain skill] → implement
4. code-review → review quality

### Research → Implement → Comment

For learning-oriented tasks: "帮我实现一个 Transformer 并添加详细注释"
1. task-clarifier → clarify scope
2. [domain skill] → implement
3. code-commenter → add explanations
