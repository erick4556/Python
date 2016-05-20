Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mi_lista=["Python","C++","C","Java","Ruby"]
>>> for lenguaje in mi_lista: #Por cada lenguaje en mi lista.
... 	print(lenguaje) #Imprimir lenguaje.
... 
Python
C++
C
Java
Ruby
>>> for edad in range(10, 18):
... 	print("Tu edad es : ",edad)
... 
Tu edad es :  10
Tu edad es :  11
Tu edad es :  12
Tu edad es :  13
Tu edad es :  14
Tu edad es :  15
Tu edad es :  16
Tu edad es :  17
>>> tabla =[1,2,3,4,5,6,7,8,9,10]
>>> multi=int(input("¿Que tabla de multiplicar deseas? "))
¿Que tabla de multiplicar deseas? 8
>>> for numero in tabla:
... 	print(multi, "x", numero, "=", multi*numero)
... 
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
>>> 