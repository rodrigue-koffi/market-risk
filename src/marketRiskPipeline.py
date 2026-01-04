from data.loadData import loadMarketData
from data.returns import computeLogReturns
from volatility.historicalVol import computeHistoricalVol
from volatility.garchVol import computeGarchVol

filePath = "XAU_1d_data.csv"

df = loadMarketData(filePath)
df = computeLogReturns(df)
df = computeHistoricalVol(df)
df = computeGarchVol(df)
