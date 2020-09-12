import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import differential_evolution
df = pd.read_csv("output/result_matching.csv")

y_data = np.array((df['time']))
x_data = np.array((df['edges']))

# And plot it

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)

############################################################
# Now fit a simple sine function to the data
def test_func(x, a, b):
    print("a " +str(a))
    print("b " +str(b))
    print("x " + str(x))
    return (x**(a/b))

params, params_covariance = optimize.curve_fit(test_func, x_data, y_data,
                                               p0=[1,1])

print(params)

############################################################
# And plot the resulting curve on the data

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, test_func(x_data, params[0], params[1]),label='Fitted function')

plt.legend(loc='best')

plt.show()
