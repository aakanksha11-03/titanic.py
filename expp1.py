# part1

# Pre-built library file used for basic mathematical operation. 

import math

print ("square root", math.sqrt(14))
print("factorial", math.factorial(5))
print("power", math.pow(2, 3))
print("ceiling ", math.ceil(4.5))
print("floor", math.floor(4.5))
print("pi value", math.pi)
print("euler value ", math.e)


# b)Numpy Library used for numerical computing and array operations.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print("Array :", arr)
print("Mean of array :", np.mean(arr))
print("Sum : ", np.sum(arr))
print("Minimum value in array :", np.min(arr))
print("Maximum value in array :", np.max(arr))

matrix = np.array([[1, 2], [3, 4]])
print("Matrix :\n", matrix)
print("Transpose of matrix :\n", matrix.T)



# c)Matplotlib Library used for data visualization and plotting graphs.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple Line Graph")
plt.show()



# d)seaborn Library used for data visualization and plotting graphs.

import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 30 , 40, 50]

sns.histplot(data)
plt.title("Seaborn Histogram")
plt.show()



# e)SciPy Library used for scientific and technical computing.

import scipy
from scipy import stats

data = [5, 10, 15, 20, 35]

print("Mean : ", stats.tmean(data))
print("Median : ", stats.scoreatpercentile(data, 50))
print("Mode : ", stats.mode(data))