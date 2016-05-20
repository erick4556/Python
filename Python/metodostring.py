cadena = input("Escriba una cadena de texto : ")

#Obtiene longitud de la cade
print("\nEl numeor de caracteres de la cadena es : ",len(cadena))


if cadena.isalpha():
	print("\nLa cadena es alfabetica")


# Devuelve True Si la cadena contiene solo números
if cadena.isdigit():
	print("\nLa cadena es numérica ")


# Convierte la cadena  a mayúscula

print("\nEn mayúscula : ",cadena.upper())

#Convierte la cadena a minúsculas
print("\nEn minúscula : ",cadena.lower())

#Convierte de mayúscula a minúscula y viceversa
print("\nInvierte mayúscula y minúscula : ",cadena.swapcase())

#Reemplaza
print("\nReemplaza a por x :",cadena.replace("a","x"))

#Devuelve la posición del caracter solicitado (la primer insidencia)
print("\nLa posición del caracter solicitado es : ",cadena.find("a"))

#Devuelve la posición del caracter solicitado (la ultima insidencia)
print("\nLa posición del caracter solicitado es : ",cadena.rfind("a"))

#Crea una lista de sub-cadenas de la  cadena
print("Lista de sub-cadenas : ",cadena.split("a"))





