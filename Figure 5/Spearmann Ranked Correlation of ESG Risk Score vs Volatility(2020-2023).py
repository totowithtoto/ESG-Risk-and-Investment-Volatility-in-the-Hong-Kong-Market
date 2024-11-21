import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)
myPath = "ESGhisdata\\"
year = np.arange(2020,2024)

for y in year:
    esgRisk = pd.read_csv(f"ESG_Data{y}.csv",index_col=0)

    esgRisk = esgRisk.drop(columns=["G Score","S Score","E Score"])
    esgRisk = esgRisk.rename(columns={"ESG Risk Score": "Total ESG Risk Score"})
    print(esgRisk)
    stockPrices = pd.read_csv(f"Daily_Return{y}.csv",index_col=0)
    stockPrices["Volatility of Stock Prices Standard deviation"] = stockPrices.std(axis=1)
    stockPrices = stockPrices[["Volatility of Stock Prices Standard deviation"]]
    print(stockPrices)

    esgRisk = esgRisk.merge(stockPrices, how="left", on="Ticker").dropna()
    print(esgRisk)
    # esgRisk.to_csv(f"ESG Risk Score vs Volatility{y}.csv", sep=",")

    df3 = esgRisk.groupby("Sector")["Total ESG Risk Score"].agg(["count"])
    print(df3)
    valueCountforuniqueSectors = np.array(df3)
    totalvalueCountforuniqueSectors = valueCountforuniqueSectors.sum()
    sector = np.array(df3.index)
    print(sector)
    print(totalvalueCountforuniqueSectors)

    esgStandarddeviation = np.array(esgRisk["Volatility of Stock Prices Standard deviation"])
    esgRiskScore = np.array(esgRisk["Total ESG Risk Score"])

    dataFrame = []
    dataFrame = pd.DataFrame(dataFrame)

    for s in sector:
        bm = esgRisk.loc[esgRisk["Sector"] == s]
        corr, pval = sci.spearmanr(bm["Volatility of Stock Prices Standard deviation"],bm["Total ESG Risk Score"])
        corr1, pavl1 = sci.pearsonr(bm["Volatility of Stock Prices Standard deviation"],bm["Total ESG Risk Score"])
        bm = bm.groupby("Sector").agg('mean')
        bm["Spearman's correlation coefficient"] = corr
        bm["Spearman's P-value"] = pval
        bm["Pearson's correlation coefficient"] = corr1
        bm["Pearson's P-value"] = pavl1
        print(bm)
        if bm.index != 0:
            dataFrame = pd.concat([dataFrame, bm], ignore_index=False)
    dataFrame = dataFrame.merge(df3, how="left", on="Sector")
    print(dataFrame)
    dataFrame = dataFrame.drop(["Total ESG Risk Score", "Volatility of Stock Prices Standard deviation"],axis=1)

    corr, pval = sci.spearmanr(esgRisk["Volatility of Stock Prices Standard deviation"], esgRisk["Total ESG Risk Score"])
    corr1, pavl1 = sci.pearsonr(esgRisk["Volatility of Stock Prices Standard deviation"], esgRisk["Total ESG Risk Score"])

    index = ["Total"]
    total = pd.DataFrame(corr, columns=["Spearman's correlation coefficient"], index=index)
    total["Spearman's P-value"] = pval
    total["Pearson's correlation coefficient"] = corr1
    total["Pearson's P-value"] = pavl1
    total["count"] = totalvalueCountforuniqueSectors

    print(total)

    dataFrame = pd.concat([dataFrame, total], ignore_index=False)
    dataFrame.index.name = "Sector"

    print(dataFrame)

    dataFrame.to_csv(f"Spearman's correlation coefficient Industry to ESG Risk Score{y}.csv",sep=",")