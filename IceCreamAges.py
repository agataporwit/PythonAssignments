import pandas as pd
import statistics as st
import numpy as np
from scipy import stats

# The file ages.csv contains the ages of 100 random customers that came to the store during the past year.
# Assuming the ages are normally distributed,
# calculate the probability that a person
# older than 40 will come to the store. Print the result rounded to two decimals.

data = pd.read_csv("./ages.csv")

age = data["Age"]
max_age = max(age)
age_avg = st.mean(age)
age_std = np.std(age)
a1 = stats.norm.cdf(max_age, loc=age_avg, scale=age_std) - stats.norm.cdf(41, loc=age_avg, scale=age_std)
print(round(a1, 2))
# Your code ends before this line
