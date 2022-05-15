from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def l1(x):
    return 1.2*x

def f(x):
    return -0.06 * (x**2) + 1.2 * x

def l2(x):
    return -2.4 * x + 54

x = np.linspace(-30, 0)
plt.plot(x, l1(x))

x = np.linspace(0, 30)
plt.plot(x, f(x))

x = np.linspace(30, 60)
plt.plot(x, l2(x))


"""
plt.scatter(0, 0, color="black")
plt.scatter(3, 2.2666667, color="black")
plt.scatter(27, -7.333334, color="black")
plt.scatter(30, -12, color="black")
"""

plt.axvline(0, color='k')
plt.axhline(0, color='k')

plt.xlim([-5, 35])  
plt.ylim([-25, 7])  

plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')

plt.legend(["L1(x)","f(x)", "L2(x)"]) 

plt.title("Montanha russa - m1 = 1.2 - m2 = -2.4")



plt.show()