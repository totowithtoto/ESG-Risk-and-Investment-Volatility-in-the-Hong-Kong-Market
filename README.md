# ESG Risk and Investment Volatility in the Hong Kong Market
## Abstract

This study examines the relationship between Environmental, Social, and Governance (ESG) performance and stock price volatility in the Hong Kong market from 2020 to 2023. 

Leveraging Python for data collection and analysis, we utilized the Yahoo Finance API to gather stock price data and Morningstar ESG risk scores. Data cleaning techniques, including handling missing values and outlier detection, were applied using Pandas for efficient data manipulation and organization.

We analyze companies listed on the Hong Kong Stock Exchange, using Morningstar ESG risk scores as the independent variable and share price volatility as the dependent variable. Our multilinear regression analysis reveals substantial correlations (R² > 40%) across sectors, particularly in Consumer Defensive, Communication Services, and Utilities sector. Recent regulatory changes have positively influenced ESG performance amongst Hong Kong listed companies. 

This study underscores the importance of sector-specific analyses and regulatory impacts, providing insights for policymakers and corporations in integrating ESG considerations into financial decision-making.

## Key Findings

### Observation 1. ESG risk scores are higher in non-service sectors, environmental risk scores contribute the most.

Analysis indicates that non-service sectors have higher ESG risk scores, particularly in Energy and Utilities, reflecting their vulnerability to environmental regulations for transitioning into more sustainable practices.

<div align="center">
  <img src="Figure%201/Sector_Distribution.png" alt="Sector Distribution" width="400"/>
</div>

<div align="center">
  <img src="Figure%202/Sector_Average_ESG_Score.png" alt="Sector Average ESG Score" width="400"/>
</div>

### Observation 2. New regulation sees improved ESG performance in Hong Kong.

A downward trend in ESG risk scores from 2020 to 2023 suggests improved ESG management in response to regulatory changes. This decline suggests that companies are increasingly adopting sustainable practices and effectively addressing ESG challenges. The social score remains the largest component of the overall risk score, highlighting that firms may struggle with managing social risks or face persistent challenges in this area.


<div align="center">
  <img src="Figure%203/Trends in ESG Risk Scores from 2020 to 2023 in HK.png" alt="Trends ESG Risk Score" width="400"/>
</div>

A snapshot of the most recent share prices reveals that most sectors exhibit differing levels of volatility. . Healthcare and Financial Services sectors show relatively low volatility, The Technology and Consumer Cyclical sectors demonstrate the highest volatility ranges, suggesting that these sectors are more sensitive to external factors such as market trends, innovation, and changes in consumer demand.

<div align="center">
  <img src="Figure%204/HK_Daily_Return_Volatility_2023.png" alt="Trends ESG Risk Score" width="400"/>
</div>


### Observation 3: ESG risk score is a statistically significant predictor of share price volatility of the Consumer Defensive, Communication Services and Utilities sector.

<table style="margin: auto; border: none;">
  <tr>
    <td style="text-align: center;">
      <img src="Figure%205/Correlation coefficient Industry to ESG Risk Score(2020).png" alt="Image 1" width="500"/>
    </td>
    <td style="text-align: center;">
      <img src="Figure%205/Correlation coefficient Industry to ESG Risk Score(2021).png" alt="Image 2" width="500"/>
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">
      <img src="Figure%205/Correlation coefficient Industry to ESG Risk Score(2022).png" alt="Image 3" width="500"/>
    </td>
    <td style="text-align: center;">
      <img src="Figure%205/Correlation coefficient Industry to ESG Risk Score(2023).png" alt="Image 4" width="500"/>
    </td>
  </tr>
</table>

The multilinear regression analysis conducted reveals mixed insights into the relationship between ESG risk scores and share price volatility across sectors. Notably, the Utilities sector shows a consistent positive correlation, while the Consumer Defensive sector exhibits a negative correlation, both with high statistical significance (p<0.05). Multilinear regression analysis identifies seven sectors with significant results, highlighting that the Consumer Defensive, Communication Services, and Utilities sectors are key areas of focus, exhibiting R² values greater than 40%.

The findings support the hypothesis that companies with lower ESG risk scores, indicating better ESG performance, tend to have stronger internal controls, leading to reduced stock price volatility and greater investor confidence. However, some unexpected negative correlations suggest that increased ESG risk scores may coincide with lower volatility, potentially due to market inefficiencies or risk aversion among investors.

Overall, while ESG practices can enhance financial outcomes, their effects vary by industry, necessitating a deeper examination of company-specific sustainability actions for insights into operational efficiency and risk management.

<div align="center">
  <img src="Figure%206/Multi Linear Model Stats Result.png" alt="Multi Linear Model Stats Result" width="800"/>
</div>

## Data Collection
Data for 150 companies on the Hong Kong Stock Exchange was collected from yfinance api through python, data compiled and cleaned using pandas library, while all graphs created using matplotlib, seaborn library. Focusing on:

### Price Volatility: Measured as the standard deviation of daily stock price changes.
### ESG Risk Scores: Sourced from Morningstar, reflecting a company's ESG risk exposure and management effectiveness.
### Control Variables: Includes leverage (total debt/invested capital), profitability (return on invested capital), and company size (number of employees).

## Conclusion
This study highlights the nuanced relationship between ESG performance and investment volatility across sectors. While ESG practices can enhance risk management, their effects vary by industry. Understanding these dynamics is essential for investors and policymakers as they navigate the complexities of integrating ESG considerations into financial strategies.
