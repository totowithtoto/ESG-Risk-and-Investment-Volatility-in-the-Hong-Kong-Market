import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
import statsmodels.api as sm

warnings.filterwarnings("ignore")
mypath = "/Users/marcolam/Downloads/"
folderPath = "/Users/marcolam/PycharmProjects/pythonProject/MLRegression Volatility in HK stocks by sector/"
pd.set_option('display.max_columns', None, 'display.width', 500, 'display.max_rows', None)


# sector_choice = 'Utilities' # Enter Sector Name to print results from sector, for a list of sector names see sector list below.

df_number_employee = pd.read_csv(folderPath + 'company_Information_Update.csv')

df_daily_return_ESG2023 = pd.read_csv(folderPath + 'ESG Risk Score vs Volatility2023.csv')
df_daily_return_ESG2022 = pd.read_csv(folderPath + 'ESG Risk Score vs Volatility2022.csv')
df_daily_return_ESG2021 = pd.read_csv(folderPath + 'ESG Risk Score vs Volatility2021.csv')
df_daily_return_ESG2020 = pd.read_csv(folderPath + 'ESG Risk Score vs Volatility2020.csv')

df_fin_ratio2023 = pd.read_excel(folderPath + 'FinRatio2023.xlsx')
df_fin_ratio2022 = pd.read_excel(folderPath + 'FinRatio2022.xlsx')
df_fin_ratio2021 = pd.read_excel(folderPath + 'FinRatio2021.xlsx')
df_fin_ratio2020 = pd.read_excel(folderPath + 'FinRatio2020.xlsx')

ticker_and_sector = df_daily_return_ESG2023.iloc[:, :2] # Get ticker list and sector as finratio does not have sector information to merge
# print(ticker_and_sector)
fin_ratio_list = df_fin_ratio2023,df_fin_ratio2022,df_fin_ratio2021,df_fin_ratio2020
daily_return_list = df_daily_return_ESG2023,df_daily_return_ESG2022,df_daily_return_ESG2021,df_daily_return_ESG2020

df_number_employee = df_number_employee.drop(columns = ['Sector','Industry'],axis = 1)

temp = pd.DataFrame()
for i,j in zip(fin_ratio_list, daily_return_list): # Creating training and testing dataset
    j['Total ESG Risk Score'] = j['Total ESG Risk Score']/100 # Making ESG score the appx same "power" ie from 23 to 0.23 which is similar to our other ratios
    i = i.drop(columns=list(i.iloc[:, 1:5].columns)) # Just taking the row : ticker, total debt to invs and ptax to invsmt
    i = pd.merge(i, ticker_and_sector, on='Ticker', how='left') # merge to include sector
    i = pd.merge(i, df_number_employee, on='Ticker', how='left')  # merge to include employees
    i = pd.merge(i, j, on='Ticker', how='left')
    temp = pd.concat([temp, i], axis=0) # merge to include all years

data = temp.drop(columns=['Sector_y'])
data = data.rename(columns={'Sector_x': 'Sector', 'TotalDebttoInvmt': 'Debt to Capital', 'PtaxtoInvmt': 'Return on Invested Capital','Volatility of Stock Prices Standard deviation':'Volatility'})
# data.to_csv(folderPath + 'Training Data MultiLinearAnalysis All years All sectors.csv', sep = ',') # export datafile to csv
# print(data.head(1))

df = df_daily_return_ESG2020.groupby("Sector").agg(["count"])
sector = list(df.index) # get sector list
df5 = pd.DataFrame()

for sector in sector:
    sector_choice = f'{sector}' # Enter Sector Name to print results from sector, for a list of sector names see sector list below.
    data1 = data.loc[data['Sector'] == sector_choice]
    df2 = data1.drop(['Ticker','Sector'],axis = 1)
    df2 = df2.fillna(df2.mean()) # fill nan values with column mean

    for column in df2.columns:     # normalization
        df2[column] = df2[column] / df2[column].abs().max()

    X = df2[['Total ESG Risk Score','Debt to Capital', 'Return on Invested Capital','Number of Employees']]
    y = df2['Volatility']
    # X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 24) # (Sklearn)

    # reg_model = linear_model.LinearRegression()  # (Sklearn)
    # reg_model = LinearRegression().fit(X_train, y_train)  # (Sklearn)

    y_sm = y # (Stats Model)
    x_sm = sm.add_constant(X)
    est = sm.OLS(y_sm, x_sm).fit()

    # y_pred= reg_model.predict(X_test) # (Sklearn)
    # x_pred= reg_model.predict(X_train) # (Sklearn)

    # print("Prediction for test set: {}".format(y_pred)) # (Sklearn)

    # mae = mean_absolute_error(y_test, y_pred) # (Sklearn)
    # mse = mean_squared_error(y_test, y_pred) # (Sklearn)
    # r2 = r2_score(y_test, y_pred) # (Sklearn)

    print(f'Shape of {sector_choice} data is :{df2.shape}')
    print(est.summary())
    # print('Mean Absolute Error:', mae) # (Sklearn)
    # print('Mean Square Error:', mse) # (Sklearn)
    # print('Root Mean Square Error:', r2) # (Sklearn)

    # a = list(zip(X, reg_model.coef_)) # (Unused) Creating the equation label
    # label = 'y = '
    # for i,j in a:
    #     j = f'{j:.3f}'
    #     temp = '+('+str(j)+') '+str(i)+' '
    #     label = label+temp

    # npcoef = reg_model.coef_ # (sklearn) Creating a Dataframe running all sectors to include the R2 score, and each of the coefficient calculated
    # df4 = pd.DataFrame(a)
    # df4 = df4.T
    # df4.rename(columns=df4.iloc[0], inplace=True)
    # df4.drop(df4.index[0], inplace=True)
    # df4['Sector'] = sector
    # df4['R2'] = r2
    # df4 = df4.iloc[:, [4, 5, 0, 1, 2, 3]]
    # df5 = pd.concat([df5,df4])

    # if sector_choice == 'Utilities' or 'Consumer Defensive' or 'Communication Services':   # Correlation Heatmap
    #     ax = plt.axes()
    #     cmap = sns.diverging_palette(h_neg=15, h_pos=15, s=75, l=55, sep=40, as_cmap=True) # h_neg h pos set neg pos color, s is greyness, l is darkness, sep = increases the middle val range
    #     hm = sns.heatmap(df2.corr(), cmap=cmap,linecolor='black',linewidth=0.1,annot = True,vmin = -1,vmax = 1)
    #     ax.set_title(f'{sector_choice} Correlation Heatmap between variables')# Study on multicollinearity (the independent variables are not too highly correlated with each other) should be below 0.7
    #     props = {"rotation" : 30}
    #     plt.setp(ax.get_xticklabels(), **props)
    #     plt.show()
    #
    #     sns.distplot(df2['Volatility'],bins = 20).set_title('STD distribution') # Unused
    #     pp = sns.pairplot(df2, x_vars=['Total ESG Risk Score','Debt to Capital', 'Return on Invested Capital','Number of Employees'], y_vars='Volatility', height=4, kind='scatter').fig
    #     pp.suptitle(f'{sector_choice} Scatter Plot of Volatility to each Xi (independent variable)')
    #     plt.show()
    #
    #     reg_model_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred}) # Unused
    #     fig = sns.lmplot(data = reg_model_diff, x = 'Actual value', y = 'Predicted value').fig
    #     fig.suptitle(f'{sector_choice} Test Data vs Training Data')
    #     plt.show()
    #
    #     fig = sns.lmplot(data = data, x = 'Total ESG Risk Score', y = 'Volatility', ci = False,legend =False,line_kws={'color': 'red'}).fig # Unused
    #     fig.suptitle(f'{sector_choice} Multi Linear Regression Model Result', y = 0.98,size = 15)
    #     plt.legend(loc='lower right', labels=[f'{label}', f'R2: {r2}'])
    #     plt.show()


# df5.index = df5['Sector'] # (sklearn) df5 is the calculated coefficient
# df5 = df5.drop(columns = ['Sector'])
# df5 = df5.sort_values('R2',ascending=False)
# print(df5)
# df5.to_csv(folderPath+'MultiLinearRegression by sector results.csv', sep=',')