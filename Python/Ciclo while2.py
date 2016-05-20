Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> resp="si"
>>> numero=0;
>>> while resp=='si':
... 	numero = int(input("Ingrese un numero : "))
... 	if numero > 0:
... 		print("El numero ingresado es positivo")
... 	elif numero < 0:
... 		print("Numero ingresado es negativo")
... 	else:
... 		print("EL numero ingresado es cero")
... 	resp= input("¿Quieres ingresar otro numero: escribe si o no")
... 
Ingrese un numero : 8
El numero ingresado es positivo
¿Quieres ingresar otro numero: escribe si o no si
>>>