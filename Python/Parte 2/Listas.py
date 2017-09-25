my_list=["hola",3,12.3,True];

my_list.append(8) #Sirve para agregar datos en la lista.

print(my_list)

my_list.insert(4,'mañana') #Recibe dos tipos de datos, la posicion y el dato.

print(my_list)

my_list.remove(1)
print(my_list)
my_list.pop() # Extrae el último dato de la lista.

print(my_list)

#--------------------------------------------------

list2=[3,4,9,54,2,1,56,33,94,2,41]

list3=[8,65]

list2.sort() #Ordena de forma ascendente.

print(list2);

list2.sort(reverse=True) # Ordena de forma descendente.

print(list2);

list2.extend(list3) # Para unir los datos.

print(list2)