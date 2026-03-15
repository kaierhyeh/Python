import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Random id generator"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


# 能設定自動與手動建立class類別的方法
# 自動生成 __init__, __repr__ 等 boilerplate (樣板程式碼) 的裝飾器
@dataclass
class Student:
    # 這些是可以手動輸入的參數
    # 這些欄位會出現在自動生成的 __init__ 參數中
    name: str
    surname: str
    active: bool = True

    # 這些是禁止手動輸入、由系統自動計算的參數
    # 使用 field(init=False) 確保它們不會出現在 __init__ 的參數名單中
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        在 __init__ 執行完後，自動計算並填入 login 與 id。
        """
        # 根據題目範例：Edward Eagle -> login 是 Eagle
        # (請根據你的 PDF 要求確認 logic 是不是直接拿 surname)
        self.login = self.name[0] + self.surname

        # 呼叫題目提供的函數
        self.id = generate_id()
