import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 4.6, 1.6, 5.5, 3.4]).reshape((-1, 1))
y = np.array([0.7, -1, -0.2, -1.2, -0.1, 3.4, 0, 0.8, 3.7, 2])

model = LinearRegression()
model.fit(x,y)

#a task
print('B0: ', model.intercept_) 
print('B1: ', model.coef_)

b0 = model.intercept_ #a
b1 = model.coef_

y_pred = model.predict(x)
er_var = np.var(y - y_pred)
print('the error variance: ', er_var) #a

#b task
x_mean = np.mean(x) #x
s_2_x = np.sum((x - np.mean(x))**2)

var_b0 = er_var * (0.1 + (x_mean**2/s_2_x))
print('MLE of b0:', var_b0)

var_b1 = er_var/s_2_x
print('MLE of b1:', var_b1)

#c task
cov = -(x_mean * er_var / s_2_x) #covariance
cor_bb = cov/(np.sqrt(var_b0 * var_b1)) #correlation
print('correlation:', cor_bb)


    

