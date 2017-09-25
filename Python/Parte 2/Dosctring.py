def generador(*args):
	"""Recibe n cantidad de número y regresa el número, además de regresar True
	o False si el número es mayor a 5 """
	for valor in args:
		yield valor, True if valor > 5 else false


name=generador.__name__
document= generador.__doc__ #Para imprimir la documentacion.

print(document)		
print(name,' : ')