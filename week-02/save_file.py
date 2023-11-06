import numpy as np

data = np.loadtxt('x.dat')
print(data)
np.savetxt('y.dat',data,fmt="%0.3f")
