import pandas as pd
from arch import arch_model


def computeGarchVol(
    df: pd.DataFrame,
    returnCol: str = "logReturn"
) -> pd.DataFrame:
    df = df.copy()

    model = arch_model(
        df[returnCol] * 100,
        mean="Zero",
        vol="Garch",
        p=1,
        q=1,
        dist="normal"
    )

    res = model.fit(disp="off")
    df["garchVol"] = res.conditional_volatility / 100

    return df
