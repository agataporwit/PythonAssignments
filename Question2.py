import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from statsmodels.graphics import tsaplots

from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

data = pd.read_csv('./Ingredients.csv')

# Your code starts after this line

flavorMenu = [199, 154, 125, 88, 132, 130, 133, 160, 161, 123, 125, 138, 176, 209, 172, 161, 147, 142, 185, 158]

ingrid1 = [44, 26, 11, 12, 14, 5, 30, 7, 44, 5, 34, 12, 17, 42, 38, 26, 2, 6, 27, 34]
ingrid2 = [16, 38, 3, 5, 32, 40, 5, 30, 37, 4, 43, 32, 41, 13, 31, 25, 38, 32, 43, 3]
ingrid3 = [34, 39, 34, 3, 30, 20, 11, 48, 18, 33, 5, 13, 36, 32, 45, 8, 21, 27, 32, 8]
ingrid4 = [48, 32, 13, 11, 17, 36, 47, 33, 3, 44, 20, 36, 45, 45, 4, 19, 6, 42, 28, 29]
ingrid5 = [45, 7, 47, 34, 28, 15, 13, 14, 20, 31, 15, 41, 13, 34, 32, 41, 39, 28, 43, 41]
ingrid6 = [12, 12, 17, 23, 11, 14, 27, 28, 39, 6, 8, 4, 24, 43, 22, 42, 41, 7, 12, 43]

flavorMenu = [199, 154, 125, 88, 132, 130, 133, 160, 161, 123, 125, 138, 176, 209, 172, 161, 147, 142, 185, 158]

dataFrameForFlavors = pd.DataFrame(
    {"ingrid1": ingrid1, "ingrid2": ingrid2, "ingrid3": ingrid3, "ingrid4": ingrid4, "ingrid5": ingrid5,
     "ingrid6": ingrid6})
X = dataFrameForFlavors
model = sm.OLS(flavorMenu, X)
newFlavorResult = model.fit()

print(newFlavorResult.summary())

numbersForPredictedFlavor = [47, 31, 48, 18, 49, 43]
print(round(float(newFlavorResult.predict(numbersForPredictedFlavor)), 2))

sales = [57400, 40800, 27800, 32200, 26000, 38800, 66000, 50100, 51300, 37000, 31600, 31900, 57800, 82900, 34700, 59300,
         42000, 36800, 38400, 69500]


dataFrameForSales = pd.DataFrame(
    {"ingrid1": ingrid1, "ingrid2": ingrid2, "ingrid4": ingrid4, "ingrid6": ingrid6,
     })

Y = dataFrameForSales
Y = sm.add_constant(Y)
model = sm.OLS(sales, Y)

salesResults = model.fit()

print(salesResults.summary())

numbersForPredictedSales = [1, 47, 31, 18, 43]
print(round(float(salesResults.predict(numbersForPredictedSales)), 2))

# Your code ends before this line
