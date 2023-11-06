import numpy as np

l = 0
i = 1
x = []
y = []
while i<np.inf:
    l_old = l
    l+=(1/(i**4))
    if l_old == l:
        break
    x.append(i)
    y.append(l)
    i+=1
    
print(l)
import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()
