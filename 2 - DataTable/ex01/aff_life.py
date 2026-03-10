#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
# Matplotlib 是 Python 負責資料視覺化，
# 將數據畫成各種圖表（折線圖、長條圖、散佈圖等）的強大函式庫。


def extract_country_data(dataset: pd.DataFrame, country: str) -> pd.Series:
    """
    Extracts life expectancy data for a specific country.
    Improved with O(1) index lookup.
    """

    # 設 index 加速搜尋
    if 'country' in dataset.columns:
        search_dataset = dataset.set_index('country')
        # 產生一個「新的」DataFrame 來做搜尋，不加 inplace=True
        # 這樣原本傳進來的 dataset 就能保持原樣，
        # 這在函數式編程中叫 "Pure Function"。
    else:
        search_dataset = dataset
    try:
        # Series：「帶有標籤的一維陣列」
        series = search_dataset.loc[country]    # locate by index
        if isinstance(series, pd.DataFrame):
            # 有多個同名國家，取第一列
            series = series.iloc[0]             # locate by integer
        return series
    # If "country" index doesn't exist,
    # neither would search_dataset.loc["country"].
    except KeyError:
        print(f"Error: Country '{country}' not found.")
        return None
# 原版：
# if 'country' in dataset.columns:
#         dataset.set_index('country', inplace=True)
# 但：
#     但在大型專案中，如果你把一個 DataFrame 傳進函數，
#     卻在函數裡面「原地 (in-place)」修改了它，這可能會讓呼叫這個函數
#     的其他程式碼產生預期外的 Bug（因為原始資料被改變了）。

# if isinstance(series, pd.DataFrame):
#     如果原始資料中不小心有兩筆以上同樣叫做 'Taiwan' 的資料列，
#     Pandas 不知道你要哪一個，所以它會把所有叫 'Taiwan' 的列都抓出來，
#     打包成一個二維表格的 pd.DataFrame 丟還給你。


def draw_chart(data: pd.Series, country: str):
    """
    Plots the life expectancy graph using pandas
    Series data directly.
    """

    # 高效轉型：直接利用 Series 的 index (years) 和 values
    try:
        years = data.index.astype(int)
        values = data.values.astype(float)
    except ValueError:
        print("Error: Data contains non-numeric values.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, label=country)
    # 設置標籤
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    # 刻度
    plt.xticks(list(range(1800, 2101, 40)))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    plt.savefig("life_expectancy_france.jpg")
    print("Graph saved.")
    plt.show()

# astype 是 Pandas 和 NumPy 裡用來轉換資料型別 (Data Type) 的函數。
#     全名：Array-Style Type Conversion。
# 假設本來是字串: ["1", "2", "3"]
# 呼叫: array.astype(int)
# 結果: [1, 2, 3]  (變 int)

# plt.tight_layout() 是一個非常實用的自動排版功能：
#     它會自動調整子圖 (Subplots)、軸標籤 (Labels) 和標題 (Titles) 的位置，
#     確保它們：
#     1. 不會重疊
#     2. 不會被切掉、有足夠的空間
#     3. 減少不必要的留白


def main() -> None:
    """Main entry point."""

    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return

    country = "France"
    series = extract_country_data(dataset, country)
    if series is not None:
        draw_chart(series, country)


if __name__ == "__main__":
    main()
