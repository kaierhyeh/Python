import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from typing import Optional


def load_series(dataset: pd.DataFrame, country: str) -> Optional[pd.Series]:
    """loads the series for the (country) using the (dataset)"""
    try:
        row = dataset.loc[dataset["country"] == country]
        if row.empty:
            return None
        data = row.iloc[0].drop(labels=["country"])
        return data
    except Exception:
        return None


def draw_chart(years: int, vals: float):
    """draw a chart using years/vals"""
    plt.figure()
    plt.plot(years, vals, label="France")
    plt.title("Life expectancy in France")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.show()


def main() -> None:
    """entrypoint, loads dataset and displays the line chart for a country"""
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            return
        series = load_series(dataset, "France")
        if series is None:
            return

        years = []
        vals = []
        for k, v in series.items():
            try:
                # print(k, v)
                years.append(int(k))
                vals.append(float(v))
            except Exception:
                """skips malformed lines"""
                continue
        if not years:
            return

        draw_chart(years, vals)

    except Exception:
        return


if __name__ == "__main__":
    main()
