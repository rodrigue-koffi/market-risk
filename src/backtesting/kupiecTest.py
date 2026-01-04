import numpy as np
import pandas as pd
from scipy.stats import chi2


def kupiecTest(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    varCol: str = "varHist_99",
    alpha: float = 0.99
) -> dict:
    returns = df[returnCol]
    varValue = df[varCol].iloc[0]

    exceptions = returns < varValue
    n = len(returns)
    x = exceptions.sum()

    p = 1 - alpha
    phat = x / n if n > 0 else 0

    if phat == 0 or phat == 1:
        return {"LR": np.nan, "exceptions": x}

    lrStat = -2 * (
        (n - x) * np.log((1 - p) / (1 - phat)) +
        x * np.log(p / phat)
    )

    pValue = 1 - chi2.cdf(lrStat, df=1)

    return {
        "LR": lrStat,
        "pValue": pValue,
        "exceptions": x
    }
