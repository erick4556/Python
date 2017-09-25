class Main:
	def fun1(self,num1,num2):
		suma=0;
		suma=num1+num2
		return suma

	def fun2(self):
		n=int(input("Ingrese un numero : "))
		mult=n*2
		print("La multiplicacion de ese numero por dos es : ",mult)

	def prom(self,c):
		suma=0
		for x in range(c):
			print("Introduzca nota ",x+1," : ")
			nota=int(input(""))
			suma+=nota
		prom=suma/c
		print("El promedio es : ",prom)	

def node(a,b):
	multi=a*b;
	print("La multiplicacion es : ",multi)

def sal(s,d):
	div=a/d
	return div

def saludo():
	a=int(input("Ingrese numero : "))
	if a%2==0:
		print('Saludos')
	else:
		print("No saludos")


#Se crea el objeto
obj=Main()
	
#Menu
	
op=0


while op!=3:

	
	print("1.Prueba de funciones\n2.Saludos\n3.Salir")

	op=int(input("Ingresa una opcion : "))

	if op==1:

		saludo()

		a=int(input("Ingresa numero 1 : "))
		e=int(input("Ingresa numero 2 :"))

		node(a,e)

		print(sal(a,e))

		if obj.fun1(a,e)%2==0:	
 			print("Funcion con objeto es positivo, y el resultado de la suma es : ",obj.fun1(a,e))
		else:
 			print("Funcion con objeto es negativa, y el resultado de la suma es : ",obj.fun1(a,e))
		obj.fun2()
		n=int(input("Introduzca la cantidad para la función  del promedio : "))
		obj.prom(n)

	elif op==2:
		for x in range(0,3):
			print("Saludo ",x+1,"\n") 	

	elif op==3:
		print("Gracias por visitarnos")

	elif op>3:
		print("Opción erronea vuelve a insertar")		

