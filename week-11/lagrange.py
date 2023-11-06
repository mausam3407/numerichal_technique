import numpy as np
import matplotlib.pyplot as plt
x = 10  
val = 0
data = np.loadtxt("cos.dat")

arr = data[:,0] 
yarr = data[:,1] 
N = len(arr)
#print(arr)
#print(yarr)
for i in range(N-1):
    num = 1
    den = 1
    for j in range(N-1):
        if j != i:
            num*=(x-arr[j])
            den*=(arr[i]-arr[j])
    val += (num/den)*yarr[i]
    #print(val)
#np.savetxt("cos.dat", np.c_[arr, yarr])
print(val)

plt.plot(arr, yarr)
plt.plot([x],[val], 'r*')
plt.show()
