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


def parse_numbers(value: object) -> Optional[float]:
    """converts k/M/B to float numerics"""
    try:
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)

        suffix = str(value).strip()
        if suffix == "":
            return None

        if suffix.endswith(("k", "K")):
            multiplier = 1000.0
            suffix = suffix[:-1]
        elif suffix.endswith(("m", "M")):
            multiplier = 1000000.0
            suffix = suffix[:-1]
        elif suffix.endswith(("b", "B")):
            multiplier = 1000000000.0
            suffix = suffix[:-1]
        else:
            multiplier = 1.0

        return float(suffix) * multiplier

    except Exception:
        return None


def draw_chart(years1: list, years2: list, vals1: list, vals2: list):
    """draw a chart using years1-2/vals1-2"""
    plt.figure()
    plt.plot(years1, vals1, label="France")
    plt.plot(years2, vals2, label="Albania")
    plt.title("Population projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


def main() -> None:
    """entrypoint, loads datasets and displays them in a chart"""
    try:
        dataset = load("population_total.csv")
        if dataset is None:
            return
        series1 = load_series(dataset, "France")
        if series1 is None:
            return
        series2 = load_series(dataset, "Albania")
        if series2 is None:
            return

        years1 = []
        vals1 = []
        for k, v in series1.items():
            try:
                year = int(k)
                if year < 1800 or year > 2050:
                    continue
                years1.append(year)
                vals1.append(parse_numbers(v))
            except Exception:
                """skips malformed lines"""
                continue
        if not years1:
            return

        years2 = []
        vals2 = []
        for k, v in series2.items():
            try:
                year = int(k)
                if year < 1800 or year > 2050:
                    continue
                years2.append(year)
                vals2.append(parse_numbers(v))
            except Exception:
                """skips malformed lines"""
                continue
        if not years2:
            return

        draw_chart(years1, years2, vals1, vals2)

    except Exception:
        return


if __name__ == "__main__":
    main()
