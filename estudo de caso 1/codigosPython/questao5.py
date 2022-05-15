from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def l1(x):
    return 0.8 * x

def g(x):
    return (-0.0049382716049382715826 * (x**3)) + (0.8 * x)

def q(x):
    return (-0.044444444444444445598 * (x**2)) + (0.93333333333333333655 * x) - 0.13333333333333333655

def h(x):
    return (0.0049382716049382715809 * (x**3)) - (0.44444444444444444207 * (x**2)) + (11.733333333333333272 * x) - 97.333333333333332761

def l2(x):
    return -1.6 * x + 36

x = np.linspace(-30, 0)
plt.plot(x, l1(x))

x = np.linspace(0, 3)
plt.plot(x, g(x))

x = np.linspace(3, 27)
plt.plot(x, q(x))

x = np.linspace(27, 30)
plt.plot(x, h(x))

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
plt.ylim([-14, 6])  

plt.ylabel('Altura')
plt.xlabel('Distância')

#plt.legend(["L1(x)","g(x)", "q(x)", "h(x)", "L2(x)"]) 

plt.title("Gráfico das funções")



plt.show()