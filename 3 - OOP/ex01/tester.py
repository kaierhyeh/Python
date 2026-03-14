#!/usr/bin/env python3
from S1E7 import Baratheon, Lannister


# Robert.__str__()：
#     下指令：「請執行這個函數並回傳字串。」
# Robert.__str__  ：
#     問 Python：「請問這個東西是什麼？」
#     Python：「這是一個綁定在物件上的方法，它長這樣...」
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
