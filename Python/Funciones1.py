Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def  mifuncion():
... 	"""Primera funcion en python
... 		imprime  dos mensajes"""
... 	print("Hola todos")
... 	print("Esta es mi primera funcion")
... 
>>> mifuncion()
Hola todos
Esta es mi primera funcion
>>> def  mifuncion():
... 	"Primera funcion
  File "<stdin>", line 2
    "Primera funcion
                   ^
SyntaxError: EOL while scanning string literal
>>> 	"Primera funcion"
  File "<stdin>", line 1
    "Primera funcion"
    ^
IndentationError: unexpected indent
>>> def mi_funcion2(cadena, numero):
... 	"""Escribe una cadena de texto
... 		El número  de veces que le asignemos a numero"""
... 	print(cadena * numero)
... 
>>> mi_funcion2("Holaa",4)#Indica el numeor de veces que imprimira la cadena...
HolaaHolaaHolaaHolaa
>>> def funcion_3(cadena, numero=3):
... 	"""Escribe una cadena de texto
... 		por default 4 veces"""
... 	print(cadena * numero)
... 
>>> funcion_3("Hola que tal")
Hola que talHola que talHola que tal
>>> funcion_3("Hola que tal", 10)
Hola que talHola que talHola que talHola que talHola que talHola que talHola que talHola que talHola que talHola que tal
>>>  