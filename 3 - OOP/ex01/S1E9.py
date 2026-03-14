from abc import ABC, abstractmethod


# 1. 建立抽象類別 Character
#    繼承 ABC 就等於告訴 Python：「這是一張抽象藍圖，不准直接實體化它！」
class Character(ABC):
    """
    This is an Abstract Base Class,
    defining all the common attributes and behaviors of characters.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Character 的建構子(constructor)。
        初始化 first_name 和 is_alive，並預設 is_alive 是 True。
        """
        # 在 Python，宣告成員變數不需像 C++ 在 class.hpp 先宣告型別，再到.cpp賦值。
        # 直接在 __init__ 裡面宣告後掛在 self 身上即可。
        self.first_name = first_name
        self.is_alive = is_alive

    # 在 Python 中，抽象方法通常可以先寫 pass (什麼都不做)
    # 或者也可以在這裡寫好實作，讓子類別繼承。
    # @abstractmethod 就是 C++ 的 virtual f() = 0

    @abstractmethod
    def die(self):
        """這是一個抽象方法，用來將狀態改為 False。"""
        self.is_alive = False
    # Or:
    # @abstractmethod
    # def die(self):
    #     """這是一個抽象方法。子類別必須自己決定怎麼死。"""
    #     pass  # 👈 沒錯，就是寫 pass！乾淨俐落！


# 2. 建立子類別 Stark
class Stark(Character):
    """Stark 類別，繼承 Character。"""

    # 在 Python，若子類別的建構子「沒有任何自己獨有的新變數」，
    # 只是單純把東西傳給父類別，_init__ 可以省略不寫！
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Stark 的建構子。
        使用 super() 將參數往上傳遞給父類別 Character 進行初始化。
        """
        super().__init__(first_name, is_alive)
        # 如果Stark有自己獨有的變數，可以寫在這裡，例如：
        # self.slots = 2

    def die(self):
        """實作父類別的抽象方法，把 is_alive 變成 False。"""
        super().die()
        # 或是自己定義：
        # self.is_alive = False


# 模板：
# from abc import ABC, abstractmethod

# # 1. 建立抽象類別 Appliance (對應你的 Character)
# #    繼承 ABC 就等於告訴 Python：「這是一張抽象藍圖，不准直接實體化它！」
# class Appliance(ABC):
#     """
#     這是一個家電的抽象基底類別 (Abstract Base Class)。
#     定義了所有家電共有的屬性與行為。
#     """

#     def __init__(self, brand_name: str, is_plugged: bool = True):
#         """
#         Appliance 的建構子。
#         初始化品牌名稱，並預設插頭是插上的 (True)。
#         """
#         # 在 Python 裡，宣告成員變數不需要像 C++ 一樣在 class 頂端先宣告型別
#         # 直接在 __init__ 裡面掛在 self 身上即可
#         self.brand_name = brand_name
#         self.is_plugged = is_plugged

#     # 在 Python 中，抽象方法通常可以先寫 pass (什麼都不做)
#     # 或者也可以在這裡寫好實作，讓子類別繼承。
#     # 根據你的作業邏輯，你可以把「改變狀態」的方法設為抽象，強迫子類別一定要實作。
#     @abstractmethod
#     def unplug(self):
#         """
#         這是一個抽象方法，用來拔掉家電插頭，將狀態改為 False。
#         (對應你的 die 方法)
#         """
#         self.is_plugged = False


# # 2. 建立子類別 Toaster (對應你的 Stark)
# class Toaster(Appliance):
#     """
#     烤麵包機類別，繼承自家電 (Appliance)。
#     """

#     # 這裡的 is_plugged=True 是預設參數
#     def __init__(self, brand_name: str, is_plugged: bool = True):
#         """
#         Toaster 的建構子。
#         使用 super() 將參數往上傳遞給父類別 Appliance 進行初始化。
#         """
#         super().__init__(brand_name, is_plugged)
#         # 如果烤麵包機有自己獨有的變數，可以寫在這裡，例如：
#         # self.slots = 2

#     def unplug(self):
#         """
#         實作父類別的抽象方法。
#         把插頭拔掉，也就是把 is_plugged 變成 False。
#         """
#         self.is_plugged = False
