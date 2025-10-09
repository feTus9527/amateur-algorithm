from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/create-a-dataframe-from-list/description/
    """
    return pd.DataFrame(
        {
            "student_id": [d[0] for d in student_data],
            "age": [d[1] for d in student_data],
        }
    )
