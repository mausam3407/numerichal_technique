
def func(x):
    return x**2-4

def der(x):
    return 2*x

x = -3.1 
#x = 3.1
eps = 1e-5
rem = func(-3.1)

while abs(rem)>eps:
    x = x - (func(x)/der(x))
    rem = func(x)
    #print(x)
    #print(rem)

print(x)
