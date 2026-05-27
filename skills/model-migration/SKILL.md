---
name: model-migration
description: >
  Deep learning model architecture migration and fusion skill. Use this when the user wants to
  migrate modules, replace components, fuse architectures, or transfer design patterns between
  PyTorch models. Trigger on: model migration, model fusion, architecture migration, backbone
  replacement, encoder migration, module transfer, weight migration, transfer learning between
  models, replacing branches in dual-branch networks, fusing model outputs, migrating attention
  mechanisms, replacing encoders/decoders. Always use this skill when the user mentions combining,
  replacing, migrating, or fusing any part of one model with another, even if they don't explicitly
  say "migration".
---

# Model Migration & Fusion

A general-purpose skill for migrating modules or design ideas between PyTorch deep learning models.

## Scope

- PyTorch models only. If the source/target uses TensorFlow, JAX, or other frameworks, inform the user and suggest manual conversion first.
- Covers: module replacement, branch substitution, structure fusion, adapter insertion, weight transfer.
- Does NOT cover: training pipeline migration, data pipeline changes, deployment optimization.

## Workflow

Follow these steps in order. Each step builds on the previous one.

### Step 1: Quick Scan

Read both the source model and target model Python files. Extract:

1. **Class hierarchy** — inheritance, submodule composition
2. **Forward data flow** — trace `forward()` method, note each layer's input/output shapes
3. **Key hyperparameters** — embed_dim, num_heads, patch_size, kernel_size, etc.
4. **Weight file (optional)** — if user provides a `.pth`, `.safetensors`, or HuggingFace model path, load state_dict keys and shapes to validate code analysis

Present the result as a tree-structured comparison of both models. For large models with many submodules, show a summary first (top-level modules + parameter counts), then drill down into the modules the user is interested in. Highlight shape annotations at each layer boundary.

### Step 2: Smart Questions

Only ask what cannot be inferred from code. Present analysis results alongside each question.

**Auto-inferred (do NOT ask)**:
- Model layers and structure
- Input/output shapes per layer
- Parameter count
- Dimension compatibility between adjacent layers
- Gradient flow status

**Must ask (one question per message, use multiple choice when possible)**:

If the user is unsure what to migrate, proactively recommend the most compatible module combinations based on structural similarity (matching input/output shapes, similar architectural role, compatible data flow). Present 2-3 recommended migration pairs with reasoning.

1. Migration target identification:
   - Present the structure comparison
   - Ask: "Which part of the source model do you want to migrate?" (highlight candidates)
   - Ask: "Which part of the target model should be replaced?" (highlight compatible modules)

2. Migration strategy:
   - "Direct replacement — swap the module entirely"
   - "Adapter insertion — add the source module alongside existing structure"
   - "Output fusion — combine outputs of both modules (concat/add/cross-attention)"
   - "Design pattern transfer — transfer the architectural idea, not the exact module"

3. Weights and training:
   - "Preserve pretrained weights from source model? (Y/N)"
   - "Freeze migrated parameters? (Y/N, and for how many epochs)"
   - "Any changes to loss function or learning rate needed?"

### Step 3: AI Review

Proactively audit the migration plan. This is the key differentiator. Use your deep learning knowledge to identify issues the user might miss.

#### Dimension Compatibility Check
- Verify tensor shapes align between source output and target input
- Check channel count, spatial dimensions, sequence length, batch dimension
- If incompatible, propose specific adapter layers:
  - Channel mismatch → 1x1 Conv or Linear projection
  - Spatial mismatch → interpolation or strided convolution
  - Sequence length mismatch → positional embedding interpolation or truncation
- Flag potential information bottlenecks (aggressive dimension reduction)

#### Gradient Flow Check
- Trace the computational graph through the replacement
- Identify gradient breakpoints: `.detach()`, `torch.no_grad()`, in-place operations on leaf tensors
- Check for gradient vanishing risks (too many sequential layers without residual connections)
- Check for gradient exploding risks (large fan-in without normalization)
- Suggest fixes: skip connections, gradient clipping, normalization layers

#### Architecture Reasonability Review
- Reference academic precedents for this type of migration
- Identify capacity mismatches (e.g., huge encoder with tiny decoder)
- Flag training stability risks:
  - BatchNorm vs LayerNorm mismatch
  - Different activation functions
  - Learning rate sensitivity differences
- Suggest training strategies: warmup, progressive unfreezing, discriminative learning rates

#### Output Format
```
## Migration Review

### Warnings
⚠️  Source module outputs dim=1024, target expects dim=768
    Suggestion: Add Linear(1024, 768) adapter layer

⚠️  Source uses BatchNorm, target uses LayerNorm
    Suggestion: Unify to LayerNorm for transformer-based models

### Gradient Flow
✅  Gradients can flow normally through the replacement
⚠️  Detached tensor detected at layer X - gradient won't propagate

### Suggestions
💡  Consider freezing the migrated encoder for first N epochs
💡  Learning rate for migrated layers should be 0.1x of new layers
```

### Step 4: Plan Confirmation

Present a complete migration summary:

- Files to modify (with specific class/method changes)
- New adapter layers needed
- Config file changes
- Expected parameter count change
- Training strategy recommendations

**User must explicitly confirm** before proceeding to code generation.

### Step 5: Code Generation

#### File Strategy
- Can modify the target model file (add, remove, replace classes and methods)
- Source model file is read-only
- Before modifying the target file, show a diff preview of what will change
- Recommend user commit current code before migration

#### Code Quality Standards
- Type hints for all function signatures
- Clear module boundaries with single responsibility
- Reasonable default values
- Docstrings for public classes and complex methods
- Follow general Python/PyTorch best practices, NOT the project's existing style

#### Deliverables

1. **Modified target model code** — the migrated model, ready to run
2. **Verification script** — run this to validate the migration:
   - Forward pass with dummy input → check output shapes
   - Backward pass → verify gradients reach all trainable parameters
   - Parameter count summary
3. **Migration report** — markdown document listing:
   - Which layers were migrated
   - Which layers were skipped and why
   - Dimension changes at each boundary
   - Adapter layers added
   - Training recommendations

## Reference Files

Read these as needed:
- `references/migration-patterns.md` — Common migration patterns with code examples
- `references/adapter-layers.md` — Catalog of adapter layers for dimension/structure mismatches

## Verification Script Template

Use `scripts/verify_migration.py` as a template. The template contains TODO comments indicating where to add your model imports and tests — these are intentional, not oversights. Customize the script for the specific migration by filling in the TODO sections.

## Key Principles

- Ask one question at a time, never stack multiple questions
- Show, don't tell — present analysis results alongside questions
- Be opinionated — give recommendations with reasoning, not just options
- Safety first — always show diff preview before modifying files
- Test everything — generate verification scripts, not just code
