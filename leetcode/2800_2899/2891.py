import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    See: https://leetcode.cn/problems/method-chaining/description/
    """
    return animals.loc[animals["weight"] > 100].sort_values(
        by="weight", ascending=False
    )[["name"]]
