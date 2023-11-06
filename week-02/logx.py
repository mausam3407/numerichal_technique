import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.dat')
print(data)

log_dat = np.log(data)
print(log_dat)

plt.plot(data, log_dat)
plt.show()

