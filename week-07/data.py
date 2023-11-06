import numpy as np

x = np.linspace(0,np.pi/2, 50)
y = np.cos(x)

np.savetxt("polat.dat", np.c_[x,y], fmt = "%3f")
