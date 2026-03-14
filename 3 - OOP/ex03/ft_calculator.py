class calculator:
    """一個能與純量進行加減乘除的向量計算機"""

    def __init__(self, vector: list[float]):
        """Initialize"""
        self.vector = vector

    def __add__(self, object) -> None:
        """+ operator"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """* operator"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """- operator"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """/ operator"""
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
