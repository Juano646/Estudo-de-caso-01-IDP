from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def l1(x):
    return 0.4 * x 

def f(x):
    return (-0.02 * x**2 )+ (0.4 *x)

def l2(x):
    return -0.8 * x + 18

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

plt.xlim([-3, 33])  
plt.ylim([-7, 3])  

plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')

plt.legend(["L1(x)","f(x)", "L2(x)"]) 

plt.title("Montanha russa -> m1 = 0.4 -> m2 = -0.8")



plt.show()