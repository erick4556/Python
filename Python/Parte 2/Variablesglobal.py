#def palindromo():
	#nuevo=sentencia.replace(' ','') #Variables locales se usan dentro de una función.
	#return nuevo== nuevo[::-1] #regresa la cadena caracteres alrevés.

#sentencia='anita lava la tina' #Variables globales
#print(sentencia)
#resul=palindromo()
#print(sentencia)
#print(resul)


def valor_global():
	global variable_glob;
	variable_glob='Cambia valor'; #Variable local

def mostrar_global():
	print(variable_glob)


def crear_globa():
	global nueva_vari;
	nueva_vari="Esto es una variable global"


crear_globa()
print(nueva_vari)