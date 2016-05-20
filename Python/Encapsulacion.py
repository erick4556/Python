class Ejemplo:

	def __init__(self):
		self.__oculto = "Me encuentro oculto en la clase"

	def publico (self):
		return "Soy un metodo publico. A la vista  de todos!"


	def __privado(self):#Metodo de privado
		print ("Dentro de la clase todos me pueden ver")

		#Estos metodos se utilizan para establecer un nuevo valor.
	def get_oculto(self):
		return self.__oculto

	def set_oculto(self):
		 self.__oculto=self.__privado()	


#Instanciamos un objeto de la clase objeto
objeto= Ejemplo()
 
 #Intentamos acceder al metodo publico

 #print(objeto.publico())

 #Intentamos acceder al metodo __privado

 #print(objeto.__privado())


 #name mangling

 #print(objeto._Ejemplo__privado())

 #Accedemos al atributo __oculto del metodo __init__
 #mediante el metodo get_oculto
 #print(objeto.get_oculto())

objeto.set_oculto()



