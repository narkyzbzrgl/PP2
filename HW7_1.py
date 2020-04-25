import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]).reshape((-1, 1))
y = np.array([40,41,43,42,44,42,43,42]) #giving the data

model = LinearRegression().fit(x, y) #fitting the model

r_sq = model.score(x, y) #coef of determination
print('coefficient of determination in (a):', r_sq)
print('intercept in a(b0):', model.intercept_)
print('slope in a(b1):', model.coef_)
y_pred = model.predict(x)
print('predicted response in a:', y_pred, sep='\n')

import matplotlib.pyplot as plt 
plt.scatter(x, y)#dots
plt.plot(x, y_pred, color = 'purple')#1st regression as line

poly = PolynomialFeatures(degree = 2)#creating new polynomial function
x_ = poly.fit_transform(x)#squared x
poly.fit(x_, y)

model2 = LinearRegression()
model2.fit(x_, y)

plt.plot(x, model2.predict(x_), color = 'green')#parabola
plt.show()

r_sq2 = model2.score(x_, y) #coef of determination
print('coefficient of determination in b:', r_sq2)
print('intercept(b0) in b:', model2.intercept_)
print('slope(b1) in b:', model2.coef_)
y_pred2 = model2.predict(x_)
print('predicted response in b:', y_pred2, sep='\n')




