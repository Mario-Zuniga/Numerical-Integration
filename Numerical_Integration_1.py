#Seccion 1 Metodo Simspon 3/8
#Importacion de paquetes
from scipy import *
from numpy import *
from sympy import *

#Declaramos t como simbolo de la formula dada
t = Symbol('t')

#Declaramos T como 1 de manera temporal para evitar error
T = 1

#Declaramos a y b en los rangos de la integracion
a = 0.0
b = 0.5

#Escribimos la formula
f = (1/T) * ((10*exp(-t/T) * sin((2*pi*t) /T))**2)

#Declaramos n en 2 representando 2 secciones
n = 2

#Declaramos formula de h y valores
h = (b - a) / n

#Valores para los residuos
s1 = 0
s2 = 0
s3 = 0

#Generamos un arreglo que tiene el rango de la integracion + h
#y avanza en el numero h
xs = arange(a, b+h, h)

#Substituimos el valor de t con el valor que esta en el arreglo xs
ys = [f.subs(t, xs[0])]

#Hacemos un valor stop para tener un rango en el ciclo loop
stop = len(xs)

#Hacemos un arreglo que tendra parametro del arreglo xs, con el fin de hacer los calculos
for cont in range(1, stop):

	#Subsituimos el valor de t con el valor cont para obtener los valores
	val = f.subs(t, xs[cont])

	#Agregamos el valor de val al arreglo ys
	ys.append(val)

#Hacemos un valor stop para tener un rango en el ciclo loop
stop2 = len(ys)

#Ciclo para obtener los residuos para la sumatoria de Simspon
for cont in range(1, stop2):

	#Si el valor tiene residuo 1 lo suma
	if cont % 3 == 1:
		s1 = s1 + ys[cont]

	#Si el valor tiene residuo 2 lo suma
	if cont % 3 == 2:
		s2 = s2 + ys[cont]

	#Si el valor tiene residuo 0 lo suma
	if cont % 3 == 0:
		s3 = s3 + ys[cont]

#Hacemos la sumatoria de los valores
result = (3.0/8.0) * h * (ys[0] + 3*s1 + 3*s2 + 2*s3 + ys[n])

#Imprimimos el resultado
print(result)