from typing import Any


def callLimit(limit: int):
    """
    接收裝飾器參數的函數。
    Function that takes the decorator arguments.
    In this case, the limiter.
    """
    count = 0

    def callLimiter(function):
        """
        接收目標函數的函數。
        Function that takes the function.
        """

        def limit_function(*args: Any, **kwds: Any):
            """核心函數 Core function"""

            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(
                    f"Error: Calling function <{function.__name__}> the "
                    f"[{count + 1}]th time, exceeding the call limit of "
                    f"[{limit}]."
                )
                return None
        return limit_function
    return callLimiter
