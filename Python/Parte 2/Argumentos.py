# Un * puedes trabar con n cantidad de valores para nuestra función, esos valores se van a traducir que son tuplas.
# Con ** igual pero la diferencia que se va a trabajar con diccionarios.

def suma(*arg):
	print(arg)
	print(type(arg))#De que tipo es un valor.

suma(10,4,5,1,5)

def sum3(**kwarg):
	print(kwarg)
	print(type(kwarg))

sum3(val="Eduardo", x=2, y=9, z=True)	