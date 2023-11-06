def d_func(x,y):
    return -y

h = 0.01

y = 1
x = 0

yn = 10

while x<yn:
    x+=h
    y+=h*d_func(x,y) 
print(y)

