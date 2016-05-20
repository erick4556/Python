Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> resp="si"
>>> numero =0
>>> while resp == 'si':
... 	numero= int(input("Escriba un numero")) #Pedimos que escriba un numero
... 	if numero > 0:
... 		print("El numero es positivo")
... 	elif numero < 0:
... 		print ("El numero es negativo")
... 	else:
... 		print("El numero es igual a cero")
... 
Escriba un numero 9
El numero es positivo
Escriba un numero 0
El numero es igual a cero
Escriba un numero-5
El numero es negativo
Escriba un numero1
El numero es positivo
Escriba un numero5
El numero es positivo
Escriba un numero-6
El numero es negativo
Escriba un numero//
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '//'
>>> #Escribi // para que fuera un error y mi sacara del ciclo ya que era infinito..:
... 
>>> while resp == 'si':
... 	numero= int(input("Escriba un numero"))
... 	if numero > 0:
... 		print("El numero es positivo")
... 	elif numero < 0:
... 		print ("El numero es negativo")
... 	else:
... 		print("El numero es igual a cero")
...   File "<stdin>", line 2
    ... 	numero= int(input("Escriba un numero"))
      ^
IndentationError: expected an indented block
>>>   File "<stdin>", line 1
    ... 	if numero > 0:
                      ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    ... 		print("El numero es positivo")
              ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    ... 	elif numero < 0:
            ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    ... 		print ("El numero es negativo")
              ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    ... 	else:
            ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    ... 		print("El numero es igual a cero")
              ^
SyntaxError: invalid syntax
>>> 