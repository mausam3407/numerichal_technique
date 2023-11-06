import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(0, 2*math.pi,100)
sine = np.sin(x)
coef = np.polyfit(x, sine, 5)
f = np.poly1d(coef)
graph = f(x)
plt.plot(x,sine, "r*")
plt.plot(x, graph)
plt.show()
