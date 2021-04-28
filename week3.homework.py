import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf
# agata <(o_O)>
# Read the data file sales_quarter.csv. When using your computer
data = pd.read_csv('./sales_quarter.csv')
# Calculate the Partial Auto-Correlation in the data in the sales column
plot_pacf(data['sales'])
pyplot.show()  # comment out for HW

# Use the lags from the previous part to create a linear model that predicts
# future sales based on past sales
# Name the shifted variables s1, s2, ..., sn, where s1 is the one with the smallest lag
# s2 the one with the second smallest and so on.
# Summarize the model and use it to predict the sales for the next time period in the set.

s = 'sales'
shift = [1, 2, 11]
S = data[s]
s1 = S.shift(periods=1)
s2 = S.shift(periods=2)
s12 = S.shift(periods=11)
predictor = pd.DataFrame({'s1': s1, 's2': s2})

Y = S[11:]
X = predictor[11:]
model = sm.OLS(Y, X)
print(model.fit().summary())

t = S.size
period = ({'s1': [S[t - 1]], 's2': [S[t - 2]]})
print([model.fit().predict(period)])
# Use the model to predict the sales in the next quarter rounded to two decimal places
nextQuarter = model.fit().predict(period)
print(round(nextQuarter, 2))
