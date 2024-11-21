import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

pd.set_option('display.max_columns', None, 'display.width', 200, 'display.max_rows', None)
mypath = '~/PycharmProjects/pythonProject/' # Change directory path if needed

years = np.arange(2020, 2024)
dataframes = []

for year in years:
    esg = pd.read_csv(mypath + f'ESG_Data{year}.csv', index_col=0)
    esg1 = pd.read_csv(mypath + f'ESG_Data{year}.csv', index_col=0)

    esg = esg.drop(columns=["G Score", "E Score", "S Score"])
    esg1 = esg1.drop(columns=["ESG Risk Score"])
    esg1 = esg1[esg1["G Score"] != 0]  # Keep only rows where G Score is not 0

    esg_mean = esg.mean().to_frame().T # Calculate means and create DataFrames
    esg1_mean = esg1.mean().to_frame().T

    esg_mean["Year"] = year
    esg1_mean["Year"] = year
    esg_mean.set_index("Year", inplace=True)
    esg1_mean.set_index("Year", inplace=True)
    dataframes.append(esg_mean)
    dataframes.append(esg1_mean)

result = pd.concat(dataframes, axis=0, ignore_index=False)
result = result.groupby(result.index).mean()  # Combine mean values for duplicate years
result.to_csv(mypath+ "Average Score of yearly ESG Data.csv", sep=',')

esg_risk = result.drop(columns=["G Score", "E Score", "S Score"],axis=1) # Linegraph with two axis
esg_risk = esg_risk.reset_index()
esg_risk = pd.melt(esg_risk, ["Year"])

risk = result.drop(columns=["ESG Risk Score"], axis=1)
risk = risk.reset_index()
risk = pd.melt(risk, ["Year"])

fig, ax1 = plt.subplots()
sns.set(style="ticks")
colors = cm.Greens(np.linspace(0.3, 1, 3))
sns.lineplot(data=esg_risk, x='Year', y='value', label="ESG Risk Score",marker='o', markersize=8, ax=ax1, color="green")

ax2 = ax1.twinx()
# sns.lineplot(data=risk, x='Year', y='value', hue='variable', linestyle='dashed', marker='o', markersize=5, ax=ax2)
sns.lineplot(data=risk[risk['variable'] == 'E Score'], x='Year', y='value',
             linestyle='dashed', ax=ax2, color=colors[0])
sns.lineplot(data=risk[risk['variable'] == 'S Score'], x='Year', y='value',
             linestyle='dashed', ax=ax2, color=colors[1])
sns.lineplot(data=risk[risk['variable'] == 'G Score'], x='Year', y='value',
             linestyle='dashed', ax=ax2, color=colors[2])
ax1.set_xticks(esg_risk["Year"], esg_risk["Year"])
ax1.set_xlabel("Year")
ax1.set_ylabel("ESG Risk Score")
ax2.set_ylabel("Risk Score")
ax2.set_title("Trends in ESG Risk Scores from 2020 to 2023 in HK")
ax2.legend([ax1.get_lines()[0], ax2.get_lines()[0], ax2.get_lines()[1], ax2.get_lines()[2]],
["ESG Risk Score","E Score", "S Score", "G Score"], loc="upper right")

plt.savefig('Trends in ESG Risk Scores from 2020 to 2023 in HK.png', bbox_inches='tight',dpi=300)
plt.show()
