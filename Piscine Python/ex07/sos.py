import sys


def handle_error():
    """Print the error message and exit."""

    print("AssertionError: Bad argument.")
    print("[Usage] python3.10 sos.py STRING")
    exit()


def morse():
    """Morse code dictionary"""

    return {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/"
    }


def main():
    """Translate a string to Morse code."""

    if len(sys.argv) != 2:
        handle_error()
    s = sys.argv[1]
    for c in s:
        if not (c.isalnum() or c == " "):
            handle_error()
    M = morse()     # 不能對 function 使用 []
    res = " ".join(M[c.upper()] for c in s)
    # 分隔符.join(清單)
    # Equivalence:
    # for i, c in enumerate(s):
    #     print(morse(c.upper()), end="")
    #     if i != len(s) - 1:
    #         print(" ", end="")
    print(res)


if __name__ == "__main__":
    main()
