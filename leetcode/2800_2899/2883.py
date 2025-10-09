import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/drop-missing-data/description/
    """
    return students.dropna(subset=["name"])
