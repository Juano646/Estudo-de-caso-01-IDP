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
plt.plot(x, l1(x), color='red')

x = np.linspace(0, 3)
plt.plot(x, g(x), color='red')

x = np.linspace(3, 27)
plt.plot(x, q(x), color='red')

x = np.linspace(27, 30)
plt.plot(x, h(x), color='red')

x = np.linspace(30, 60)
plt.plot(x, l2(x), color='red')

def L1(x):
    return 0.8 * x

def F(x):
    return (-0.04 * (x**2)) + (0.8 * x)

def L2(x):
    return (-1.6 * x) + 36

x = np.linspace(-30, 0)
plt.plot(x, L1(x), color='green')

x = np.linspace(0, 30)
plt.plot(x, F(x), color='green')

x = np.linspace(30, 60)
plt.plot(x, L2(x), color='green')


plt.axvline(0, color='k')
plt.axhline(0, color='k')

plt.xlim([-5, 35])  
plt.ylim([-14, 6])  

plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')

plt.legend(["y(x) - Questão 5","", "", "", "", "y(x) - Questão 2", "", ""]) 

plt.title("Gráfico das funções da questões 2 e 5")



plt.show()