class Usuario:
	def __init__(self,username,password,email):
		self.username = username
		#__password Atributo privado..
		self.__password = self.__generar_pass(password)
		self.email = email

	#Cifrar el password
	
	def __generar_pass(self,password):
		return password.upper()	


	#Lo unico que esta haciendo es retornado el atributo privado...
	@property
	def password(self):
		return self.__password


	#Va generar un nuevo string y se lo asigna al atributo privado..
	@password.setter
	def password(self, valor):
		self.__password = self.__generar_pass(valor)



obj = Usuario('Eduardo',"Loco123","ejemplo@hotmail.com")


print("\n",obj.password)
obj.password = "Nuevo pass"
print("\n",obj.password)
