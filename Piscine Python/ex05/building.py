# Rules:
#     1. No code in the global scope.
#     2. Each "program" must have its main.
#         def main():
#             # 你的主程式、測試、錯誤處理都寫這裡

#         if __name__ == "__main__":
#             main()

#         if __name__ == "__main__":
#         → 這一行是 Python 用來判斷：
#         「這個檔案是被直接執行？」還是「被當成模組匯入？」
#         如果你用 python3 myfile.py 直接執行檔案，
#         Python 會在記憶體裡建立一個變數叫 __name__（兩個底線），
#         然後自動幫你把值設成 "__main__"。
#         __name__ 就會是 "__main__"，所以會執行 main()。

#         但如果別的檔案 import myfile，
#         那麼 __name__ 會變成 "myfile"，
#         就不會執行 main()，避免干擾別人的程式。

#         這是 Python 的標準規範模式，也符合你作業要求「不能有程式在 global scope」。
#     3. Each "function" must have documentation: __doc__
#         你用 """ ... """ 寫 docstring
#         → Python 自動把它存到函式的 __doc__ 屬性裡。
#         → Python 會自動讓 add.__doc__ = " ... "
#     4. flake8（norm）會檢查什麼？
#         你的課程要求你遵循 Python 標準程式風格，也就是：
#         PEP 8（Python Enhancement Proposal #8）
#         a. 縮排
#             只能使用 4 spaces，不能用 tab。
#         b. 行長
#             一行建議不要超過 79 或 88 字元（依設定）。
#         c. 空白使用規則
#             x = 1
#         d. 函式和變數命名
#             - 小寫 + 底線：my_function（符合 PEP8）
#             - 不允許用駝峰式：myFunction（flake8 會抱怨）
#         e. 未使用的變數、import
#         f. 缺少 docstring
#         g. 語法錯誤、格式不完整


import string
import sys


def main():
    """Verify characters:
        upper and lower letters, punctuation marks, spaces and digits."""
    if len(sys.argv) > 2:
        print("AssertionError")
        print("[Usage] python3.10 building.py STRING")
        exit()
    elif len(sys.argv) == 1:
        print("Provide the text to count below:")
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    u, l, d, p, s = 0, 0, 0, 0, 0
    for c in text:
        if c.isupper():
            u += 1
        elif c.islower():
            l += 1
        elif c.isdigit():
            d += 1
        elif c in string.punctuation:
            # String of ASCII characters which are considered punctuation
            #     characters in the C locale:
            # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
            p += 1
        elif c.isspace():
            s += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{u} upper letters")
    print(f"{l} lower letters")
    print(f"{p} punctuation marks")
    print(f"{s} spaces")
    print(f"{d} digits")


if __name__ == "__main__":
    main()


# When using ctrl+D:
#     按一次 Ctrl+D → 緩衝區裡有文字，但不送給程式。
#     終端只把 EOF 放在緩衝區尾端，但程式仍在等待完整行。
#     你需要再按一次 Ctrl+D 才能讓 EOF 生效 → 程式結束。

# input() vs sys.stdin.read():
# 1. input():
#     讀一行（直到使用者按 Enter），不包含換行符 \n。
#     EOF：拋出 EOFError。
# 2. sys.stdin.read():
#     讀取 stdin 直到 EOF，包含換行符 \n。
#     EOF：不會拋出 EOFError，直接返回字串。
