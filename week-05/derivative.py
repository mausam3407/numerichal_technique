import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sin.dat")

x = data[:,0]
sin = data[:,1]
der = np.zeros(len(sin)-1)
x_new = np.zeros(len(sin)-1)
cos = np.zeros(len(sin)-1)
per_error = np.zeros(len(sin)-1)
for i in range(1, len(x)):
    x_new[i-1] = (x[i]+x[i-1])/2
    cos[i-1] = np.cos(x_new[i-1])
    der[i-1] = (sin[i]-sin[i-1])/(x[i]-x[i-1])
    per_error[i-1] = (abs(der[i-1]-cos[i-1])/cos[i-1])*100
    
plt.plot(x, sin, label = "Sine")
plt.plot(x_new, der, label = "Derivative")
plt.plot(x_new, cos, label = "Cosine")
plt.plot(x_new, per_error, label = "Error")
plt.title("First derivative of Sin")
plt.legend()
plt.show()

second_derivative = np.zeros(len(x_new)-1)
x_new1 = np.zeros(len(x_new)-1)
second_derivative_actual = np.zeros(len(x_new)-1)
per_error1 = np.zeros(len(x_new)-1)
for i in range(1, len(x_new)):
    x_new1[i-1] = (x_new[i]+x_new[i-1])/2
    second_derivative_actual[i-1] = -np.sin(x_new1[i-1])
    second_derivative[i-1] = (der[i]-der[i-1])/(x_new[i]-x_new[i-1])
    per_error1[i-1] = (abs(second_derivative[i-1] - second_derivative_actual[i-1])/second_derivative_actual[i-1])*100

plt.plot(x_new1, second_derivative, "r*", label = "Numerically calculated Derivative")
plt.plot(x_new1, second_derivative_actual, label = "Actual Derivative")
plt.plot(x_new1, per_error1, label = "percentage error")
plt.legend()
plt.title("2nd derivative of sin")
plt.show()


plt.plot(x, sin, color="green", label = "Sine Function")
plt.plot(x_new, der, color="blue", label = "First derivative")
plt.plot(x_new1, second_derivative, color="yellow", label = "2nd derivative")
plt.legend()
plt.title("First and 2nd derivative combined")
plt.show()

"""
final_x = np.concatenate([x,x_new,x_new1])
final_der = np.concatenate([sin, der, second_derivative])
final_der1 = np.concatenate([sin, cos, second_derivative_actual])
plt.plot(final_x, final_der, "b*", label = "First and 2nd derivatives combined")
plt.plot(final_x, final_der1, label = "First and 2nd actual derivatives combined")
plt.legend()
plt.title("All combined")
plt.show()
#print(x_new)
"""

