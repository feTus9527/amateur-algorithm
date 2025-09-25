import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/modify-columns/description/
    """
    employees["salary"] = employees["salary"] * 2
    return employees
