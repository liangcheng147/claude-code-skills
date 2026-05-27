# Audit Checklist

Use before Stage 6 (Audit and Fix Until Clean) or after any stage failure. Perform checks by direct file inspection using available file reading and search tools. Record findings in `MIGRATION_REPORT.md`.

## Static Structure

Paths:
- graphics paths resolve to existing files
- bibliography paths resolve
- `\input`/`\include` paths resolve
- `\addbibresource` paths resolve
- supplement links resolve when target-supported
- no path points back to source directory

References:
- all citation keys exist in `.bib` files
- no duplicate labels
- all refs resolve to existing labels
- begin/end environment pairing is correct

Template conformance:
- target requirements are recorded as required, optional/example-only, prohibited/unsupported, or unclear
- user-approved migration plan is recorded before migration execution
- required target rules are implemented, and optional/example-only patterns are not treated as mandatory without evidence
- target document class and template commands are used
- no residual source-template core commands
- no source syntax remains where the target template provides different syntax
- no invalid or absolute source paths
- declarations are present only when required or allowed by target evidence
- supplements/appendices are present only when required or allowed by target evidence
- target-supported administrative declarations follow required or selected target examples and order
- scientific appendices/supplements use target-supported structure without rewriting scientific content
- unsupported source-only elements are removed, recorded, or marked TODO when substantive content needs user decision

Floats:
- environment counts match source unless target rules require supported relocation/removal
- placement options follow target template
- caption and label placement follow target template
- table rules (booktabs/hline) follow target template
- ordinary vs wide table environment correct
- wide-table wrappers present only when target-supported
- multipanel figures use correct target subfloat syntax
- panel caption format correct
- table notes use target format
- appendix float labels use correct target prefix

## Content Consistency

Compare source and migrated: abstract, body sentences, scientific appendix/supplement sentences, equations, table data, captions, citation keys, labels/refs, figure file mappings, and factual content in target-supported declarations and administrative sections.

Body/scientific content check: abstract, body sentences, scientific appendix/supplement sentences, equations, table values, captions, citation keys, labels/refs, figure content, and scientific claims must keep the source wording and meaning. Only target-required formatting, commands, environments, wrappers, placement, paths, and structural conversion may differ.

Administrative check: declarations, funding, acknowledgements, author contributions, data availability, ethics, and conflicts of interest may use target-template wording, labels, order, and required or selected examples, but their factual meaning must match the source or user-provided facts.

Allowed differences: target-template commands, target syntax, float syntax, float placement, asset paths, metadata placeholders, target-required declarations, target-supported administrative declaration conversion and wording, target-supported scientific supplement structure conversion without content rewriting, removed unsupported declarations/supplements, section-command normalization, removed source-template artifacts (title pages, TOC, forced page breaks), and removed source-only elements not required or allowed by target evidence.

Non-allowed scientific-content differences must be restored unless user explicitly approved the edit.

## Compile

Detect available tools. Prefer target-template-recommended compile sequence. Check: LaTeX errors, missing figures, undefined citations/refs, bibliography generation, important layout warnings. If unavailable, record why - do not present static checks as compile checks.

## Audit-Fix Loop

For every issue found in static structure, content consistency, or compile checks:
- fix evidence-resolvable issues and rerun the affected checks
- record missing facts as TODOs
- pause for user decision when evidence does not determine the correct fix
- do not finalize while any evidence-resolvable issue remains open

## Final Delivery

Confirm: directory self-contained, main `.tex` present, bibliography present, template dependencies present, figures/assets present, supplements present only if target-supported, all paths project-relative, target requirements classified, user approval recorded, required rules implemented, no source syntax remains where target syntax exists, body/scientific content and scientific appendices/supplements only format-converted, administrative declaration wording follows required or selected target examples without changing facts, audit-fix loop has no evidence-resolvable issues remaining, `MIGRATION_REPORT.md` complete, all audit results and TODOs recorded.
