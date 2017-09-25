dic={ 'a': 75, 3: 'Hola', (1,2) : "Saludos" } #Se le agregan claves... Las claves deben ser inmutables.
#Si se repite una clave, agarra la ultima clave agregada... 

dic["c"]='nuevo valor' #Se agrega una nueva clave con su valor.

dic['a']=False #Modificar clave

print(dic)

#val=dic["a"] #Traer el valor que deseemos del diccionario

val= dic.get('l', 'No se encuentra la clave') #Para saber si no se encuentra una clave. Tambien para traer valor que deseemos

print(val)

val = dic.get("a");

print(val)

del dic[3] #Eliminar una clave

print(dic)

llave= list(dic.keys()) #Objeto iterable. Nos trae todas las llaves. list trae las llaves como una lista.

print(llave)

valores= tuple(dic.values()) #Traer los valores del diccionario. tuple trae los valores en forma de tupla.

print(valores)


dic_2={"c": 56, 'u':52}

print(dic_2)

##Crecer un diccionario

dic.update(dic_2)

print(dic)





