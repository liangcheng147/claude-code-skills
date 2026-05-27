---
name: latex-template-migrator
description: Use this skill when the user needs to migrate, convert, reformat, or adapt an existing LaTeX manuscript into a journal, conference, or publisher template. It first plans the migration by identifying target-template format requirements, source-manuscript formatting, requirement classifications, and migration recommendations, then waits for user confirmation before changing files. After approval, it preserves scientific manuscript content, including scientific appendices and supplements, while converting only structure, formatting, syntax, floats, citations, and bibliography; rewrites administrative declarations, funding, acknowledgements, and contributions to target-template wording without changing meaning; audits and fixes until no issues remain; then produces a Chinese migration report.
---

# LaTeX Template Migrator

Migrate a source LaTeX manuscript into a target journal/conference/publisher template as a self-contained LaTeX project.

## Non-Negotiables

- **Evidence only**: derive all requirements from target template files, official author instructions, submission guidelines, template documentation, examples, publisher policies, or user input. Do not invent requirements.
- **Planning gate before migration**: on the first pass of a migration, inspect the target template and source manuscript, present a Chinese migration plan with target format, source format, requirement classifications, source-to-target mapping, risks, TODOs, and migration recommendations, then stop for user confirmation. Do not create the migrated project directory or modify LaTeX files until the user confirms the plan.
- **Classify target requirements first**: before migration, read and classify target rules as required, optional/example-only, prohibited/unsupported, or unclear. Required rules must be implemented; optional/example-only patterns guide style only when compatible; prohibited/unsupported elements must not be carried over; unclear requirements become TODOs or user questions.
- **Target rules override source habits**: the migrated project must follow the target journal's official template and author instructions, not the source manuscript's formatting, package choices, syntax, float patterns, declaration structure, supplement structure, or front/back matter conventions.
- **Template syntax wins**: when the source manuscript uses a LaTeX syntax, environment, command, package, or wrapper that differs from the target template's required syntax or the selected target-supported example pattern, remove the source syntax and convert the content to the target syntax. Do not keep both syntaxes or preserve source-only constructs for convenience.
- **Body/scientific content is format-only**: preserve source abstract, body text, equations, table data, captions, citation keys, labels, figures, and scientific claims verbatim in meaning and wording unless the user explicitly authorizes edits. For this content, only convert formatting, LaTeX structure, commands, environments, placement, and target-required wrappers.
- **Administrative content may be template-worded**: for declarations, funding, acknowledgements, author contributions, data availability, ethics, and conflicts of interest, extract the factual meaning from the source and rewrite it only as needed to match the target template's wording, order, labels, and required or selected example patterns while preserving meaning.
- **Scientific appendices/supplements stay format-only**: appendices and supplementary files often contain methods, results, equations, tables, captions, and claims. Treat those scientific parts as body/scientific content: preserve wording and meaning, and only convert formatting, structure, placement, paths, and target-supported wrappers.
- **No unsupported carryover**: do not retain source-only template artifacts, metadata blocks, declarations, supplements, sections, packages, commands, environments, or formatting constructs that are not required or allowed by the target template, official author instructions, or user constraints.
- **Target-supported supplemental structures**: if the target template or author instructions provide a required structure or selected example pattern, transform administrative declarations into that wording/structure while preserving facts, and transform scientific appendices/supplements only into that structure while preserving their scientific wording and meaning.
- **Unsupported substantive content**: if an unsupported source-only item contains substantive manuscript content and the target disposition is unclear, ask the user or record a TODO instead of silently keeping, deleting, or relocating it.
- **TODO for unknowns**: use TODO placeholders for missing factual information. Do not guess.
- **Audit-fix loop**: after migration, run static structure, content consistency, and compile audits. Fix every issue that can be resolved from evidence and rerun the affected audits. Do not finalize while evidence-resolvable issues remain; if the remaining issue requires user decision or missing facts, pause for input or record an explicit TODO before final delivery.
- **Chinese report**: write `MIGRATION_REPORT.md` in Chinese unless the user explicitly asks for another language.

## Compatibility and Composition

Use available file reading, search, copy, and LaTeX compile tools in the current environment. Do not assume this skill is the only active capability; compose with other skills when the task also involves writing, presentations, data processing, or repository automation.

## Quality Evaluation

When evaluating this skill, treat targets as benchmarks rather than exact thresholds: test 10-20 realistic migration prompts for trigger accuracy, compare tool calls and token use against a no-skill baseline when possible, and expect a complete workflow to avoid failed API/tool calls. For qualitative checks, repeat 3-5 representative migrations or dry runs and record whether the workflow needs extra user prompting, manual correction, or differs across fresh sessions.

## Progressive Loading

Load references only when the workflow reaches that stage:

- `references/full-workflow.md` - when doing an actual migration or recovering from a failed stage.
- `references/float-rules.md` - before converting figures, tables, schemes, listings, declarations, appendices, or supplements.
- `references/audit-checklist.md` - before running audits or final delivery.
- `references/migration-report-template.md` - when creating `MIGRATION_REPORT.md`.

## Workflow

8 stages: (1) establish evidence, (2) plan migration and compare target/source formats, (3) present migration recommendations and wait for user confirmation, (4) create migrated project directory, (5) execute migration, (6) audit and fix until clean, (7) collect missing information and re-audit, (8) final delivery. See `references/full-workflow.md` for details.

Each stage: do the work, self-check, and record in the Chinese `MIGRATION_REPORT.md` once the migrated project exists. Before user confirmation, report the plan and migration recommendations in Chinese in chat, or in a separate `MIGRATION_PLAN.md` only if useful or requested. If a stage fails, fix and rerun before moving on. If a fix needs user decision, pause and ask.

## Float and Supplement Handling

Follow official author instructions exactly. Follow template examples exactly only when classified as required or when using them as the selected target-supported pattern; otherwise treat examples as style guidance. Preserve scientific content while converting only syntax, placement, ordering, and wrappers. For administrative sections, preserve source facts while adopting target-template wording, labels, order, and required or selected example patterns. Do not keep source constructs that the target template/instructions do not support. See `references/float-rules.md`.

## Reporting

Create one Chinese `MIGRATION_REPORT.md` in the migrated project directory using `references/migration-report-template.md` as the structure. Record evidence, target requirement classification, user plan confirmation, body/scientific content format-only conversions, syntax conversions, removed unsupported source-only elements, transformed administrative declarations/items, audit-fix results, compile status, and remaining TODOs.

## Static Review

Validate by direct file inspection using available file reading and search tools. See `references/audit-checklist.md` for the full checklist. Record findings in `MIGRATION_REPORT.md`.

## Deliverable

The final deliverable is the full migrated LaTeX project directory, including main `.tex`, bibliography, target template dependencies, target-allowed assets, and Chinese `MIGRATION_REPORT.md`.
