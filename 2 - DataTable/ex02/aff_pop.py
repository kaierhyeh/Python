#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter  # 用來格式化 Y 軸
from load_csv import load
from typing import Optional


def parse_numbers(value: object) -> Optional[float]:
    """Convert k/M/B to float numerics"""

    try:
        if pd.isna(value) or value is None:
            return None     # isna: is not available
        if isinstance(value, (int, float)):
            return float(value)

        suffix = str(value).strip()
        if not suffix:
            return None

        # k = 10^3, M = 10^6, B = 10^9
        if suffix[-1].lower() == "k":
            return float(suffix[:-1]) * 1e3
        elif suffix[-1].lower() == "m":
            return float(suffix[:-1]) * 1e6
        elif suffix[-1].lower() == "b":
            return float(suffix[:-1]) * 1e9
        else:
            return float(suffix)
    except Exception:
        print("Error: Data conversion failed.")
        return None
# value: object
#     雖然什麼都沒有宣告、只能操作所有物件共有的基本方法，
#     但執行時系統會檢查型別：
#     value.strip()       # 系統會跳錯誤
#     str(value).strip()  # 系統會正常執行

# Optional[float]: 即 value: float | None
#     表示會回傳 float 但也有可能會給 None。


def extract_and_clean_data(dataset: pd.DataFrame, country: str) \
        -> Optional[pd.Series]:
    """
    Select a country, filter 1800-2050, and convert strings to numbers.
    """

    row = dataset.loc[dataset["country"] == country]    # locate by index
    if row.empty:
        print(f"Warning: Country '{country}' not found.")
        return None

    # 製出一份全新的 Series : data
    # 0. 取出該國資料並去掉 'country' 欄位
    data = row.iloc[0].drop(labels=["country"])         # locate by integer
    # 1. 將 X 軸 (Index，也就是年份) 轉成整數
    data.index = data.index.astype(int)
    # 2. 強大的 Pandas 切片！直接抓取 1800 到 2050 年
    data = data.loc[1800:2050]
    # 3. 強大的 apply！把 parse_numbers 自動套用到每一個數值上 (取代 for 迴圈)
    data = data.apply(parse_numbers)

    return data
# .drop() 的時候，Pandas 不會去動原本的資料，
#     而是會在記憶體裡複製出一份全新的 Series，
#     然後把這份新資料交給變數 data。


def format_y_axis(value: float, pos: int) -> str:
    """Format Y-axis to show 20k, 40M instead of scientific notation (2e7)"""

    if value >= 1e9:
        return f"{value / 1e9:.1f}B"    # 數字大，留一位小數
    elif value >= 1e6:
        return f"{value / 1e6:.0f}M"    # 數字相對小，不留小數
    elif value >= 1e3:
        return f"{value / 1e3:.0f}k"
    return str(int(value))


def draw_chart(countries_data: dict[str, pd.Series]):
    """
    Receive a dictionary containing countries and their data,
    and dynamically draw the chart.
    """

    plt.figure(figsize=(10, 6))

    # 不管字典裡有幾個國家，一個迴圈就能全部畫完！
    for country, data in countries_data.items():
        plt.plot(data.index, data.values, label=country)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    # 套用 Y 軸格式化器
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y_axis))

    # 設定 X 軸刻度
    plt.xticks(list(range(1800, 2051, 40)))

    plt.legend(loc="lower right")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("population_total.jpg")
    print("Graph saved.")
    plt.show()


def main() -> None:
    """Main entry point."""

    dataset = load("population_total.csv")
    if dataset is None:
        return

    target_countries = ["France", "Japan"]
    plot_data = {}
    for country in target_countries:
        series = extract_and_clean_data(dataset, country)
        if series is not None:
            plot_data[country] = series

    if plot_data:
        draw_chart(plot_data)


if __name__ == "__main__":
    main()
