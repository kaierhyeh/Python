def ft_filter(function, iterable):
    """
    Filters the elements that fit the function given as condition.
    Returns an iterator (set of elements) that
        when applied in the function, returns True.
    """

    if function is None:
        return (x for x in iterable if x)
    return (x for x in iterable if function(x))


# value/expression for variable in iterable if condition:
#     returns the "value/expression", using each "variable" in "range"
#     if "condition" is true.
# ie. 找偶數的平方：
# numbers = [1, 2, 3, 4]
# list = [x**2 for x in numbers if x % 2 == 0]
# print(list)   # [4, 16]
