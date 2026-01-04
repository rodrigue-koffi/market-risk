from data.loadData import loadMarketData
from data.returns import computeLogReturns
from volatility.historicalVol import computeHistoricalVol
from volatility.garchVol import computeGarchVol

from var.parametricVar import computeParametricVaR
from var.historicalVar import computeHistoricalVaR
from var.monteCarloVar import computeMonteCarloVaR

filePath = "XAU_1d_data.csv"

df = loadMarketData(filePath)
df = computeLogReturns(df)
df = computeHistoricalVol(df)
df = computeGarchVol(df)

df = computeParametricVaR(df, alpha=0.99)
df = computeHistoricalVaR(df, alpha=0.99)
df = computeMonteCarloVaR(df, alpha=0.99)
