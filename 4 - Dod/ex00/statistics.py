# args: positional arguments
# kwargs: keyword arguments
# f(1, "red", 3.14, True, c=10, d="blue")
# args = (1, "red", 3.14, True), a tuple.
# kwargs = {"c": 10, "d": "blue"}, a dict.
# Order matters: args are followed by kwargs.

from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate Mean, Median, Quartile (25% and 75%), Standard Deviation
    and Variance for the given numbers.
    """

    if args:
        sorted_args = sorted(args)
        n = len(args)
        mean = sum(args) / n
        var = sum((x - mean) ** 2 for x in args) / n
        std = var ** 0.5

    for request in kwargs.values():
        if not args:
            print("ERROR")
            continue

        if request == "mean":
            print(f"Mean: {mean}")
        elif request == "median":
            if n % 2 == 0:
                median = (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
            else:
                median = sorted_args[n // 2]
            print(f"Median: {median}")
        elif request == "quartile":
            q1 = float(sorted_args[n // 4])
            q3 = float(sorted_args[n // 4 * 3])
            print(f"Quartiles: [{q1}, {q3}]")
        elif request == "var":
            print(f"Variance: {var}")
        elif request == "std":
            print(f"Standard Deviation: {std}")
