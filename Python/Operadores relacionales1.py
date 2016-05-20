Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> v=3
>>> a=1
>>> print (v==a)
False
>>> print (1==1)
True
>>> a=10
>>> b=10
>>> print (a!=b)
False
>>> print (12!=a)
True
>>> #Como pueen ver se puede hacer de varias formas 
... :
  File "<stdin>", line 2
    :
    ^
SyntaxError: invalid syntax
>>> 
>>> #Se puede hacer como desees
... a
10
>>> b
10
>>> print ("azul" != "AZUL")
True
>>> print ("azul" != "azul")
False
>>> s=3
>>> c=1
>>> s > c
True
>>> print s < c
  File "<stdin>", line 1
    print s < c
          ^
SyntaxError: Missing parentheses in call to 'print'
>>> print (s < c)
False
>>> print (2 <=  1)
False
>>> print (6 <=6)
True
>>> print (3 >=1)
True
>>> print (3>=19)
False
>>> lista_uno=[1,2,3]
>>> lista_2=[1,2,4]
>>> print (lista_unod == lista_2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lista_unod' is not defined
>>> print (lista_uno == lista_2)
False
>>> lista_2=[1,2,3]
>>> print (lista_uno == lista_2)
True
>>> #Es igual por que modifiquie la variable...
... 
>>> tupla_uno=(1,2,"Hola")
>>> tupla_2=(1,2,'Que hay')
>>> print (tupla_uno==tupla_2)
False
>>> print (tupla_uno!=tupla_2)
True
>>> 