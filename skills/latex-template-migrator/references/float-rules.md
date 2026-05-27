# Float Rules

Use this reference before converting figures, tables, schemes, listings, multipanel figures, wide tables, table notes, landscape floats, appendix floats, declarations, appendices, or supplementary information.

## Sources and Priority

Extract float and supplemental-structure rules only from: official author/submission instructions, target template documentation, target template examples, publisher policies, or user constraints. Reference papers may be used as style examples only when official target evidence is silent and must not override official instructions or template examples. When the target template defines a required pattern, or when an allowed example is selected as the target-supported pattern, follow it exactly - do not rely on generic LaTeX habits or source-manuscript style.

Classify float and supplemental rules before conversion: required, optional/example-only, prohibited/unsupported, or unclear. Implement required rules; use optional/example-only patterns as style guidance only when compatible or as the selected target-supported pattern when the target allows alternatives; remove or avoid prohibited/unsupported constructs; record unclear cases as TODOs or user questions.

If source syntax, wrappers, placement habits, package choices, table rules, subfigure mechanisms, notes, appendix numbering, declarations, or supplement structures are not required or allowed by target evidence, do not retain them by default. Convert them to the target-supported pattern, record the change, or ask the user when substantive meaning would be affected.

## Conversion Boundary

**Preserve**: figure filenames, figure content, table values, captions, citation keys, labels/refs (unless template requires mechanical label update), panel meanings and order, scientific claims, and factual content in target-supported declarations/supplements.

**Allowed changes**: float environment syntax, placement options, caption/label/note location, asset paths, wrapper macros, section-command normalization, target-required width/layout commands, conversion of administrative declaration syntax to target syntax, target-template wording for administrative declaration content that preserves source meaning, target-supported structure conversion for scientific appendices/supplements without rewriting their scientific content, and removal of unsupported source-only wrappers.

**Ask before changing**: caption wording, table values, figure content, citation keys, author-provided interpretation, any data or experimental claim, declaration facts, supplement facts, or any unsupported element whose removal would change scientific meaning.

For declarations, funding, acknowledgements, author contributions, data availability, ethics, and conflicts of interest, extract the source facts first, then express them with the target template's labels, order, and required or selected example wording. Do not invent missing facts or change the meaning to fit an example.

For appendices and supplementary information that contain methods, results, equations, tables, captions, figure descriptions, data, or scientific claims, treat the content as scientific/body content. Convert only the target-supported structure, wrappers, placement, links, and paths; do not rewrite scientific wording or claims.

## Required Mapping

Before editing floats, declarations, appendices, or supplements, record in the Chinese `MIGRATION_REPORT.md` how each source pattern maps to the target pattern:

| Category | Record |
|---|---|
| Ordinary figures | environment name, placement, caption/label position |
| Multipanel figures | subfloat syntax, panel caption format |
| Ordinary tables | environment, column types, booktabs/tabular rules |
| Wide tables | wrapper environment, width macro |
| Table notes | note command and position |
| Figure/table labels | label position (inside caption or standalone) |
| Float placement | required placement options |
| Appendix floats | numbering scheme and label prefix |
| Administrative declarations | required/allowed declaration type, command/section format, wording pattern, order |
| Scientific supplementary information | target location, command/section format, wrappers, linked files, unchanged scientific content |
| Removed source-only constructs | source construct, target evidence, action taken |

Record every intentional exception with source evidence or user approval. Avoid source-only or generic constructs when the target template does not permit them (e.g., `figure*`, `resizebox`, `minipage`, deprecated `subfigure`, `hline`, vertical rules, ad hoc declaration sections, or custom supplement wrappers).
