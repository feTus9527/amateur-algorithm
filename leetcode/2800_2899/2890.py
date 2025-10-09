import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/reshape-data-melt/description/
    """
    return pd.melt(report, id_vars="product", var_name="quarter", value_name="sales")
