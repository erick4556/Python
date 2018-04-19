class Animal:
	@property
	def terrestre(self):
		return True



class Felino(Animal): #clase padre..
	@property
	def garras_retractiles(self):
		return 'Garras'

	def cazar(self):
		print("El felino esta cazando")	


class Mascota:

	def __init__(self,nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino,Mascota):

	def __init__(self,nombre):
		Mascota.__init__(self,nombre)
		self.nombre_gato = nombre

	def gato_bandido(self):
		self.cazar()

	def mostrar_nombre(self): #Sobre escritura de métodos..
		#Llamar el metodo pero de la clase padre..
		Mascota.mostrar_nombre(self)
		print("Nombre gato : {}".format(self.nombre))	


name = 'Carlos'

gato = Gato(name)

#gato.nombre="Patricio"
gato.mostrar_nombre()

#Sobreescribir metodo es tomar el metodo de una clase padre y cambiarle una funcionalidad o agregarle mayor 
#funcional..



