import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/change-data-type/description/
    """
    students["grade"] = students["grade"].astype(int)
    return students
