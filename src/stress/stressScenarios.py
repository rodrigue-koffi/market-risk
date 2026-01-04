import numpy as np
import pandas as pd


def stressReturns(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    shock: float = 2.0
) -> pd.DataFrame:
    df = df.copy()
    df["stressedReturn"] = df[returnCol] * shock
    return df
