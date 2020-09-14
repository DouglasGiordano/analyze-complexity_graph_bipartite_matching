import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import curve_fit

df = pd.read_csv("output/result_matching.csv")

y_data = np.array((df['edges']))
x_data = np.array((df['time']))

# And plot it

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)

def func(x, a, b):
    #return a * np.exp(b * x)
    return a*x + b

params = curve_fit(func, x_data, y_data)

[a, b] = params[0]

# And plot the resulting curve on the data
plt.scatter(x_data, y_data, label='Data')
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, func(x_data, a, b),label='Fitted function')

plt.legend(loc='best')

plt.show()
