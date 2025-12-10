"""
ft_color: Print colored text in terminal.
"""
# This is a module, a function collection,
#     and therefore doesn't have to have a main function.


# ANSI escape codes for colors
def get_color():
    """Returns a dictionary of ANSI escape codes for colors."""

    return {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }


def color_text(text: str, color: str) -> str:
    """Returns the given text wrapped in ANSI codes for the given color."""

    colors = get_color()
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
# f-string 用法，把文字加上 ANSI 顏色碼：
#     f"{COLOR}{text}{RESET}"


# Optional helper functions for each color
def red(text):
    """red"""
    return color_text(text, "red")


def green(text):
    """green"""
    return color_text(text, "green")


def blue(text):
    """blue"""
    return color_text(text, "blue")


def yellow(text):
    """yellow"""
    return color_text(text, "yellow")


def magenta(text):
    """magenta"""
    return color_text(text, "magenta")


def cyan(text):
    """cyan"""
    return color_text(text, "cyan")


def white(text):
    """white"""
    return color_text(text, "white")


def black(text):
    """black"""
    return color_text(text, "black")
