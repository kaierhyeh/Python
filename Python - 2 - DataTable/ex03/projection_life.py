import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from typing import Optional


def load_country_val(dataset: pd.DataFrame,
                     country: str, year: str) -> Optional[float]:
    """loads the value in the (dataset) for (country) in (year)"""
    try:
        row = dataset.loc[dataset["country"] == country]
        if row.empty:
            return None
        if year not in dataset.columns:
            return None
        data = row.iloc[0][year]
        if data is None:
            return None
        return float(data)
    except Exception:
        return None


def draw_chart(year: str, xs: list, ys: list):
    """draw a scatter chart showing life expectancy vs GDP"""
    plt.figure()
    plt.scatter(xs, ys, label=f"Year {year}", alpha=0.75)
    plt.title(f"{year}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.legend()
    plt.show()


def main() -> None:
    """entrypoint, loads datasets and displays them in a chart"""
    try:
        life_dataset = load("life_expectancy_years.csv")
        if life_dataset is None:
            return
        gdp_dataset = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        if gdp_dataset is None:
            return

        year = "1900"
        life_countries = set(life_dataset["country"].astype(str).tolist())
        gdp_countries = set(gdp_dataset["country"].astype(str).tolist())
        intersect = sorted(gdp_countries.intersection(life_countries))
        xs: list = []
        ys: list = []

        for country in intersect:
            gdp_val = load_country_val(gdp_dataset, country, year)
            if gdp_val is None or gdp_val <= 0:
                continue
            life_val = load_country_val(life_dataset, country, year)
            if life_val is None:
                continue
            xs.append(gdp_val)
            ys.append(life_val)

        if not xs:
            return

        draw_chart(year, xs, ys)

    except Exception:
        return


if __name__ == "__main__":
    main()
