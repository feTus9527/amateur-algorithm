import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/rename-columns/description/
    """
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
