from ft_filter import ft_filter


def main():
    """Returns the documentation and the return type of the function"""
    print(ft_filter.__doc__)
    print(type(ft_filter(lambda x: x > 0, [1, 2, 3])))

    print("-------------------------------")
    """Example"""
    numbers = [0, 1, 2, 3, 4, 5]

    # 篩選偶數
    even = ft_filter(lambda x: x % 2 == 0, numbers)
    print(list(even))  # [0, 2, 4]

    # function=None → 過濾掉 False 元素
    mixed = [0, "", 1, "Hello", [], [1, 2]]
    filtered = ft_filter(None, mixed)
    print(list(filtered))  # [1, 'Hello', [1,2]]
    # If no function's given, it returns the elements that are True.


if __name__ == "__main__":
    main()
