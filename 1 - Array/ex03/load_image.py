# Error 處裡建議
#     「函數內」用 raise：
#         立即告知並編輯錯誤訊息。
#     「調用處」用 try-except：
#         決定如何呈現錯誤訊息。

# shape: (height, width, channel色彩資訊)
# 色彩資訊通常是3個：RGB

from PIL import Image       # pip3 install numpy pillow
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format,
    and its pixels content in RGB format.
    """

    # 1. Verify input
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        with Image.open(path) as img:
            img = img.convert("RGB")
            arr = np.array(img)
            print(f"The shape of image is: {arr.shape}")
            print(arr)
            return arr
    except Exception as e:
        print(f"Error: {e}")
        return None
