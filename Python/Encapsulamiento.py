Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> class Aeronave:
... 	def viajar(self):
... 		print("Yo viajo por los aires")
... 
>>> class Automovil:
... 	def viajar(self):
... 		print("Yo viajo por los camimnos")
... 
>>> zeppelin=Aeronave()
>>> coche=Automovil()
>>> 
>>> zeppelin.viajar()# Se imprime de manera automática sin necesidad de usar el print
Yo viajo por los aires
>>> coche.viajar()# Se imprime de manera automática sin necesidad de usar el print
Yo viajo por los camimnos
>>> 