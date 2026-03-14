from S1E9 import Character


class Baratheon(Character):
    """Baratheon class, inheriting Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon constructor."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):     # Representation
        """給開發者看的：如何產生該物件的指令"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):      # String
        """給使用者看的：漂亮好讀的格式"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """die method."""
        super().die()


class Lannister(Character):
    """Lannister class, inheriting Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Lannister constructor."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    # 預設情況下，當你直接對一個物件做 print() 時，Python 會自動呼叫 __str__。
    # 如果你沒有定義 __str__，Python 就會退而求其次，使用 __repr__。
    # 若兩者都沒定義則會直接回傳包含「類別名稱」與「記憶體位址」的字串。
    # ie.
    #     Cersei = Lannister("Cersei")
    #     print(Cersei)
    #     # 輸出: <__main__.Lannister object at 0x7fa8b9c23d10>
    #     # (類別名稱 + 記憶體位址)
    def __repr__(self):
        """給開發者看的：如何產生該物件的指令"""
        # 理想狀態：回傳類似 Baratheon('Robert', is_alive=True) 這樣的字串
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """給使用者看的：漂亮好讀的格式"""
        # 例如只印出簡單的名字和狀態
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """die method."""
        super().die()

    # 在一般情況下，類別裡面的方法都必須要有實體（self）才能呼叫。
    # ie.平常我們創造角色是寫 Cersei = Lannister("Cersei")，
    # 這是把藍圖（Class）拿來實體化。
    # 但 Jaine = Lannister.create_lannister("Jaine", True)，
    # 居然是「直接對著藍圖 (Lannister) 呼叫一個方法」！
    # 「不需要實體，直接掛在類別藍圖上供人使用」，為此我們需要 @classmethod。
    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        這是一個類別方法 (工廠方法)。
        cls 就代表 Lannister 這個類別本身。
        """
        return cls(first_name, is_alive)
