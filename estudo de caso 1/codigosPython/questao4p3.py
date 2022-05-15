import funcoesQuestao4 as fQ
from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

# y(x)
x = np.linspace(-30, 0)
plt.plot(x, fQ.yl1(x), color='red')

x = np.linspace(0, 30)
plt.plot(x, fQ.yf(x), color='red')

x = np.linspace(30, 60)
plt.plot(x, fQ.yl2(x), color='red')

# g(x)
x = np.linspace(-30, 0)
plt.plot(x, fQ.gl1(x), color='blue')

x = np.linspace(0, 30)
plt.plot(x, fQ.gf(x), color='blue')

x = np.linspace(30, 60)
plt.plot(x, fQ.gl2(x), color='blue')

# h(x)
x = np.linspace(-30, 0)
plt.plot(x, fQ.hl1(x), color='green')

x = np.linspace(0, 30)
plt.plot(x, fQ.hf(x), color='green')

x = np.linspace(30, 60)
plt.plot(x, fQ.hl2(x), color='green')


"""
plt.scatter(0, 0, color="black")
plt.scatter(3, 2.2666667, color="black")
plt.scatter(27, -7.333334, color="black")
plt.scatter(30, -12, color="black")
plt.xlim([-3, 33])  
plt.ylim([-7, 3])  

"""
plt.xlim([-6, 33])  
plt.ylim([-15, 7]) 

plt.axvline(0, color='k')
plt.axhline(0, color='k')


plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')

plt.legend(["y(x) -L1(x)","y(x) - f(x)", "y(x) - L2(x)", "g(x) - L1(x)", "g(x) - f(x)", "g(x) - L2(x)", "h(x) - L1(x)", "h(x) - f(x)", "h(x) - L2(x)"]) 

plt.title("Comparação das três curvas")



plt.show()