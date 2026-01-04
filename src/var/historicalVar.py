import pandas as pd
import numpy as np


def computeHistoricalVaR(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    alpha: float = 0.99
) -> pd.DataFrame:
    df = df.copy()

    varValue = np.quantile(df[returnCol], 1 - alpha)
    df[f"varHist_{int(alpha*100)}"] = varValue

    return df
