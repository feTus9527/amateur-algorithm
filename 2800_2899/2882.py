import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/drop-duplicate-rows/description/
    """
    return customers.drop_duplicates(subset=["email"])
