from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):      # 多重繼承：寫在前面的擁有絕對優先權！
    """King class, inheriting Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """King constructor."""
        super().__init__(first_name, is_alive)

    def __repr__(self):     # Representation
        """給開發者看的：如何產生該物件的指令"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):      # String
        """給使用者看的：漂亮好讀的格式"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """die method."""
        super().die()

    # This too C++/Java. The modern way is to use @property below.
    def set_eyes(self, color: str):
        """set eye color."""
        self.eyes = color

    def set_hairs(self, color: str):
        """set hair color."""
        self.hairs = color

    def get_eyes(self):
        """get eye color."""
        return self.eyes

    def get_hairs(self):
        """get hair color."""
        return self.hairs

    # # The above is too C++/Java. The pythonic way is to use @property:
    # @property
    # def eyes(self):
    #     """get eye color."""
    #     return self._eyes
    #     # Need to use _eyes to avoid infinite recursion 自己呼叫自己 (無限迴圈).
    #     # return self.eyes    # 🔴 呼叫 @property 自己！
    #     # return self._eyes   # 🟢 回傳真正的變數

    # @eyes.setter
    # def eyes(self, color: str):
    #     """set eye color."""
    #     self._eyes = color

    # @property
    # def hairs(self):
    #     """get hair color."""
    #     return self._hairs

    # @hairs.setter
    # def hairs(self, color: str):
    #     """set hair color."""
    #     self._hairs = color
