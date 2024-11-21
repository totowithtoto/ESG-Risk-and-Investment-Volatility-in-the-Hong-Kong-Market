import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd


# myPath = "ESGhisdata\\"
# data = pd.read_csv(myPath+"Sectors ESG Risk.csv", index_col=0) # Define the data
data = pd.read_csv("Sectors ESG Risk.csv", index_col=0) # Define the data
sectors = np.array(data.index)
esg_risk_mean = np.array(data["Total ESG Risk Mean"])
environment_risk_mean = np.array(data["E Risk Mean"])
governance_risk_mean = np.array(data["G Risk Mean"])
social_risk_mean = np.array(data["S Risk Mean"])
esg_risk_mean = environment_risk_mean + governance_risk_mean + social_risk_mean

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))
ind = [x for x, _ in enumerate(sectors)]
colors = cm.Greens(np.linspace(0.3, 1, 3))

ax1 = ax.bar(ind, governance_risk_mean, width=0.8, label='Mean of Governance Risk Score', color=colors[0], bottom= social_risk_mean+environment_risk_mean )
ax2 = ax.bar(ind, social_risk_mean, width=0.8, label='Mean of Social Risk Score', color=colors[1], bottom= environment_risk_mean)
ax3 = ax.bar(ind, environment_risk_mean , width=0.8, label='Mean of Environment Risk Score', color=colors[2])

# Set the x-axis ticks and labels
ax.set_xticks(ind, sectors)
ax.set_xticklabels(sectors, rotation=30)

# Add labels and title
ax.set_xlabel('Sector', fontsize=20)
ax.set_ylabel('Average ESG Risk Score', fontsize=16)
ax.set(ylim=(0,55))
ax.set_title('Average ESG Risk Score by Sector', fontsize=30,pad=20)
ax.legend(fontsize=12, loc='upper left')
plt.subplots_adjust(bottom=0.25)

y_offset = -1.4
for bar in ax.patches:
  ax.text(
      bar.get_x() + bar.get_width() / 2,
      bar.get_height() + bar.get_y()+y_offset,
      round(bar.get_height(),2),
      ha='center',
      color='white',
      size=8.5
  )

y_offset = 1
for i, esg in enumerate(esg_risk_mean):
  ax.text(i, esg + y_offset, round(esg,1), ha='center',
          weight='bold',color="black",size=12)

plt.savefig('Sector_Average_ESG_Score.png', bbox_inches='tight',dpi=300)
plt.show()

