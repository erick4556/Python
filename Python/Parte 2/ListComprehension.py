lista=[valor for valor in range(0,101) if valor%2==0]

print(lista)

print();

tupla=tuple((valor for valor in range(0,101) if valor%2!=0))

print(tupla)

print()

diccionario={indice:valor for indice,valor in enumerate(lista) if indice < 10}

print(diccionario)