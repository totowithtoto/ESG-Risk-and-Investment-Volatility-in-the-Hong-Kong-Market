import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)

myPath = "ESGhisdata\\"
df = pd.read_csv(myPath+'Company information_update.csv', index_col=0)
tickerList = np.array(df.index)

df = df.drop(columns=["Industry", "Number of Employees"])

dataframes = []
dataframes = pd.DataFrame(dataframes)

for ticker in tickerList:
    df1 = pd.read_csv(myPath+f"{ticker}ESG.csv", index_col=0)
    df1 = df1.tail(1)
    df1["timestamp"] = ticker
    df1 = df1.rename(columns={"timestamp": "Ticker",
                              "esgScore": "ESG Risk Score",
                              "governanceScore": "G Score",
                              "environmentScore": "E Score",
                              "socialScore": "S Score"})
    df1 = df1.set_index(df1["Ticker"])
    df1 = df1.drop(columns=["Ticker"])

    if df1.index != 0:
        dataframes = pd.concat([dataframes, df1], ignore_index=False)
        print(dataframes)

df = df.merge(dataframes, how="left", on="Ticker")
print(df)

df.to_csv(myPath + "ESG_Data.csv", sep=',')

