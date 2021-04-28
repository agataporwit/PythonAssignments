import pandas as pd
import statistics as st
import numpy as np
from scipy import stats
#agata <(@_@)>

data = pd.read_csv("./weight-height-v2.csv")

#Calculate the min, max, median, average, and 10th percentile Height


# Your code starts after this line

heights = data["Height"]
min_height = min(heights)
max_height = max(heights)
median_height = st.median(heights)
average_height = st.mean(heights)
percentile_height = np.percentile(heights, 0.9)

# Your code ends before this line


print("Min Height: " + str(round(min_height, 2)))
print("Max Height: " + str(round(max_height, 2)))
print("Average Height: " + str(round(average_height, 2)))
print("Median Height: " + str(round(median_height, 2)))
print("10th Percentile Height: " + str(round(percentile_height, 2)))

#Assuming that the data is normally distributed answer the following questions

# Q1 - What is the minimum height for a door that allows 83% of 

#      the people to go through without bending?

# Q2 - What is the minimum height for a door that allows 95% of 

#      the people to go through without bending?

# Q3 - What percentage of people are taller than 66 inches?

# Q4 - What percentage of people are shorter than 66 inches?

# Q5 - What percentage of people are between 60 and 70 inches?


# Your code starts after this line

# following what we did in class including some of the naming
heights_sd = np.std(heights)
a1 = stats.norm.ppf(0.83, loc=average_height, scale=heights_sd)
a2 = stats.norm.ppf(0.95, loc=average_height, scale=heights_sd)
a3 = stats.norm.cdf(max_height, loc=average_height, scale=heights_sd) - stats.norm.cdf(66, loc=average_height,scale=heights_sd)
a4 = stats.norm.cdf(66, loc=average_height, scale=heights_sd)
a5 = stats.norm.cdf(70, loc=average_height, scale=heights_sd)-stats.norm.cdf(60, loc =average_height, scale=heights_sd)


# Your code ends before this line


print("Q1: " + str(round(a1, 2)))
print("Q2: " + str(round(a2, 2)))
print("Q3: " + str(round(a3, 2)))
print("Q4: " + str(round(a4, 2)))
print("Q5: " + str(round(a5, 2)))

