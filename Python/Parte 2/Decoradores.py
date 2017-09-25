#Un decorador es una función que recibe como parametro otra función para dar como salida una función.

def decorador(func):
	def ante():
		print("Vamos a ejecutar la funcion")

	def despues():
		print("Se ejecutó la función")	

	def nuev(*args,**kwargs):#Los * es por que va recibir n cantidad de argumentos.
		#Agrega código
		ante()
		func(*args,**kwargs)#Donde la ejecuto.
		#Agrega código tambien despues.
		despues()
	return nuev	

@decorador
def salud():
	print("Saludos")

@decorador
def suma(d,f):
	print(d+f)


suma(8,32)
