def factorial_numero(numero):
	factorial=1
	while numero >0:
		factorial= factorial *numero
		numero-=1
	return factorial

e=int(input("Ingresa primer numero : "))

print("Resultado : ",factorial_numero(e))		