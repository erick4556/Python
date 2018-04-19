class Main:

	#color = 'Rojo'

	#tiene_borrador = False

	#usa_grafito = True

	def __init__(self):

		#Para que un metodo pueda acceder a un atributo...
		self.color = 'Rojo'

		self.tiene_borrador = False

		self.usa_grafito = True


	def dibujar(self):
		print('El lapiz esta dibujando!!')	

	def borrador(self):
		if self.valido(): #Llamar un metodo dentro de otro metodo...
			print('El lapiz esta borrando!!')
		else:
			print("El lapiz no puede borrar!!")

	def valido(self):
		return self.tiene_borrador		

obj = Main()

#print(obj.color," ",obj.borrador," ",obj.usa_grafito)

obj.tiene_borrador = True
obj.dibujar();
obj.borrador()