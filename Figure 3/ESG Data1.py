import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)

myPath = "ESGhisdata\\"
df = pd.read_csv(myPath+'Company information_update.csv', index_col=0)
tickerList = np.array(df.index)
year = np.arange(2021,2025)
print(year)
df = df.drop(columns=["Industry", "Number of Employees"])

for y in year:
    dataframes = []
    dataframes = pd.DataFrame(dataframes)
    for ticker in tickerList:
        df1 = pd.read_csv(myPath+f"{ticker}ESG.csv", index_col=0)
        df1 = df1.loc[df1["timestamp"] < f"{y}-01-01"]
        df1 = df1.tail(1)

        df1["timestamp"] = ticker
        df1 = df1.rename(columns={"timestamp": "Ticker",
                              "esgScore": "ESG Risk Score",
                              "governanceScore": "G Score",
                              "environmentScore": "E Score",
                              "socialScore": "S Score"})
        df1 = df1.set_index(df1["Ticker"])
        df1 = df1.drop(columns=["Ticker"])

        dataframes = pd.concat([dataframes, df1], ignore_index=False)
    print(dataframes)
    dataframes.to_csv(myPath + f"ESG_Data{y-1}.csv", sep=',')
