# 不用實體化就能呼叫：就像 tester.py 寫的 calculator.dotproduct(a,b)，
# 我們不需要先寫 calc = calculator() 就能直接用。
# → @staticmethod

# 因為不需實體化，所以我們不需要__init__
class calculator:
    """向量計算機"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product V1 · V2"""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add vector V1 + V2"""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract vector V1 - V2"""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector: {res}")

# a = [1, 2, 3]
# b = [4, 5, 6]
# # zip(a, b) 會依序產出 (1,4), (2,5), (3,6)
# result = [x + y for x, y in zip(a, b)]
# # result 變成 [5, 7, 9]
