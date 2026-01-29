from ft_filter import ft_filter
import sys


def handle_error():
    """Print the error message and exit."""

    print("AssertionError: Bad arguments.")
    print("[Usage] python3.10 filterstring.py STRING INTEGER")
    exit()


def main():
    """
    Arguments: a string S and an integer N.
    The program outputs a list of words from S
    that have a length greater than N.

    • Words are separated from each other by space characters.
    • Strings do not contain any special characters
      (punctuation or invisible).
    """

    if len(sys.argv) != 3:
        handle_error()
    else:
        S = sys.argv[1]
        # Accept only alphabets, numbers and spaces
        # (not including \t nor \n).
        for c in S:
            if not (c.isalnum() or c == " "):
                handle_error()
        try:
            N = int(sys.argv[2])
        except ValueError:
            handle_error()

        words = S.split()
        print(list(ft_filter(lambda x: len(x) > N, words)))


if __name__ == "__main__":
    main()


# lambda 的概念：
# lambda = 匿名函式，就是不用 def 就能定義小函式。
# 語法：
# lambda 參數: 回傳值

# 範例：
# [正規函式]
# def square(x):
#     return x**2

# [lambda 寫法]
# square = lambda x: x**2

# [用法]
# print(square(5))  # 25

# [More] λ演算 lambda calculus
#     https://zh.wikipedia.org/wiki/%CE%9B%E6%BC%94%E7%AE%97
