# tqdm 是一個來自阿拉伯語的縮寫，代表"進度條"。
# yield 的效果很像「在 for 迴圈中，一次吐出一個東西」。
#     讓 function 像迴圈一樣，一步一步「產生值」，
#     每次迴圈要求下一個值時，function 就會繼續到下一個 yield。

import os


def ft_tqdm(lst: range) -> None:
    """
    Shows a dynamic progress bar in the terminal,
    using yield.
    """

    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    bar_size = max(10, terminal_width - 20)
    for i, item in enumerate(lst, 1):
        percent = int(i / total * 100)
        progress = int(bar_size * i / total)
        bar = "█" * progress + " " * (bar_size - progress)
        print(f"\r{percent:3d}%|{bar}| {i}/{total}", end="", flush=True)
        # 3d: at least "3" digits in "decimal"
        # flush=True 不經buffer、無延遲
        yield item
    print()


# Bar style in the subject:
#     bar = "=" * progress + ">" + " " * (bar_size - progress)
#     print(f"\r{percent:3d}%|[{bar}]| {i}/{total}", end="", flush=True)

# 時間與速率需要 import time 才能算。

# for (index, element) in enumerate(iterable, start=1):
#     yield item
#     這樣 generator 才能完全模擬原本的迭代行為，儘管我們這裡沒有用到 item。

# • start 只影響索引，而不會改變你從列表（或任何 iterable）讀取元素的順序。
# lst = ['a', 'b', 'c']
#     若用預設 start=0：
#         (0, 'a')
#         (1, 'b')
#         (2, 'c')
#     若用 start=1：
#         (1, 'a')
#         (2, 'b')
#         (3, 'c')
