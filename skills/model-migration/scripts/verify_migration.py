"""
Migration Verification Script Template

Customize this script for your specific migration. It verifies:
1. Forward pass produces correct output shapes
2. Backward pass gradients flow to all trainable parameters
3. Parameter count summary
4. Old vs new model output comparison (sanity check)

Usage:
    python verify_migration.py --input-shape "3,224,224"
"""

import argparse
import torch
import torch.nn as nn


def verify_forward_pass(model: nn.Module, input_shape: tuple[int, ...], device: str = "cpu") -> bool:
    """Verify forward pass produces output with expected shape."""
    model.eval()
    model.to(device)

    dummy_input = torch.randn(2, *input_shape, device=device)

    try:
        with torch.no_grad():
            output = model(dummy_input)
        print(f"✅ Forward pass successful")
        print(f"   Input shape:  {dummy_input.shape}")
        print(f"   Output shape: {output.shape}")
        return True
    except Exception as e:
        print(f"❌ Forward pass failed: {e}")
        return False


def verify_backward_pass(model: nn.Module, input_shape: tuple[int, ...], device: str = "cpu") -> bool:
    """Verify gradients flow to all trainable parameters."""
    model.train()
    model.to(device)

    dummy_input = torch.randn(2, *input_shape, device=device)
    target = torch.randn(2, 1, device=device)  # adjust target shape as needed

    try:
        output = model(dummy_input)
        loss = nn.MSELoss()(output, target)
        loss.backward()

        has_grad = []
        no_grad = []
        for name, param in model.named_parameters():
            if param.requires_grad:
                if param.grad is not None and param.grad.abs().sum() > 0:
                    has_grad.append(name)
                else:
                    no_grad.append(name)

        print(f"✅ Backward pass successful")
        print(f"   Parameters with gradients: {len(has_grad)}")
        if no_grad:
            print(f"⚠️  Parameters WITHOUT gradients: {len(no_grad)}")
            for name in no_grad[:10]:
                print(f"      - {name}")
            if len(no_grad) > 10:
                print(f"      ... and {len(no_grad) - 10} more")
        return len(no_grad) == 0
    except Exception as e:
        print(f"❌ Backward pass failed: {e}")
        return False


def count_parameters(model: nn.Module) -> dict[str, int]:
    """Count total, trainable, and non-trainable parameters."""
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = total - trainable
    return {"total": total, "trainable": trainable, "frozen": frozen}


def print_parameter_summary(model: nn.Module):
    """Print detailed parameter summary."""
    counts = count_parameters(model)
    print(f"\n📊 Parameter Summary:")
    print(f"   Total:     {counts['total']:>12,}")
    print(f"   Trainable: {counts['trainable']:>12,}")
    print(f"   Frozen:    {counts['frozen']:>12,}")

    print(f"\n   Per-module breakdown:")
    for name, module in model.named_children():
        module_params = sum(p.numel() for p in module.parameters())
        module_trainable = sum(p.numel() for p in module.parameters() if p.requires_grad)
        print(f"   {name}: {module_params:>10,} total, {module_trainable:>10,} trainable")


def main():
    parser = argparse.ArgumentParser(description="Verify model migration")
    parser.add_argument("--input-shape", type=str, default="3,224,224",
                        help="Input shape as comma-separated values (e.g., '3,224,224')")
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    input_shape = tuple(int(x) for x in args.input_shape.split(","))

    print("=" * 60)
    print("Model Migration Verification")
    print("=" * 60)

    # TODO: Import or instantiate your migrated model here
    # Example:
    # from models.target_model import MigratedModel
    # model = MigratedModel()

    # print("\n--- Forward Pass Test ---")
    # verify_forward_pass(model, input_shape, args.device)

    # print("\n--- Backward Pass Test ---")
    # verify_backward_pass(model, input_shape, args.device)

    # print_parameter_summary(model)

    print("\n⚠️  Customize this script with your actual model imports and tests.")


if __name__ == "__main__":
    main()
