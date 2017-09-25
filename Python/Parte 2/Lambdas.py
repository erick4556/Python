#Lambdas nos sirve para crear pequeñas funciones anónimas en una sola línea de código. Debe ser la forma más simple posible.

func=lambda al,al2 : al + al2

form=lambda palabra: "¿{}?".format(palabra)

no_valor = lambda : 'Regresa algo'

#print(func(12,321))

#print(form('Esto es una pregunta'))

a=int(input("Numero 1 : "))
b=int(input("Numero 2 : "))

	
print(func(a,b))

print(form('Esto es una pregunta'))
