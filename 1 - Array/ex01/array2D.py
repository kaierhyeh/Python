# Error 處裡建議
#     「函數內」用 raise：
#         立即告知並編輯錯誤訊息。
#     「調用處」用 try-except：
#         決定如何呈現錯誤訊息。

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and print its shape before and after slicing.

    Args:
        family: 2D list of family members' data
        start: Starting index for slicing
        end: Ending index for slicing (exclusive)

    Returns:
        Sliced list
    """

    # 1. Verify input
    if not isinstance(family, list) or not isinstance(start, int) \
            or not isinstance(end, int):
        raise TypeError(
            "Family must be a list, and start and "
            "end must be integers."
        )
    if len(family) == 0:
        raise ValueError("List cannot be empty.")

    # 1-1. Verify list format
    row_len = None
    for i, row in enumerate(family):
        if not isinstance(row, list):
            raise TypeError(
                f"Family[{i}] must be a list, "
                f"got {type(row).__name__}."
            )
        if len(row) == 0:
            raise ValueError("Lists cannot be empty.")

        # 1-2. Row consistency check
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise ValueError(
                "All rows must have the same length.\n"
                f"Row 0 has {row_len} elements, "
                f"and row {i} has {len(row)} elements.")

        # 1-3. Value check
        for j, v in enumerate(row):
            if not isinstance(v, (int, float)):
                raise TypeError(
                    f"Family[{i}][{j}] must be int or float, "
                    f"got {type(v).__name__}."
                )

    # 2. Convert to NumPy array to get shape
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()

# • 什麼是 NumPy？
#     NumPy = Python 最強大的數值計算函式庫

# family = [
#     [1.80, 78.4],
#     [2.15, 102.7],
#     [2.10, 98.5],
#     [1.88, 75.2]
# ]
# Shape = (4, 2)
#          ↑  ↑
#          |  └─ 每row有 2 個元素（2 columns）
#          └─── 總共 4 rows


# Python List	   |  NumPy Array
# [1, 2, 3]      | array([1, 2, 3])
# 沒有 .shape    | 有 .shape 屬性 ✅
# 數學運算慢      | 數學運算超快 ⚡
# 不支援矩陣運算  | 支援矩陣運算 ✅
