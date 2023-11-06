import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("polat.dat")
x = data[:,0]
y = data[:,1]
xi = np.linspace(0, np.pi/2, 10)
yi = []
for i in xi:
    j = np.argmax(x>i)
    k = j - 1
    m = (y[j]-y[k])/(x[j]-x[k])
    c = y[j] - (m*x[j])
    yi.append((m*i)+c)
print(yi)

plt.plot(x,y)
plt.plot(xi,yi, "r*")
plt.show()
        


