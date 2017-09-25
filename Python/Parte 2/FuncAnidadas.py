def crear_func(n,m):#Funcíon Closure
	def val():
		return n>0 and m>0
	
	return val


nuev=crear_func(10,7)

print(nuev())

#Función que recibe como parámetro una función.
def crear_func(n,m):
	def val():
		print('Se ejecuta la validacion')
		return n>0 and m>0
	
	return val


def aplicar_func(func):
	resul=func()
	print(resul)

#nueva_func=crear_func(10,9)
aplicar_func(crear_func(10,9))	