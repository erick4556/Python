Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> class Ejemplo:
... 	def sal(self, texto):
... 		print(texto)
... 	def calcu(self,a,b):
... 		div=a*b
... 		print("La multi es : ",div)
... 
>>> obj=Ejemplo()
>>> al=input("texto :")
texto :hola
>>> obj.sal(al)
hola
>>> nu=int(input("Numero 1 :"))
Numero 1 :4
>>> nu2=int(input("Numero 2 :"))
Numero 2 :2
>>> obj.calcu(nu,nu2)
La multi es :  8
>>> 