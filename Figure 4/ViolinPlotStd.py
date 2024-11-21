import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None, 'display.width', 500, 'display.max_rows', None)
# mypath = '~/PycharmProjects/pythonProject/'

drupdate = pd.read_csv('Daily_Return_Update.csv')
sector = pd.read_csv("Company information_update.csv", index_col=0)
sector = pd.DataFrame(sector["Sector"])

drsec = pd.merge(sector, drupdate, on="Ticker", how="left") # merge sector categorisation
drsec = drsec.iloc[:, 1:] # remove the ticker column, cannot aggregate
drsec = drsec.groupby("Sector").agg("std")
temp = drsec.T

median_values = temp.median() # Need to sort the violin plot from smallest the largest median values
median_values = median_values.sort_values()
median_values = median_values.reset_index()
median_values['Median'] = median_values.iloc[:,1]
median_values = median_values [['Sector','Median']]


drsec1 = pd.merge(median_values, drsec, on='Sector', how='left') # sort the violin plot from smallest the largest median values
drsec1 = drsec1.drop(columns=['Median'])
drsec1 = drsec1.set_index(['Sector'])
drsec1 = drsec1.T

plt.figure(figsize=(8, 6)) # Create the violin plot
sns.violinplot(data=drsec1, palette="Greens")
plt.xlabel('Sector')
plt.xticks(rotation=30, horizontalalignment='right')
plt.ylabel('Daily Return Volatility')
plt.title('HK Daily Return Volatility 2023')
plt.subplots_adjust(bottom=0.3)

plt.savefig('HK_Daily_Return_Volatility_2023.png', bbox_inches='tight',dpi=300)

plt.show()

