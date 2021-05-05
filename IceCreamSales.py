import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf

"""
The file Quarter_Sales.csv contains ice cream sales data for each quarter from 2006 till 2020.
Using auto-correlation techniques, predict the sales for Q1 of 2020.
Your code should print the summary of the linear model and the prediction.
Don't show any charts.
"""

data = pd.read_csv('./Quarter_Sales.csv')

# Your code starts after this line

plot_pacf(data['Sales'])

s = 'Sales'
shift = [1, 3, 4, 6, 8, 11, 18]
S = data[s]
s1 = S.shift(periods=1)
s3 = S.shift(periods=3)
s4 = S.shift(periods=4)
s6 = S.shift(periods=6)
s8 = S.shift(periods=8)
s11 = S.shift(periods=11)
s18 = S.shift(periods=18)
predictor = pd.DataFrame({'s4': s4, 's6': s6, 's18': s18, })
Y = S[18:]
X = predictor[18:]
model = sm.OLS(Y, X)
print(model.fit().summary())
t = S.size
period = pd.DataFrame({'s4': [S[t - 4]], 's6': [S[t - 6]], 's18': [S[t - 18]]})
print(round(model.fit().predict(period), 2))

# Your code ends before this line
