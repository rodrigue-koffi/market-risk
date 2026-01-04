import pandas as pd


def loadMarketData(filePath: str) -> pd.DataFrame:
    df = pd.read_csv(filePath)
    df.columns = [c.lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df
