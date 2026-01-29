def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object}", end=" ")
    elif type(object) == float and object != object:
        print(f"Cheese: {object}", end=" ")
    elif type(object) == bool and object is False:
        print(f"Fake: {object}", end=" ")
    elif type(object) == int and object == 0:
        print(f"Zero: {object}", end=" ")
    elif type(object) == str and object == "":
        print(f"Empty:", end=" ")
    else:
        print("Type not Found")
        return 1
    print(type(object))
    return 0

# NaN (Not a Number) is the only value that is not equal to itself:
#     >>> x = float("NaN")
#     >>> x == x
#     False
#     >>> x != x
#     True

# Checking bool before int because bool is a subclass of int.

# Nothing = None
#     empty value, type: NoneType
# Garlic = float("NaN")
#     type: float
# Zero = 0
#     type: int
# Empty = ""
#     type: str
# Fake = False
#     type: bool