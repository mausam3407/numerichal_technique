from math import e
def quad(x):
    return (x**2)-4

def wien(x):
    return (5*(1-(e**(-x))))-x


def bisect(f, a, b):
    while True:
        c = (a+b)/2
        if f(c) == 0:
            return c
        if f(c) > 0:
            b = c
        else:
            a = c

print(bisect(wien, 100,1))
print(bisect(quad, 100,-100))




