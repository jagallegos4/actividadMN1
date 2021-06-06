#se importa lalibreria matplotlib
import matplotlib.pyplot as plt

#se importa libreria numpy
import numpy as np


def f(x):
    return x**2-x+1

def g(x): #se defina la funcion g(x)
    return 2/(x-1)

x=np.linspace(-5,5,100) #se define el dominio de la funcion y el numero de puntos a grficar

plt.plot(x,f(x), label='f(x)')
plt.plot(x,g(x), label='g(x)')
plt.grid()
plt.legend(loc=1)
plt.show()
