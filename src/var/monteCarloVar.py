import numpy as np
import pandas as pd


def computeMonteCarloVaR(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    alpha: float = 0.99,
    nSim: int = 10000
) -> pd.DataFrame:
    df = df.copy()

    mu = df[returnCol].mean()
    sigma = df[returnCol].std()

    simulatedReturns = np.random.normal(mu, sigma, nSim)
    varValue = np.quantile(simulatedReturns, 1 - alpha)

    df[f"varMC_{int(alpha*100)}"] = varValue

    return df
