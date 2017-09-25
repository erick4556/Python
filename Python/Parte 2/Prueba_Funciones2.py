class Main:
	def eleve(self,el):
		mul=1
		num=int(input("Ingrese numero a elevar : "))
		for x in range(el):
			mul=mul*num
		return mul	
	def suma(self):
		suma=0
		for x in range(0,5):
			print(x)
			suma+=x
		print("La suma es : ",suma)		

def nodev():
	suma=0
	for x in range(0,3):
		print("Ingrese numero ",x+1," vez : ")
		num=int(input(""))
		suma+=num
	print("La suma es : ",suma)

def elevacion(cant):
	multi=1;
	a=int(input("Ingrese un numero para ser elevado : "))
	for x in range(cant):
		multi=multi*a;
	print("La elevacion de ",a," a la ",cant," es : ",multi)		


obj=Main()
c=int(input("Ingrese la cantidad a elevar : "))
elevacion(c);
#print(obj.eleve(c))			
#obj.suma();
#nodev()