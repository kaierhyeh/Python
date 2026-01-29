from array2D import slice_me

# === Test 1: Normal case ===
print("=" * 60)
print("Test 1: Normal case")
print("=" * 60)

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# === Test 2: Inconsistent row lengths ===
print("\n" + "=" * 60)
print("Test 2: Inconsistent row lengths")
print("=" * 60)

family_bad = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10],  # ← 只有 1 個元素！
              [1.88, 75.2]]

try:
    print(slice_me(family_bad, 0, 2))
except ValueError as e:
    print(f"✓ Caught error: {e}")

# === Test 3: Empty list ===
print("\n" + "=" * 60)
print("Test 3: Empty list")
print("=" * 60)

try:
    print(slice_me([], 0, 2))
except ValueError as e:
    print(f"✓ Caught error: {e}")

# === Test 4: Non-numeric value ===
print("\n" + "=" * 60)
print("Test 4: Non-numeric value")
print("=" * 60)

family_bad2 = [[1.80, "abc"],
               [2.15, 102.7]]

try:
    print(slice_me(family_bad2, 0, 2))
except TypeError as e:
    print(f"✓ Caught error: {e}")
