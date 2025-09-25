import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/reshape-data-concatenate/description/
    """
    return pd.concat([df1, df2])
