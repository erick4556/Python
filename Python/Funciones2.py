Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def cuadrado(num):
... 	"Muestra el cuadrado de un numero"
... 	print(num*num)
... 
>>> cuadrado(2)
4
>>> cuadrado(7)
49
>>> def cuadrado2():
... 	"""Imprime el cuadrado  de numero ingresado"""
... 	n=int(input("Ingrese un numero : "))
... 	cuadrado(n)
... 
>>> cuadrado2()
Ingrese un numero : 9
81
>>> #Aqui llame la función cuadrado para calcular el cuadrado de un numeor que ingrese..
... 
>>> print(cuadrado2())
Ingrese un numero : 3
9
None
>>> def cuadrado3_return():
... 	"""Retorna el cuadrado de un numero"
... 	"
... 	""
... 	cuadrado de un numero"""
... 	n=int(input('Ingrese un numero : '))
... 	return n* n
... 
>>> cuad = cuadrado3_return()
Ingrese un numero : 4
>>> print(cuad)
16
>>> 