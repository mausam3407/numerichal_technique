from math import e
def nr(func, der, x):
    eps = 1e-5
    rem = func(x)
    #print(rem)
    while abs(rem)>eps:
        x = x - (func(x)/der(x))
        rem = func(x)
        #print(x)
    return x
from wien import wien, wien_der
root = nr(wien, wien_der,12)
print(root)
