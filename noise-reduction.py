import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import random

# Parameter
ymin = -2
ymax = 7

# Real function
def f1(e):
    return 5/(1 + math.pow(math.e, -e))

# Function with noise
def f2(e):  
    return f1(e) + noise[math.floor(e / step)] 

# Where to evaluate f1
step = 0.1
x = list(np.arange(-25, 25, step))

# Noise added to f1 in order to obtain f2
noise_range = 0.2
noise = list(map(lambda e: random.uniform(-noise_range, noise_range)*(20 if random.uniform(0,1) < 0.1 else 1), x))

# Plot f1
ax = plt.figure().gca()
ax.set_ylim([ymin,ymax])
ax.plot(x, list(map(lambda e: f1(e), x)))
plt.title("Original signal")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("1")
plt.show()

# Plot f2
ax = plt.figure().gca()
ax.set_ylim([ymin,ymax])
ax.plot(x, list(map(lambda e: f2(e), x)))
plt.title("Signal with noise")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("2")
plt.show()

# Reduce noise by applying moving average applied to function with noise
def f3(e):
    epsilon = 2
    neighborhood_e = list(filter(lambda ee: ee >= e - epsilon and ee <= e + epsilon, x))
    f2_neighborhood_e = list(map(lambda ee: f2(ee), neighborhood_e))
    return np.mean(f2_neighborhood_e)

# Plot f3
ax = plt.figure().gca()
ax.set_ylim([ymin,ymax])
ax.plot(x, list(map(lambda e: f3(e), x)) )
plt.title("Signal after moving average")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("3")
plt.show()

def reject_outliers(f, m = 2):
    return f[abs(f - np.mean(f)) < m * np.std(f)]

# Improved attempt to reconstruct the real function based on removing outlier and moving average
def f4(e):
    epsilon = 2
    neighborhood_e = list(filter(lambda ee: ee >= e - epsilon and ee <= e + epsilon, x))
    f2_neighborhood_e = list(map(lambda ee: f2(ee), neighborhood_e))
    f2_neighborhood_e_no_outliers = reject_outliers(np.array(f2_neighborhood_e))
    return np.mean(f2_neighborhood_e_no_outliers)

# Plot f4
ax = plt.figure().gca()
ax.set_ylim([ymin,ymax])
ax.plot(x, list(map(lambda e: f4(e), x)) )
plt.title("Signal after removing outliers and moving average")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("4")
plt.show()

