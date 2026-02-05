#!/usr/bin/env python3

import matplotlib.pyplot as plt     # pip3 install matplotlib
import numpy as np
from load_image import ft_load


def main():
    """
    Load an image, display the shape,
    cut a square part from it and transpose (rotate) it.
    """

    # Read & display
    img = ft_load("animal.jpeg")
    if img is None:
        return

    # Zoom in with the shape (400, 400)
    # 轉置只能處理 2D 矩陣，所以「取出 index 為 0 的那個通道」
    # 降維為 2D。
    h, w = img.shape[:2]
    if h >= 768 and w >= 1024:
        zoomed_img = img[109:509, 437:837, 0]
    else:
        zoomed_img = img[
            h // 2 - int(h * 0.375):h // 2 + int(h * 0.375),
            w // 2 - int(w * 0.375):w // 2 + int(w * 0.375),
            0]
    # 建立同樣 Data Type 的空白矩陣
    rows, cols = zoomed_img.shape   # shape 回傳 (x, y) tuple
    transposed_img = np.zeros((cols, rows), dtype=zoomed_img.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed_img[j, i] = zoomed_img[i, j]
    print(f"New shape after Transpose: {transposed_img.shape}")
    print(transposed_img)
    try:
        plt.imshow(transposed_img, cmap="gray")
        plt.title("Rotated Image")
        plt.savefig("rotated_animal.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")


if __name__ == "__main__":
    main()

# No need to sweat over zoomed_img = img[109:509, 437:837, 0]
# for the dimention cuz in ft_load:
# img = img.convert("RGB")後，
# Pillow 保證輸出一定是三通道 (H, W, 3)。
