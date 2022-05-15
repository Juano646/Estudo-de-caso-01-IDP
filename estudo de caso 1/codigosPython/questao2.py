from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def L1(x):
    return 0.8 * x

def f(x):
    return (-0.04 * (x**2)) + (0.8 * x)

def L2(x):
    return (-1.6 * x) + 36


x = np.linspace(-30, 0)
plt.plot(x, L1(x))

x = np.linspace(0, 30)
plt.plot(x, f(x))

x = np.linspace(30, 60)
plt.plot(x, L2(x))

plt.scatter(0, 0, color="black")
plt.scatter(30, -12, color="black")

plt.axvline(0, color='k')
plt.axhline(0, color='k')

plt.xlim([-5, 35])  
plt.ylim([-14, 6])  

plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')

plt.legend(["L1(x)", "f(x)", "L2(x)"]) 

plt.title("Montanha russa")

plt.show()

