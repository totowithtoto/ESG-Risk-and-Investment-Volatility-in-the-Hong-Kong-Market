import pandas as pd

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)

myPath = "ESGhisdata\\"
df = pd.read_csv(myPath+'ESG_Data.csv', index_col=0)
df1 = df.T
df1 = df1.drop(["0293.HK","0317.HK","0347.HK","0525.HK",
                    "0551.HK","0659.HK","0762.HK","0883.HK",
                    "0981.HK","1033.HK","1128.HK","1186.HK",
                    "1800.HK","2039.HK","2066.HK","2282.HK"], axis=1)
df1 = df1.T

esg = df[["Sector","ESG Risk Score"]]
esg = esg.groupby("Sector")["ESG Risk Score"].agg(['mean', 'std', 'min', 'max'])
esg = esg.rename(columns={"mean": "Total ESG Risk Mean",
                          "std": "Total ESG Risk Standard Deviation",
                          "min": "Total ESG Risk Min",
                          "max": "Total ESG Risk Max"})

e = df1[["Sector","E Score"]]
e = e.groupby("Sector")["E Score"].agg(['mean', 'std', 'min', 'max'])
e = e.rename(columns={"mean": "E Risk Mean",
                          "std": "E Risk Standard Deviation",
                          "min": "E Risk Min",
                          "max": "E Risk Max"})

s = df1[["Sector","S Score"]]
s = s.groupby("Sector")["S Score"].agg(['mean', 'std', 'min', 'max'])
s = s.rename(columns={"mean": "S Risk Mean",
                          "std": "S Risk Standard Deviation",
                          "min": "S Risk Min",
                          "max": "S Risk Max"})

g = df1[["Sector","G Score"]]
g = g.groupby("Sector")["G Score"].agg(['mean', 'std', 'min', 'max'])
g = g.rename(columns={"mean": "G Risk Mean",
                          "std": "G Risk Standard Deviation",
                          "min": "G Risk Min",
                          "max": "G Risk Max"})

esg = esg.merge(e, how="left", on="Sector")
esg = esg.merge(s, how="left", on="Sector")
esg = esg.merge(g, how="left", on="Sector")

esg.sort_values("Total ESG Risk Mean", axis=0, ascending=True,
                 inplace=True, na_position='last')
print(esg)

esg.to_csv(myPath + "Sectors ESG Risk.csv", sep=',')
