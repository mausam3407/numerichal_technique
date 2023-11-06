import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

gain = 3.1
input_vol = np.arange(1,1000,10)
output_vol = 3.1*input_vol

coef = np.polyfit(input_vol, output_vol, 1)
f = np.poly1d(coef)
graph = f(input_vol)
plt.plot(input_vol,output_vol, "r*")
plt.plot(input_vol, graph)
plt.show()
