import numpy as np
from matplotlib import pyplot as plt


def biseccion(f,a,b,tol,nmax):
    for i in range(1,nmax):
        if np.sign(f(a)) == np.sign(f(b)):
            print("La raíz no está en el intervalo especificado")
            return
        m = (a + b)/2
        if abs(f(m)) < tol:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        else:
            b = m
            i += i

f=lambda x: 2**x-(1/3)
r=biseccion(f,-2,-1,0.0001,100)

print("Raiz de la ecuacion: ",r)

x=np.linspace(-10,1,100) #se define el dominio de la funcion y el numero de puntos a grficar

plt.plot(x,f(x), label='f(x)')
plt.grid()
plt.legend(loc=1)
plt.show()
