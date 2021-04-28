import statsmodels.api as sm
import numpy as np
import pandas as pd
#agata<(O_O)>
df = pd.read_csv('./kc.csv')

# Your code starts after this line
area = df['GrLivArea']
salePrice = df['SalePrice']
area = sm.add_constant(area)
model = sm.OLS(salePrice, area)
result = model.fit()
# Your code ends before this line

print(result.params)

