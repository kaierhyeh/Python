import matplotlib.pyplot as plt     # pip3 install matplotlib
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Invert the color of an image."""

    img = 255 - array
    try:
        plt.imshow(img)
        plt.title("Inverted")
        plt.savefig("inverted.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img


def ft_red(array) -> np.ndarray:
    """Convert an image to red."""

    img = array.copy()
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    try:
        plt.imshow(img)
        plt.title("Red")
        plt.savefig("red.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img


def ft_green(array) -> np.ndarray:
    """Convert an image to green."""

    img = array.copy()
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    try:
        plt.imshow(img)
        plt.title("Green")
        plt.savefig("green.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img


def ft_blue(array) -> np.ndarray:
    """Convert an image to blue."""

    img = array.copy()
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    try:
        plt.imshow(img)
        plt.title("Blue")
        plt.savefig("blue.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img


def ft_grey(array) -> np.ndarray:
    """Convert an image to greyscale."""

    img = array.copy()
    color = np.mean(img, axis=2)  # table manipulation allowed
    img[:, :, 0] = color
    img[:, :, 1] = color
    img[:, :, 2] = color
    try:
        plt.imshow(img)
        plt.title("Grey")
        plt.savefig("grey.jpg")
    except Exception as e:
        print(f"Error displaying image: {e}")
    return img

# axis: The dimension along which to operate.
# image[height, width, channel]
#     height: axis = 0
#     width: axis = 1
#     channel: axis = 2

# np.mean(axis=2) 是最優解，因為它比 sum / 3 更安全
# (處理溢位)。
# 可以改成 img.astype(float).sum(axis=2) / 3
