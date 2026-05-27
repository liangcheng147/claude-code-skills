# Common Migration Patterns

Reference guide for typical deep learning model migration scenarios.

## Pattern 1: Backbone Replacement

**Scenario**: Replace the encoder/backbone of model B with a different encoder from model A.

**Common Cases**:
- ResNet → ViT backbone
- EfficientNet → ConvNeXt backbone
- Custom CNN → pretrained CLIP/DINOv2 backbone

**Key Considerations**:
- Output feature dimensions must match downstream layers
- Multi-scale features (FPN-style) need matching channel counts at each level
- Positional embeddings may need interpolation if spatial resolution changes

**Typical Adapter**:
```python
# When source outputs dim=1024 but target expects dim=768
self.adapter = nn.Linear(1024, 768)
# Or for spatial mismatch
self.spatial_adapter = nn.AdaptiveAvgPool2d(target_size)
```

## Pattern 2: Branch Replacement

**Scenario**: Model B has multiple branches (e.g., dual-branch network). Replace one branch with a module from model A.

**Common Cases**:
- Replace conv branch with attention branch
- Replace local feature branch with global feature branch
- Replace frequency domain branch with spatial domain branch

**Key Considerations**:
- The other branch(es) remain untouched — verify their inputs still work
- Fusion point (where branches merge) may need dimension adjustment
- Gradient flow through the untouched branch should not be affected

**Typical Structure**:
```python
class DualBranchModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.branch_a = OriginalBranchA()      # untouched
        self.branch_b = MigratedBranchB()       # from source model
        self.fusion = FusionModule()            # may need adjustment

    def forward(self, x):
        feat_a = self.branch_a(x)
        feat_b = self.branch_b(x)              # check: same input format?
        return self.fusion(feat_a, feat_b)     # check: matching dims?
```

## Pattern 3: Attention Mechanism Transfer

**Scenario**: Transfer a specific attention mechanism from model A into model B.

**Common Cases**:
- Standard self-attention → windowed attention (Swin-style)
- Self-attention → cross-attention (for dual-input)
- Single-head → multi-head with different head count
- Add spatial attention to channel attention (CBAM-style)

**Key Considerations**:
- Attention dimension (q/k/v dim) must match
- Number of heads must divide the dimension evenly
- Relative position bias may need retraining
- Temperature/scaling factors may differ between models

## Pattern 4: Decoder/Head Replacement

**Scenario**: Replace the classification head or decoder of model B with one from model A.

**Common Cases**:
- Single-class head → multi-class head
- Linear head → MLP head
- Simple decoder → UNet-style decoder with skip connections

**Key Considerations**:
- Input dimension to the head must match encoder output
- If adding skip connections, need intermediate feature maps from encoder
- Output format (logits vs probabilities) must match loss function

## Pattern 5: Design Pattern Transfer

**Scenario**: Not migrating actual code, but transferring an architectural idea.

**Common Cases**:
- "I want residual connections like ResNet in my custom model"
- "I want the hierarchical structure of Swin Transformer"
- "I want the frequency decomposition approach from SPAI"

**Approach**:
1. Understand the core idea from the source model
2. Design a new module that implements the same idea in the target model's context
3. This is the most creative case — the AI should propose a design, not just copy code

## Pattern 6: Multi-Scale Feature Fusion

**Scenario**: Add multi-scale feature extraction to a single-scale model.

**Common Cases**:
- Single-resolution ViT → multi-scale with FPN
- Add feature pyramid to CNN backbone
- Add intermediate feature extraction to transformer

**Key Considerations**:
- Which layers to extract features from
- How to align features at different scales (interpolation vs strided conv)
- Fusion method: concatenation, element-wise addition, attention-weighted fusion
