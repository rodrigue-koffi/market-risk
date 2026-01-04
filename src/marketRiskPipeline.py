from data.loadData import loadMarketData
from data.returns import computeLogReturns

from volatility.historicalVol import computeHistoricalVol
from volatility.garchVol import computeGarchVol

from var.parametricVar import computeParametricVaR
from var.historicalVar import computeHistoricalVaR
from var.monteCarloVar import computeMonteCarloVaR

from es.historicalES import computeHistoricalES
from es.monteCarloES import computeMonteCarloES

from backtesting.kupiecTest import kupiecTest
from backtesting.trafficLight import trafficLight

from stress.stressScenarios import stressReturns


def goMarketRiskPipeline(filePath: str,alphaVar: float = 0.99,alphaEs: float = 0.975):
    """
    pipeline Market Risk :
    """

    # Chargement des données
    filePath = "XAU_1d_data.csv"
    df = loadMarketData(filePath)


    # Rendements
    df = computeLogReturns(df)

    # Volatilité
    df = computeHistoricalVol(df)
    df = computeGarchVol(df)

    # VaR
    df = computeParametricVaR(df, alpha=alphaVar)
    df = computeHistoricalVaR(df, alpha=alphaVar)
    df = computeMonteCarloVaR(df, alpha=alphaVar)

    # Expected Shortfall
    df = computeHistoricalES(df, alpha=alphaVar)
    df = computeMonteCarloES(df, alpha=alphaEs)

    # Backtesting VaR
    backtestResult = kupiecTest(
        df,
        varCol="varHist_99",
        alpha=alphaVar
    )

    traffic = trafficLight(backtestResult["exceptions"])

    # Stress testing
    dfStress = stressReturns(df)

    return {
        "data": df,
        "backtest": backtestResult,
        "trafficLight": traffic,
        "stressData": dfStress
    }


def main():
    filePath = "XAU_1d_data.csv"
    goMarketRiskPipeline(filePath)


if __name__ == "__main__":
    main()
