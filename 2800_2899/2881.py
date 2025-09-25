import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/create-a-new-column/description/
    """
    employees["bonus"] = 2 * employees["salary"]
    return employees
