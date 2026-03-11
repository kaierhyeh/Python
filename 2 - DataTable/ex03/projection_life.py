#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
from load_csv import load


def parse_numbers(value: object) -> float | None:
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


def clean_and_merge(df_gdp: pd.DataFrame, df_life: pd.DataFrame, year: str) \
        -> pd.DataFrame:
    """
    Extracts the specified year from both datasets, merges them,
    and cleans the data strings into floats.
    """

    # 1. 只切出 'country' 和 '1900' 這兩欄
    #    使用 .copy() 確保我們不會動到原本的 dataset (Pure Function 原則)
    gdp_year = df_gdp[['country', year]].copy()
    life_year = df_life[['country', year]].copy()

    # 2. 重新命名欄位！否則兩邊都叫 '1900'，合併後會變成 '1900_x' 和 '1900_y'。
    gdp_year.rename(columns={year: 'gdp'}, inplace=True)
    life_year.rename(columns={year: 'life'}, inplace=True)

    # 3. 對準 country 來合併兩欄 (兩個 DataFrame)
    # (把兩個一欄的資料合為一個兩欄的資料)
    merged_df = pd.merge(gdp_year, life_year, on='country')

    # 4. 向量化清洗資料：套用我們的 parse_numbers，把 '1.5k' 變成 1500
    merged_df['gdp'] = merged_df['gdp'].apply(parse_numbers)
    merged_df['life'] = merged_df['life'].apply(parse_numbers)

    # 5. 把那些轉型失敗或原本就是空值的行 (Row) 狠狠丟掉
    merged_df.dropna(inplace=True)

    return merged_df


def format_x_axis(value: float, pos: int) -> str:
    """Format X-axis to show 1k, 10k instead of scientific numbers"""

    if value >= 1000:
        return f"{value / 1000:.0f}k"
    return str(int(value))


def draw_chart(df: pd.DataFrame, year: str):
    """Draw a scatter chart showing Life Expectancy vs GDP"""

    plt.figure(figsize=(10, 6))

    # 畫散佈圖，直接把合併好的 DataFrame 欄位丟進去
    plt.scatter(df['gdp'], df['life'], label=f"Year {year}", alpha=0.7)

    plt.title(f"Life Expectancy vs Gross Domestic Product (Year {year})")
    plt.xlabel("Gross Domestic Product (GDP)")
    plt.ylabel("Life Expectancy (Years)")

    # Income needs to be scaled by log
    plt.xscale("log")

    # Let the X axis ticks follow Gapminder's aesthetics (300, 1000, 10000...)
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    # Apply formatter to look better
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_x_axis))

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("projection_life.jpg")
    print("Graph saved.")
    plt.show()


def main() -> None:
    """Entrypoint"""

    # 1. Load datasets
    df_life = load("life_expectancy_years.csv")
    if df_life is None:
        return
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if df_gdp is None:
        return

    # 2. Clean and merge datasets
    year = "1900"
    # Check if the target year exists in both datasets
    if year not in df_life.columns or year not in df_gdp.columns:
        print(f"Error: Year {year} not found in datasets.")
        return
    plot_df = clean_and_merge(df_gdp, df_life, year)

    # 3. Draw chart
    if not plot_df.empty:
        draw_chart(plot_df, year)
    else:
        print("Error: No valid data available to plot after cleaning.")


if __name__ == "__main__":
    main()
