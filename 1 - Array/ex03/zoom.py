#!/usr/bin/env python3

import matplotlib.pyplot as plt     # pip3 install matplotlib
from load_image import ft_load


def main():
    """
    Load an image, display the shape,
    zoom in on the center, and update the shape.
    """

    # Read & display
    img = ft_load("animal.jpeg")
    if img is None:
        return

    # Zoom in with the shape (400, 400, 1)
    h, w = img.shape[:2]
    if h >= 768 and w >= 1024:
        zoomed_img = img[109:509, 437:837, 0:1]
    else:
        zoomed_img = img[
            h // 2 - int(h * 0.375):h // 2 + int(h * 0.375),
            w // 2 - int(w * 0.375):w // 2 + int(w * 0.375),
            0:1]
    print(f"New shape after slicing: {zoomed_img.shape}")
    print(zoomed_img)
    try:
        plt.imshow(zoomed_img.squeeze(), cmap="gray")
        plt.title("Zoomed Image")
        plt.savefig("zoomed_animal.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")


if __name__ == "__main__":
    main()

# 在範例中剪裁後的形狀為(400, 400, 1)或(400, 400)，
# 同時每個像素中只有一個值，代表處理後的圖片必須是
# 單通道 (Single Channel) 的。
# 而在圖片處理的世界裡，單通道通常就代表
# 灰階圖 (Grayscale) 或 二值圖 (Black & White)。
# 所以在取 0:1 後需要 squeeze 成 2D。
