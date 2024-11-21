import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None, 'display.width', 500, 'display.max_rows', None)

df = pd.read_csv('Company information_update.csv')
df1 = df.groupby('Sector')["Ticker"].count().reset_index()
df1 = df1.sort_values(by='Ticker', ascending=False)

pastel_colors = sns.light_palette("Green",n_colors=len(df1["Ticker"]))[::-1] # Create a green gradient for the wedge color from dark to light
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(df1["Ticker"], labels=df1['Sector'], autopct='%1.2f%%', colors=pastel_colors,
        textprops={'fontsize': 13},
        pctdistance=0.75,
        labeldistance=1.1,
        radius = 0.3)

sizes = df1["Ticker"]  # Create list of only top 5 largest label
labels = df1['Sector'].tolist()
top_sectors = df1.head(5)
display_labels = []
for sector in labels:
    if sector in top_sectors['Sector'].values:
        display_labels.append(sector)
    else:
        display_labels.append('')

for i, autotext in enumerate(autotexts): # Only label the autolabels of the 5 largest sector
    if df1['Sector'].iloc[i] not in top_sectors['Sector'].values:
        autotext.set_text('')

plt.axis('equal')
plt.title('Sector distribution in HKEX', fontsize=20, pad=20)
plt.savefig('Sector_Distribution.png', bbox_inches='tight',dpi=300)
plt.show()
