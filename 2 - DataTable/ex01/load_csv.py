# Pandas 是 Python 最強大、最流行的資料分析庫。
# 它的名字來自 "Panel Data" (面板數據)。
# 它提供了 DataFrame (資料表) 結構，讓你在 Python 裡
# 像用 Excel 一樣處理幾百萬行的資料。

import pandas as pd     # pip3 install pandas


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file, print its dimensions, and return the dataset.

    Args:
        path (str): The file path to the CSV dataset.

    Returns:
        pd.DataFrame: The loaded dataset, or None if an error occurs.
    """

    try:
        dataset = pd.read_csv(path)
        if dataset.empty:
            print(f"Warning: The dataset at '{path}' is empty.")
            return None
        rows, cols = dataset.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")
        return dataset

    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(
            f"Error: Could not open '{path}'."
            f"Reason: {e}"
        )
        return None
    except pd.errors.EmptyDataError:    # 連讀都不能讀 (0 bytes)
        print(f"Error: The file '{path}' is empty or contains no data.")
        return None
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as e:
        print(
            f"Error: Failed to parse '{path}'."
            f"Reason: {e}"
        )
        return None
