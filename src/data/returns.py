import numpy as np
import pandas as pd


def computeLogReturns(
    df: pd.DataFrame,
    priceCol: str = "close"
) -> pd.DataFrame:
    """
    logarithmiques prix de clôture.
    """

    df = df.copy()

    if priceCol not in df.columns:
        raise ValueError(
            f"Colonne '{priceCol}' introuvable. Colonnes disponibles : {df.columns.tolist()}"
        )

    df["logReturn"] = np.log(df[priceCol] / df[priceCol].shift(1))
    df = df.dropna().reset_index(drop=True)

    return df
