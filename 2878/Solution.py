from typing import List

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    See: https://leetcode.cn/problems/get-the-size-of-a-dataframe/description/
    """
    return [players.shape[0], players.shape[1]]
