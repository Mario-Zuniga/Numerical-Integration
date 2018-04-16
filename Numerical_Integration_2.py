#Seccion 2 Integracion de una función desconocida

#Importacion de paquetes
from scipy import *
from numpy import *
from sympy import *

#Creamos el simbolo t para la funcion
t = Symbol('t')

#Declaramos la funcion
f = exp(-t)

#Rangos de la integracion
#Agregar .0 a los valores ayuda a evitar numeros complejos
a = 0.0
b = 3.0

#Valor de senal
h = 0.001

#Valores para calcular
w = [0.0]
y = [0.0]

#Valor de la posicion x en i
xi = []

#Generamos un arreglo que tiene el rango de la integracion + h
#y avanza en el numero h
xs = arange(a, b+h, h)

#Susituimos el primer valor del arreglo xs en la funcion t
x = [f.subs(t, xs[0])]

#Hacemos un valor stop para tener un rango en el ciclo loop
stop = len(xs)

#Hacemos un arreglo que tendra parametro del arreglo xs, con el fin de hacer los calculos
for cont in range(1, stop):

	#Subsituimos el valor de t con el valor cont para obtener los valores
	a = f.subs(t, xs[cont])

	#Agregamos el valor de val al arreglo x
	x.append(a)


#Hacemos un valor stop para tener un rango en el ciclo loop
stop2 = len(x)

#Creamos un ciclo for que empiece en 0 y llegue a 1 valor menos que el arreglo x
for i in range(0, stop2 - 1):

	#Agregamos el valor de x en xi
	xi.append(x[i])

	#Agregamos a w el valor calculado
	w.append(sum(y) * h)

	#Agregamos a y el valor calculado
	y.append((sum(xi) - 2.0 * sum(y) - sum(w)) * h)


#Senal de salida
g = (1.0/2.0) * t * (2.0-t) * exp(-t)

#Para hacer la sumatoria empezamos agregando a yt el valor de la funcion g evaluado con el valor 0 del arreglo xs
yt = g.subs(t, xs[0])

#Hacemos un arreglo que tendra parametro del arreglo xs, con el fin de hacer los calculos
for cont in range(1, stop):

	#Substituimos el valor actual de xs en la funcion g
	res = g.subs(t, xs[cont])
	
	#Agregamos el valor de res a yt
	yt.append(res)


#Imprimimos yt
print(yt)