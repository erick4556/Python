Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mi_diccionario= {"clave 1":"valor 1","clave 2":2, "clave 3": 3.33}
>>> print (mi_diccionario['clave 2'])
2
>>> mi_diccionario["clave 3"]="nuevo valor"    #Esto sirve para modificar esta clave...
>>> print (mi_diccionario['clave 3'])
nuevo valor
>>> del(mi_diccionario["clave 1"])
>>> print (mi_diccionario)
{'clave 2': 2, 'clave 3': 'nuevo valor'}
>>> # Aqui use 'del que es para eliminar'...
... 
>>> mi_diccionario= {"clave 1":"valor 1","clave 2":2, "clave 3": 3.33,(1,2): [5,6,7]}  #Aqui use duplas que son las que estan en parentesis y lista la que estan en corchetes
>>> print (mi_diccionario)
{(1, 2): [5, 6, 7], 'clave 2': 2, 'clave 1': 'valor 1', 'clave 3': 3.33}
>>> print
<built-in function print>
>>> print(mi_diccionario[(1,2)])
[5, 6, 7]
>>> 