#se llama al paquete matrix de numpy
from numpy import matrix

#se llama al paquete linalg de numpy
from numpy.linalg import linalg

#se declara la matriz de 2x2 con el metodo matrix
a=matrix([[5,-4],[-3,2]])

#se imprime la matriz
print("Matriz a invertir")
print(a)

#se declara una variable para invertir la matriz con el metodo inv
invertida=(linalg.inv(a))

#se imprime la matriz invertida
print("Matriz invertida")
print(invertida)