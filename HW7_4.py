import pandas as pd
import  statistics
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import scipy.stats as ss

df = {'X': [105.7, 102, 93.5, 110.8],
      'Y': [30.3, 54.4, 25, 36.4]}

data = pd.DataFrame(data=df)
data

x = data.X
y = data.Y

M = (np.sum(x))/4  #mean of x
print('mean of x:', M)

s1 = 10*y
s1

S = np.sum((x-M)**2)  #sum of sq. between samp
dbf = 4 - 1  #between samples df
c = S/dbf  #mean sq between samples
print('sum of squares between sample:', S, 'mean square between samples:', c)

drf = 40 - 4   #residuals df
dtf = 39
Z = np.sum(s1)   #sum of sq. residuals
v = Z/drf   #mean sq residuals
print(Z, v)

F = c/v   #F-statistic
print('F-statistic:', F)

b = ss.f.ppf(1 - 0.05, dbf, dtf)
b

print("""Acoording to the estimated values we can see that 5% significance level is 2.85  is less than calculated 
     value of test statistic , that's why we don't reject null hypothesis at 5% significance""")
print("senior classes at all four high schools would perform equally well on this examnation")
