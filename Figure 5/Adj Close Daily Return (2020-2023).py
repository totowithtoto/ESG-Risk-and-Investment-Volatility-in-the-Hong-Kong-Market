import pandas as pd

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)

import numpy as np
import pandas as pd
import yfinance as yf


dataframes = []
url = "https://query2.finance.yahoo.com/v1/finance/esgChart?symbol="
start = "2019-12-01"
end = "2023-12-31"
year = np.arange(2020,2024)
number3 = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0010.HK', '0011.HK', '0012.HK', '0016.HK', '0017.HK', '0019.HK', '0020.HK', '0023.HK', '0027.HK', '0066.HK', '0083.HK', '0101.HK', '0135.HK', '0144.HK', '0151.HK', '0168.HK', '0175.HK', '0177.HK', '0257.HK', '0267.HK', '0270.HK', '0288.HK', '0291.HK', '0293.HK', '0317.HK', '0322.HK', '0338.HK', '0347.HK', '0358.HK', '0371.HK', '0384.HK', '0386.HK', '0388.HK', '0390.HK', '0392.HK', '0489.HK', '0525.HK', '0551.HK', '0656.HK', '0659.HK', '0669.HK', '0670.HK', '0688.HK', '0696.HK', '0700.HK', '0728.HK', '0753.HK', '0762.HK', '0763.HK', '0836.HK', '0857.HK', '0883.HK', '0902.HK', '0914.HK', '0916.HK', '0939.HK', '0941.HK', '0945.HK', '0960.HK', '0966.HK', '0981.HK', '0992.HK', '0998.HK', '1033.HK', '1038.HK', '1044.HK', '1055.HK', '1071.HK', '1088.HK', '1093.HK', '1099.HK', '1109.HK', '1113.HK', '1114.HK', '1128.HK', '1171.HK', '1177.HK', '1186.HK', '1193.HK', '1211.HK', '1288.HK', '1299.HK', '1336.HK', '1339.HK', '1359.HK', '1398.HK', '1576.HK', '1618.HK', '1766.HK', '1800.HK', '1816.HK', '1898.HK', '1919.HK', '1928.HK', '1972.HK', '1988.HK', '2007.HK', '2018.HK', '2020.HK', '2039.HK', '2066.HK', '2196.HK', '2202.HK', '2238.HK', '2282.HK', '2313.HK', '2318.HK', '2319.HK', '2328.HK', '2333.HK', '2338.HK', '2378.HK', '2388.HK', '2600.HK', '2601.HK', '2607.HK', '2628.HK', '2638.HK', '2688.HK', '2689.HK', '2727.HK', '2799.HK', '2866.HK', '2883.HK', '2888.HK', '2899.HK', '3311.HK', '3328.HK', '3333.HK', '3618.HK', '3898.HK', '3968.HK', '3988.HK', '4332.HK', '4333.HK', '4335.HK', '4336.HK', '4337.HK', '4338.HK', '6030.HK', '6808.HK', '6818.HK', '6823.HK', '6837.HK', '6881.HK', '6886.HK', '9618.HK', '9888.HK', '9901.HK', '9961.HK', '9988.HK', '9999.HK']

for y in year:
    AllDays = []
    AllDays = pd.DataFrame(AllDays)
    for ticker in number3:
        try:
            Oneticker = yf.download(ticker, start=start, end=end)
            Oneticker = Oneticker.ffill()
            Oneticker = pd.DataFrame(Oneticker)
            Oneticker["Return"] = Oneticker[['Adj Close']].pct_change()
            Oneticker = Oneticker[f"{y}-01-01":f"{y}-12-31"]
            Oneticker = Oneticker.rename(columns={"Return": ticker})
            Oneticker = Oneticker[[ticker]]
            Oneticker = Oneticker.T
            Oneticker.index.name = 'Ticker'
            if Oneticker.index != 0:
                AllDays = pd.concat([AllDays, Oneticker], ignore_index=False)

        except Exception:
            pass
    # print(AllDays)
    AllDays.to_csv(f"Daily_Return{y}.csv", sep=',')




