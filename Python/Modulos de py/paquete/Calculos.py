def suma():
	"""Muestra la suma de dos numeros ingresados"""
	a=int(input("Ingrese un numero entero : "));
	b=int(input("Ingrese un numero entero : "));
	print (a+b);


	def resta():
	"""Muestra la resta de dos numeros ingresados"""
	a=int(input("Ingrese un numero entero : "));
	b=int(input("Ingrese un numero entero : "));
	print (a-b);


	def multi():
	"""Muestra la multiplicacion de dos numeros ingresados"""
	a=int(input("Ingrese un numero entero : "));
	b=int(input("Ingrese un numero entero : "));
	print (a*b);


	def div():
	"""Muestra la division de dos numeros ingresados"""
	a=int(input("Ingrese un numero entero : "));
	b=int(input("Ingrese un numero entero : "));
	print (a/b);


	def fibonacci(n):
		"""Muestra la serie finobacci
			Hasta el numero n"""
		x, y=0,1  #Asignacion multiple

		while x < n:
			print(x);
			x,y = y,x+y #Aqui va ser x=y, y=x+y
		print() #Salto de linea
 					