import matplotlib.pyplot as plt

def d_func_2(x,y,v):
    return -0.5*y

def d_func_1(x,y,v):
    return v

h = 0.01
x = 0
v = 1
y = 0
yn = 60
x1 = []
y1 = []
z1 = []
n1 = []
while x<yn:
    x+=h
    y+=h*d_func_1(x,y,v)
    v+=h*d_func_2(x,y,v)
    x1.append(x)
    y1.append(y)
    z1.append(v)
    n1.append((y**2+v**2)/2)
print(y)
print(v)

plt.plot(x1,y1)
plt.plot(x1, z1, 'r*')
plt.plot(x1, n1, 'b+')
plt.show()

