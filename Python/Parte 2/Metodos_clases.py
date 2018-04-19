class Animal:
	volador= True

class Cocodrilo(Animal):
	
	def __init__(self,nombre):
		self.nombre = nombre

	#Metodo factory
	@classmethod #Pueden acceder a los atributos o metodos de las clases que estamos heredando...
	def new(cls,nombre):
		cls.volador = False
		return Cocodrilo(nombre)



cocod = Cocodrilo.new('Juancho')

print(cocod.nombre)
print(cocod.volador)