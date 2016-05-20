class Miamigo()
	"""Otro ejemplo"""
	def __init__(self,color): #self se referencia al objeto..
		#Definimos atributos	
		self.color

	def romp(self, romper):
		print(romper)

	def juego(self, jugar):
		print(jugar)

	def proteger(self,cuidar):
		print(cuidar)


#Instanciamos  dos objetos  de la calse Miamigo()

Luis=Miamigo("Moreno")   #Aqui tenemos los dos objetos creados
Ale=Miamigo("Blanca")
#Accedemos  a su atributo
print(Ale.color)

#Accedemos a los métodos

Luis.romp("Mi mejor amigo")
Ale.romp('No se quien es XD...')
