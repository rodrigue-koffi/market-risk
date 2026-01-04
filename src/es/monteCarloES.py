import numpy as np
import pandas as pd


def computeMonteCarloES(
    df: pd.DataFrame,
    returnCol: str = "logReturn",
    alpha: float = 0.975,
    nSim: int = 10000
) -> pd.DataFrame:
    df = df.copy()

    mu = df[returnCol].mean()
    sigma = df[returnCol].std()

    simulatedReturns = np.random.normal(mu, sigma, nSim)
    varValue = np.quantile(simulatedReturns, 1 - alpha)
    esValue = simulatedReturns[simulatedReturns <= varValue].mean()

    df["esMC_97_5"] = esValue
    return df
