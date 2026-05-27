# Adapter Layer Catalog

Common adapter layers for resolving dimension and structure mismatches during model migration.

All code examples assume the following imports:
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
```

## Dimension Adapters

### Channel/Feature Dimension Mismatch

```python
# Linear projection (for transformer features)
class FeatureAdapter(nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        self.proj = nn.Linear(in_dim, out_dim)
        self.norm = nn.LayerNorm(out_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.norm(self.proj(x))

# 1x1 Conv (for CNN feature maps)
class ChannelAdapter(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)
        self.bn = nn.BatchNorm2d(out_channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.bn(self.conv(x))
```

### Spatial Dimension Mismatch

```python
# Adaptive pooling (most flexible)
class SpatialAdapter(nn.Module):
    def __init__(self, target_size: tuple[int, int]):
        super().__init__()
        self.pool = nn.AdaptiveAvgPool2d(target_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.pool(x)

# Interpolation (preserves more information)
class InterpolationAdapter(nn.Module):
    def __init__(self, mode: str = "bilinear"):
        super().__init__()
        self.mode = mode

    def forward(self, x: torch.Tensor, target_size: tuple[int, int]) -> torch.Tensor:
        return F.interpolate(x, size=target_size, mode=self.mode, align_corners=False)
```

### Sequence Length Mismatch (Transformer)

```python
# Positional embedding interpolation
class PosEmbedAdapter(nn.Module):
    def __init__(self, src_pos_embed: torch.Tensor, target_num_patches: int):
        super().__init__()
        src_num = src_pos_embed.shape[1] - 1  # exclude CLS
        cls_token = src_pos_embed[:, :1]
        pos_tokens = src_pos_embed[:, 1:]

        # Reshape to 2D, interpolate, reshape back
        h = w = int(src_num ** 0.5)
        pos_tokens = pos_tokens.reshape(1, h, w, -1).permute(0, 3, 1, 2)
        target_h = target_w = int(target_num_patches ** 0.5)
        pos_tokens = F.interpolate(pos_tokens, size=(target_h, target_w), mode="bicubic")
        pos_tokens = pos_tokens.permute(0, 2, 3, 1).flatten(1, 2)

        self.pos_embed = nn.Parameter(torch.cat([cls_token, pos_tokens], dim=1))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.pos_embed
```

## Normalization Adapters

### BatchNorm → LayerNorm (CNN to Transformer)

```python
class BNtoLNAdapter(nn.Module):
    def __init__(self, num_channels: int):
        super().__init__()
        self.norm = nn.LayerNorm(num_channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (B, C, H, W) → (B, H, W, C) → norm → (B, C, H, W)
        x = x.permute(0, 2, 3, 1)
        x = self.norm(x)
        return x.permute(0, 3, 1, 2)
```

### LayerNorm → BatchNorm (Transformer to CNN)

```python
class LNtoBNAdapter(nn.Module):
    def __init__(self, num_channels: int):
        super().__init__()
        self.norm = nn.BatchNorm2d(num_channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3:
            B, N, C = x.shape
            H = W = int(N ** 0.5)
            x = x.reshape(B, H, W, C).permute(0, 3, 1, 2)
            x = self.norm(x)
            return x.permute(0, 2, 3, 1).flatten(1, 2)
        return self.norm(x)
```

## Fusion Modules

### Concatenation Fusion

```python
class ConcatFusion(nn.Module):
    def __init__(self, dim_a: int, dim_b: int, out_dim: int):
        super().__init__()
        self.proj = nn.Linear(dim_a + dim_b, out_dim)
        self.norm = nn.LayerNorm(out_dim)

    def forward(self, feat_a: torch.Tensor, feat_b: torch.Tensor) -> torch.Tensor:
        return self.norm(self.proj(torch.cat([feat_a, feat_b], dim=-1)))
```

### Additive Fusion

```python
class AddFusion(nn.Module):
    def __init__(self, dim_a: int, dim_b: int):
        super().__init__()
        self.proj_a = nn.Linear(dim_a, dim_a) if dim_a != dim_b else nn.Identity()
        self.proj_b = nn.Linear(dim_b, dim_a) if dim_a != dim_b else nn.Identity()

    def forward(self, feat_a: torch.Tensor, feat_b: torch.Tensor) -> torch.Tensor:
        return self.proj_a(feat_a) + self.proj_b(feat_b)
```

### Cross-Attention Fusion

```python
class CrossAttentionFusion(nn.Module):
    def __init__(self, dim: int, num_heads: int = 8):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, num_heads, batch_first=True)
        self.norm = nn.LayerNorm(dim)

    def forward(self, query: torch.Tensor, kv: torch.Tensor) -> torch.Tensor:
        out, _ = self.attn(query, kv, kv)
        return self.norm(out + query)
```
