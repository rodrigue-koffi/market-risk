import pandas as pd
import numpy as np


def computeHistoricalVol(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    window: int = 252
) -> pd.DataFrame:
    df = df.copy()
    df["histVol"] = df[returnCol].rolling(window).std() * np.sqrt(252)
    df = df.dropna().reset_index(drop=True)
    return df
