import pandas as pd
from pathlib import Path


def loadMarketData(fileName: str) -> pd.DataFrame:
    """
    Chargement des données de marché et normalisation des colonnes.
    """

    dataPath = Path(r"C:\Users\Asus\Desktop\market-risk\data") / fileName
    df = pd.read_csv(dataPath, sep=";")

    # 🔑 NORMALISATION UNIQUE
    df.columns = [c.strip().lower() for c in df.columns]

    # conversion date
    df["date"] = pd.to_datetime(df["date"])

    # tri chronologique
    df = df.sort_values("date").reset_index(drop=True)

    return df
