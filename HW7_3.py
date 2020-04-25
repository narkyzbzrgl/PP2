import numpy as np
from scipy import stats

x = np.array([0.3, 1.4, 1.0, -0.3, -0.2, 1.0, 2.0, -1.0, -0.7, 0.7]).reshape((-1, 1))
y = np.array([0.4, 0.9, 0.4, -0.3, 0.3, 0.8, 0.7, -0.4, -0.2, 0.7])
n = 10
c = 0.7

from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x, y)

intercept = model.intercept_
print('Intercept:', intercept)

slope = model.coef_
print('Slope:', slope)

s2_x = np.sum((x - np.mean(x))**2)

s2 = 0
for i in range (10):
    s2 += (y[i] - intercept - slope * x[i])**2

sigma = np.sqrt(1/(n-2) * s2) # error variance without square

print('Task a')
t_statistic = (intercept - c) / (sigma * np.sqrt(1 / n + np.mean(x)**2 / s2_x)) # U0
print("t-statistics: ", t_statistic)
p_value = stats.t.sf(np.abs(t_statistic), n-2)*2
print('p value: ', p_value)

print('Since the p-value is greater then the significance level 0.05, then we accept the null hypothesis')

print('Task b')
c = 0
t_statistic = (intercept - c) / (sigma * np.sqrt(1 / n + np.mean(x)**2 / s2_x)) # U0
print("t-statistics: ", t_statistic)

p_value = stats.t.sf(np.abs(t_statistic), n-2)*2
print('p value: ', p_value)

print('Since the p-value is less then the significance level 0.05, then we reject the null hypothesis')

print('Task e')
c0 = 5
c1 = 1
c2 = 4
t_quantile = stats.t.ppf(0.95, 8)
#print(t_quantile)
upper_bound = (c0 * intercept - c1 * slope + c2) + (sigma * np.sqrt(c0**2/n + (((c0 * np.mean(x) + c1))**2)/s2_x) * t_quantile)
lower_bound = (c0 * intercept - c1 * slope + c2) - (sigma * np.sqrt(c0**2/n + (((c0 * np.mean(x) + c1))**2)/s2_x) * t_quantile)

print('Confidence interval: ', lower_bound, ' ', upper_bound)

print('Task f')
x1 = 0.42
t_quantile = stats.t.ppf(0.99, 8)
#print(t_quantile)
upper_bound = (intercept + slope * x1) + (sigma * np.sqrt(1/n + (((x1 - np.mean(x)))**2)/s2_x) * t_quantile)
lower_bound = (intercept + slope * x1) - (sigma * np.sqrt(1/n + (((x1 - np.mean(x)))**2)/s2_x) * t_quantile)

print('Confidence interval: ', lower_bound, ' ', upper_bound)

print('Task c')

f_quantile = stats.f.ppf(0.95, 2, 8)
print(f_quantile)

def reggression_line(x0):
    return intercept + slope * x0

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(x, reggression_line(x), color='green')
plt.show()

#print('Confidence interval: ', lower_bound, ' ', upper_bound)

print('Task d')

def upper_bound_function(x0):
    return (intercept + slope * x0) + (sigma * np.sqrt(2 * f_quantile * (0.1 + ((x0 - np.mean(x))**2)/s2_x)))

def lower_bound_function(x0):
    return (intercept + slope * x0) - (sigma * np.sqrt(2 * f_quantile * (0.1 + ((x0 - np.mean(x))**2)/s2_x)))

plt.scatter(x, y)
plt.plot(x, reggression_line(x), color='green')

print(upper_bound_function(x))
print(lower_bound_function(x))

plt.plot(x, upper_bound_function(x), color = 'red', lw  = 2)
plt.plot(x, lower_bound_function(x), color = 'red', lw = 2)

x = np.array([0.3, 1.4, 1.0, -0.3, -0.2, 1.0, 2.0, -1.0, -0.7, 0.7])
plt.fill_between(x, reggression_line(x), upper_bound_function(x), color = 'lightblue', alpha = 0.4, hatch = '-')

plt.show()
