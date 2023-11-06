import numpy as np

import matplotlib.pyplot as plt

#np.linspace(startpoint,endpoint,number of points)
t=np.linspace(0,5,6)
print(t)

x=np.zeros(len(t))
y=np.zeros(len(t))

for i in range(len(t)):
    x[i]=5*t[i] - 0.006*t[i]**3
    y[i]=2*t[i] + 0.275*t[i]**2

print(np.polyfit(x,y,2,full=True))

#coeff=np.polyfit(x,y,degree)

coeff=np.polyfit(x,y,1)

#f=coeff[0]*x + coeff[1] ------ for deg 1
#f=coeff[0]*x**2 + coeff[1]*x + coeff[2] ------ for deg 2
#f=coeff[0]*x**3 + coeff[1]*x**2 + coeff[2]*x + coeff[3] ------ for deg 3

f=np.poly1d(coeff)

xnew=np.linspace(x[0],x[-1],50)
ynew=f(xnew)
plt.plot(x,y,"r*")
print(xnew)
plt.plot(xnew,ynew)
plt.show()
