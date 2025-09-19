import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/display-the-first-three-rows/description/
    """
    return employees.head(3)
