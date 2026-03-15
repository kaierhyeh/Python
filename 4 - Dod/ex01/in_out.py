# Exponentiation of argument by himself:
#     return x^x, ie. 1.5^1.5, 2^2, etc.

# 絕對的四個作用域/層 scopes (LEGB Rule):
#     Local 區域 < Enclosing 巢狀/嵌套域 < Global 全域 < Built-in 內建域

#  • Enclosing 指的是 Local 區域 和 Global 全域 間的 scopes。
#     因 Enclosing 裡能有多重域相互包含，故又稱巢狀域。
#  • Built-in：這是 Python 宇宙的最外層，打從你啟動 Python 就已經存在的變數和函數。

# 1. 尋找變數、函數時，可以由內而外 (L -> E -> G -> B) 一路往上看；
#     但修改變數時，預設只能修改自己那一層 (Local) 的變數。
# 2. nonlocal 的穿透力只存在於 Enclosing (E) 的範圍裡。
#     它如果一路往上找，找穿了所有的函數，來到最外面的 Global (G) 範圍依舊找不到時，
#     它就會報錯 (SyntaxError)。因為要改 Global 的變數，你必須用：global x。
# 3. Closure（閉包）能想像成一個「魔法背包」，
#     專門儲存所有被內部函數使用到的外部變數、函數。(under enclosing scope)

def square(x: int | float) -> int | float:
    """Square of argument."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Exponentiation of argument by himself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Outer function."""
    count = 0

    def inner() -> float:
        """Inner function."""

        nonlocal x, count      # 宣告要修改 outer variables
        count += 1
        x = function(x)
        return x
    return inner
