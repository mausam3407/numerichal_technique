import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(0, 2*math.pi,100)
sine = np.sin(x)
for i,val in enumerate(sine):
    if i%2==0:
        sine[i] = sine[i]*1.02
    else:
        sine[i] = sine[i]*0.98
np.savetxt("sin.dat", np.c_[x, sine], fmt = "%0.3f")
plt.plot(x, sine, "r*")
plt.show()
