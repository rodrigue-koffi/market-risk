import numpy as np
import pandas as pd


def computeLogReturns(df: pd.DataFrame, priceCol: str = "close") -> pd.DataFrame:
    df = df.copy()
    df["logReturn"] = np.log(df[priceCol] / df[priceCol].shift(1))
    df = df.dropna().reset_index(drop=True)
    return df
