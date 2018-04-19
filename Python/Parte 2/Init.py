class Main:

	#color = 'Rojo'

	#tiene_borrador = False

	#usa_grafito = True

	def __init__(self,color,contiene_borr,usa_grafito):

		#Para que un metodo pueda acceder a un atributo...
		self.color = color

		self.tiene_borrador = contiene_borr

		self.usa_grafito = usa_grafito

	#Con valores predeterminados....

	#def __init__(self,color = "Amarillo",contiene_borr=True,usa_grafito=False):

		#Para que un metodo pueda acceder a un atributo...
	#	self.color = color

	#	self.tiene_borrador = contiene_borr

	#	self.usa_grafito = usa_grafito



	def dibujar(self):
		print('El lapiz esta dibujando!!')	

	def borrador(self):
		if self.valido(): #Llamar un metodo dentro de otro metodo...
			print('El lapiz esta borrando!!')
		else:
			print("El lapiz no puede borrar!!")

		if self.havgrafit():
			print('Tiene grafito')
		else:
			print("No tiene grafito")	

	def valido(self):
		return self.tiene_borrador

	def havgrafit(self):
		return self.usa_grafito			

obj = Main('Verde',True,True)
#obj = Main()

obj.dibujar();
obj.borrador()