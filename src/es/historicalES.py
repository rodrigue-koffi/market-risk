import numpy as np
import pandas as pd


def computeHistoricalES(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    alpha: float = 0.99
) -> pd.DataFrame:
    df = df.copy()

    varValue = np.quantile(df[returnCol], 1 - alpha)
    esValue = df.loc[df[returnCol] <= varValue, returnCol].mean()

    df[f"esHist_{int(alpha*100)}"] = esValue
    return df
