from math import e
def wien(x):
    return 3*(1-e**(-x))-x 

def wien_der(x):
    return 3*(e**(-x))-1


