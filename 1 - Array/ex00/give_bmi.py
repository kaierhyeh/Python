import os


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate BMI"""
    # 1. Verify input
    # 1-1. List check
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists.")
    # 1-2. List length check
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    # 1-3. Empty list check
    if len(height) == 0:
        raise ValueError("Lists cannot be empty.")
    # 1-4. Number check
    for i, h in enumerate(height):
        if not isinstance(h, (int, float)):
            raise TypeError(f"Height[{i}] must be int or float, got {type(h).__name__}.")
        if h <= 0:
            raise ValueError(f"Height[{i}] must be positive, got {h}.")
    for i, w in enumerate(weight):
        if not isinstance(w, (int, float)):
            raise TypeError(f"Weight[{i}] must be int or float, got {type(w).__name__}.")
        if w <= 0:
            raise ValueError(f"Weight[{i}] must be positive, got {w}.")

    # 2. Calculate BMI
    return [w / (h**2) for h, w in zip(height, weight)]
    # Or:
    # return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI exceeds the limit."""
    # 1. Verify input
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("bmi must be a list and limit an integer.")
    if len(bmi) == 0:
        raise ValueError("List cannot be empty.")
    for i, b in enumerate(bmi):
        if not isinstance(b, (int, float)):
            raise TypeError(f"bmi[{i}] must be int or float, got {type(b).__name__}.")
        if b <= 0:
            raise ValueError(f"bmi[{i}] must be positive, got {b}.")

    # 2. Compare
    return [b > limit for b in bmi]
