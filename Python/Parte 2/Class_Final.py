#Atributos...

#class Usuario:
#	pass

#usuario = Usuario()	

#print(usuario.__dict__)

#usuario.nombre = 'Carlos'

#print(usuario.nombre)

#print(usuario.__dict__) #Ver los atributos de un objeto..


#class Usuario:
#	def __init__(self):
#		self.__nombre = "Este es uns secreto"


#usuario = Usuario()

#usuario.__password = 'Este ya no es un secreto'
#print(usuario.__dict__)


#Métodos magicos..
class Usuario:
	#apellido = 'Castillo'
	def __new__(cls): #Constructor
		print('Este es el constructor')
		return super().__new__(cls)

	def __init__(self):
		print("Este es el segundo que se ejecuta...")	


	def __str__(self): #Para que no salga los numeros..
		return 'Esto se imprime cuando intento mostrar el objeto'	

	def __getattr__(self, apellido): #Para cuando no se encuentra el atributo..
		print("Aqui mostramos que no se encontro el atributo")
		self.otro_metodo()
	def otro_metodo(self):
		print("Otro metodo!!")	

usuario = Usuario()
print(usuario)

print(usuario.apellido)



