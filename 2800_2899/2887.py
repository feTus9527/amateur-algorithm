import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/fill-missing-data/description/
    """
    return products.fillna({"quantity": 0})
