# Full Workflow

Use this reference when performing an actual migration or recovering from a failed stage.

## Stage 1: Establish Evidence

Identify source `.tex`, bibliography, figures, tables, declarations, appendices, supplements, and assets. Identify target template files, class/style, documentation, examples, official author instructions, submission guidelines, publisher policies, and user constraints. Extract target requirements for front matter, body, floats, equations, citations, references, declarations, acknowledgements, appendices, supplements, and any required or prohibited manuscript elements. Extract source structure: title, authors, abstract, keywords, sections, floats, equations, citations, labels, custom commands, packages, declarations, supplements, and asset paths.

Use this evidence priority when requirements conflict: official author instructions/submission guidelines, official template documentation, official template examples, publisher policies, explicit user constraints, then source-manuscript style only when target evidence permits it.

Classify each target rule before planning:

- Required: explicitly mandatory commands, sections, wording, order, file structure, float syntax, bibliography style, declarations, or submission elements.
- Optional/example-only: example wording, example structures, recommended but non-mandatory elements, or alternatives allowed by the template. Use them as style guidance unless you intentionally select one as the target-supported pattern.
- Prohibited/unsupported: elements the target forbids or does not support, including source-only template habits.
- Unclear: requirements whose status cannot be proven from evidence; these become TODOs or user questions.

Record all requirements with sources and their classification. Distinguish official instructions, template requirements, template examples, publisher policies, user constraints, and source-only habits. Mark source-only items that the target does not require or allow.

**Self-check**: every planned rule has a source and a classification, no source-free requirements introduced, and examples are not treated as mandatory unless the evidence says they are. If files are missing, stop and ask. If requirements conflict, follow the evidence priority above unless the user decides otherwise.

## Stage 2: Plan Migration and Compare Formats

Define: output directory, files to copy, template dependency handling, front matter/body/float/bibliography/declaration/supplement migration, unsupported source-only element handling, source-syntax to target-syntax mapping, float-format mapping (ordinary figures, multipanel figures, ordinary tables, wide tables, table notes, labels, placement), TODO placeholders, and validation steps.

Before any migration edits, compare target-template format and source-manuscript format:

- Target template format: document class, required packages/classes, front matter, abstract/keywords, section commands, body organization, equations, figures, tables, captions, labels, references, bibliography, declarations, appendices, supplements, file layout, compile sequence, and prohibited or unsupported elements.
- Source manuscript format: current class/packages, front matter, abstract/keywords, sections, equations, figures, tables, captions, labels, references, bibliography, declarations, appendices, supplements, custom commands, formatting constructs, asset paths, and source-only artifacts.
- Migration mapping: for each source structure or syntax, state the target structure or syntax, whether the change is required, optional/example-only, prohibited/unsupported, or unclear, and whether the change is format-only, administrative wording, removal, or TODO.

Plan two content tracks:

- Body/scientific content track: abstract, body text, equations, table data, captions, citation keys, labels/refs, figure content, and scientific claims must keep their source wording and meaning. Only formatting, LaTeX commands, environments, wrappers, placement, paths, and target-required structure may change.
- Administrative track: declarations, funding, acknowledgements, author contributions, data availability, ethics, and conflicts of interest should have their source facts extracted and then expressed with the target template's wording, labels, order, and required or selected example patterns when the target supports them.
- Scientific appendix/supplement track: appendices and supplementary files that contain methods, results, equations, tables, captions, figure descriptions, data, or scientific claims belong to the body/scientific content track. Preserve their wording and meaning; only convert formatting, LaTeX commands, environments, wrappers, placement, paths, and target-supported structure.

For every source-only section, metadata block, declaration, supplement, package, command, environment, float wrapper, or formatting construct, classify the target disposition as required, optional/example-only, prohibited/unsupported, or unclear. Do not keep items classified as prohibited/unsupported. If the target provides a required structure or you select an allowed example pattern, plan to transform source content into that structure. If the item contains substantive manuscript content and the target disposition is unclear, plan to ask the user or leave a TODO instead of silently retaining it.

Prepare Chinese migration recommendations for the user. Include: target-template requirements, source-manuscript format summary, source-to-target conversion table, unsupported source elements, required user decisions, missing facts/TODOs, expected compile path, risk points, and the exact next steps after approval.

**Self-check**: every action maps to Stage 1 evidence and its required, optional/example-only, prohibited/unsupported, or unclear classification. Scientific/body content, including scientific appendix/supplement content, is preserved only inside target-allowed structures and is not rewritten. Administrative content preserves source facts while adopting target wording and required or selected example patterns. Source syntax is mapped to target syntax where target evidence provides one. No fact guessing. Float and supplement plans follow target template and official author instructions exactly. The plan clearly separates target format, source format, and migration recommendations.

## Stage 3: Present Plan and Wait for Confirmation

Present the Chinese migration plan before creating the migrated project or editing LaTeX files. The plan must be concrete enough for the user to approve or correct:

- Target template format and classified requirements.
- Existing source format and source-only constructs.
- Proposed source-to-target conversions.
- Which content will be preserved verbatim or format-only.
- Which administrative content will be rewritten to target wording.
- Unsupported elements to remove or mark TODO.
- Missing facts or unresolved decisions.
- Audit and compile strategy after migration.

Stop after presenting the plan unless the user has already explicitly approved this exact plan in the current conversation. If the user requests changes, revise the plan and present it again. Only proceed to Stage 4 after approval.

## Stage 4: Create Migrated Project Directory

Create a new directory. Copy target template dependencies, bibliography, figures, supplements, and referenced assets that remain target-allowed. Normalize unsafe paths only when needed. Record file/path mappings.

**Self-check**: source project not overwritten. All referenced resources present. No figure content modified. No source-only template dependencies copied unless target evidence or user constraints require them.

## Stage 5: Execute Migration

Apply target document class and structure. Convert front matter. Insert source scientific body content and scientific appendix/supplement content into target-allowed locations without paraphrasing or changing claims. Replace source syntax with target syntax whenever the target template or author instructions provide a different required command, environment, order, wrapper, or selected example pattern. Remove incompatible source-template commands, source-only packages, source-only declarations, unsupported metadata blocks, unsupported supplement structures, and source formatting constructs not required or allowed by target evidence. Remove target-template sample content. Convert float environments per target requirements (see `references/float-rules.md`). Update asset paths. Integrate bibliography. Add declaration or supplement scaffolding only when required or allowed by target evidence. For target-supported administrative items, rewrite source facts into the target template's wording, labels, and order while keeping the meaning equivalent. Insert TODOs for missing facts. Update the Chinese `MIGRATION_REPORT.md`.

**Self-check**: target template commands used, source-template commands removed, source syntax not mixed with target syntax, unsupported source-only elements not carried over, supported declarations and administrative items transformed into target format and wording, floats preserved in content but converted to target syntax, body/appendix/supplement scientific wording, captions, labels, table data, citation keys, and figures unchanged, asset paths valid, missing facts are TODOs. If a conversion would alter scientific content, ask the user.

## Stage 6: Audit and Fix Until Clean

Three sub-steps. See `references/audit-checklist.md` for the full checklist.

### 6a: Static Structure

Check: graphics/bib/input/include/addbibresource/supplement paths, citation keys, duplicate labels, missing refs, begin/end pairing, residual incompatible commands, declaration status, supplement status, target syntax conformance, float syntax conformance, and unsupported source-only elements.

### 6b: Content Consistency

Compare source and migrated: abstract, body text, scientific appendix/supplement text, equations, table data, captions, citation keys, labels/refs, figure mappings, and factual content in target-supported declarations and administrative sections. Allowed differences: target-template commands, target-required section placement, target syntax, float syntax, asset paths, metadata placeholders, target-required declarations, declaration removal when unsupported, supplement structure conversion when target-supported, administrative wording changes that preserve source meaning and follow required or selected target patterns, section-command normalization, removed source-template artifacts, and removed source-only elements not required or allowed by target evidence. Non-allowed scientific-content differences must be restored unless user approved.

### 6c: Compile

Detect available LaTeX tools. Run target-template-recommended compile sequence. Check errors, missing figures, undefined citations/refs, bibliography generation, and important layout warnings. If unavailable, record why.

For every audit issue, decide whether it is evidence-resolvable, requires missing facts, or requires a user decision:

- Evidence-resolvable: fix it, update `MIGRATION_REPORT.md`, and rerun the affected static/content/compile checks.
- Missing fact: record TODO and move to Stage 7.
- User decision: pause and ask with the evidence, options, and consequence.

Repeat Stage 6 until all evidence-resolvable issues are fixed and the rerun audit is clean. Do not stop after a failed audit unless the remaining issue needs user input or missing facts.

**Self-check**: all referenced files exist, labels not duplicated, refs resolve, body sentences unchanged, compile attempted or reason recorded, target syntax used, and no unsupported source-only elements remain. If structural failure appears, return to Stage 5, fix, and rerun Stage 6.

## Stage 7: Collect Missing Information and Re-Audit

Ask the user only for missing facts or unresolved target-rule decisions from confirmed sources. For each question: what is needed, why, source, where it goes, and what happens if unavailable. Apply only user-provided facts. Leave unanswered items as TODOs.

After applying user input, recheck edited fields, static structure, content consistency, target conformance, compile status when affected, and the Chinese report. Update `MIGRATION_REPORT.md`. If new evidence-resolvable issues appear, return to Stage 6 and rerun the audit-fix loop.

**Self-check**: every question has a source, no facts guessed, user-provided facts inserted accurately, affected checks rerun.

## Stage 8: Final Delivery

Confirm: migrated directory is self-contained, main `.tex` present, bibliography and target template dependencies present, all referenced assets present, all paths project-relative (none point back to source), target requirements are classified, user approved the migration plan, no unsupported source-only elements remain, body/scientific content and scientific appendix/supplement content were only format-converted, all target-supported administrative declarations use target syntax and meaning-preserving target wording, Chinese `MIGRATION_REPORT.md` complete, audits and TODOs recorded, and no evidence-resolvable audit issues remain.

Report to the user in Chinese unless they request otherwise: migrated directory path, main `.tex` path, `MIGRATION_REPORT.md` path, user confirmation status, checks passed, compile status, target requirement classification, syntax conversions, body/scientific content and scientific appendix/supplement format-only handling, removed unsupported elements, transformed administrative declarations/items, and remaining TODOs.
