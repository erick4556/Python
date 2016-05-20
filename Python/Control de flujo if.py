Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numero =3
>>> if numero > 0:
... 	print("Numero positivo")
... 
Numero positivo
>>> int num=4
  File "<stdin>", line 1
    int num=4
          ^
SyntaxError: invalid syntax
>>> num=4
>>> if num > 7:
... 	print("Numero es mayor")
... else:
... 	print('Numero es menor')
... 
Numero es menor
>>> na=3
>>> if na > 0:
... 	print('Numero mayor")
  File "<stdin>", line 2
    print('Numero mayor")
                        ^
SyntaxError: EOL while scanning string literal
>>> #Esto no se puede hacer
... 
>>> numero =0
>>> numero=0:
  File "<stdin>", line 1
    numero=0:
            ^
SyntaxError: invalid syntax
>>> numero=0
>>> if numero > 0:
... 	print("Numero es positivo")
... elif numero <0:
... 	print("numero es negativo")
... else:
... 	print("Numero es igual a cero")
... 
Numero es igual a cero
>>> al=4
>>> if al > 0:
... print("Numero bueno")
  File "<stdin>", line 2
    print("Numero bueno")
        ^
IndentationError: expected an indented block
>>> if al > 0:
... print("Numero bn")
  File "<stdin>", line 2
    print("Numero bn")
        ^
IndentationError: expected an indented block
>>> if al > 0:
... 	print("Numero")
... 
Numero
>>> 