#Generadores nos va a servir para poder crear objetos sin necesidad de almacenarlos en la memria ram...

#def devva():
#	print('Hola mundo')
#	print("Hola 2")
#	print("Hola") 

def genera(*args):
	for valor in args:
		yield valor * 10,True #Para poder usar el generador se usa el yield, SIEMPRE.
 

for valor,valor_2 in genera(1,2,3,4,5,6,7,8,9,11,12):
	print(valor,valor_2)

#print(devva())	