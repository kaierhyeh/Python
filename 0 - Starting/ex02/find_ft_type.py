def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print("List : ", end="")
    elif type(object) == tuple:
        print("Tuple :", end=" ")
    elif type(object) == set:
        print("Set :", end=" ")
    elif type(object) == dict:
        print("Dict :", end=" ")
    elif type(object) == str:
        print(f"{object} is in the kitchen :", end=" ")
        # end=" ": to end the printed output with a space instead of a newline.
    else:
        print("Type not found")
        return 42
    print(type(object))
    return 42
