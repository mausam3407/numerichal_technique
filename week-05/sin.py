import numpy as np

x = np.linspace(0, np.pi/2, 1000)
sine = np.sin(x)

#for i in range(len(sine)):
#    if i%2:
#        sine[i] = sine[i]*0.98
#    else:
#        sine[i] = sine[i]*1.03

np.savetxt("sin.dat",np.c_[x,sine],)
