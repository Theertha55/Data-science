import numpy as np
from numpy.distutils.conv_template import header

x = np.arange(16).reshape(4,4)
print("Array:")
print(x)
header= 'c1 c2 c3 c4'
np.savetxt("array.txt",x,header = header )
print("\n After loading,content of the txt file:")
print(np.loadtxt("array.txt"))