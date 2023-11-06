import numpy as np

arr = np.arange(100)
arr_log = np.log(arr)

arr = np.array([arr, arr_log])
print(arr)
np.savetxt("data.dat", arr, fmt="%0.8f")
