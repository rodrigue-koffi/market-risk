import numpy as np
import pandas as pd
from scipy.stats import norm


def computeParametricVaR(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    alpha: float = 0.99
) -> pd.DataFrame:
    df = df.copy()

    mu = df[returnCol].mean()
    sigma = df[returnCol].std()

    varValue = norm.ppf(1 - alpha, mu, sigma)
    df[f"varParam_{int(alpha*100)}"] = varValue

    return df
