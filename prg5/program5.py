import numpy as np
x = np.arange(21)
print("vector")
print(x)
print("i\n After changing the sign of the no.")
x[(x>=9)&(x<=15)]+=-1
print(x)