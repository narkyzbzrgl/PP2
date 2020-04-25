import pandas as pd
import  statistics
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = {'Small': [810, 820, 820, 835, 835, 835],
     'Medium': [840, 840, 840, 845, 855, 850],
      'Large': [785, 790, 785, 760, 760, 770]}

data = pd.DataFrame(data = df)
data

Y1 = data.Small
Y2 = data.Medium
Y3 = data.Large

s = np.mean(Y1)
m = np.mean(Y2)
l = np.mean(Y3)
print(s, m, l)

x = np.sum((Y1 - s)**2)
y = np.sum((Y2 - m)**2)
z = np.sum((Y3 - l)**2)
print(x, y, z)

M = (s + m +l)/3
M

S = ((6*(s - M)**2) + (6*(m - M)**2) + (6*(l - M)**2))  #sum of sq. between samp
dbf = 3 - 1  #between samples df
c = S/dbf  #mean sq between samples
print(S, c)

drf = 18 - 3   #residuals df
Z = x + y + z   #sum of sq. residuals
v = Z/drf   #mean sq residuals
print(Z, v)

F = c/v   #F-statistic
F


import pandas as pd
import csv

with open('5.csv', newline = '') as f:
    reader = csv.reader(f, delimiter = ';')
    for row in reader:
        print(row)
        
data = pd.read_csv('5.csv', delimiter = ';')

df = pd.DataFrame(data)
data

#H0: m1 = m2 = m3
#H1: m1 != m2 != m3
print("""According to the ANOVA table we get the p-value calculated for the F-statistic is approximately 
      0, that's less than 5% level of significance, that's why null hypothesis is false and we reject null
      hypothesis ar 5% of level significance""")
print("Average all 3 sizes of vehicles don't produce the same level of noise")