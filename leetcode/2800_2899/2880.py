import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/select-data/description/
    """
    return students.loc[students["student_id"] == 101, ["name", "age"]]
