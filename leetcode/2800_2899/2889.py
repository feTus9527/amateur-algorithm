import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/reshape-data-pivot/description/
    """
    return pd.pivot_table(weather, index="month", columns="city", values="temperature")
