Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Comillas simples
... cads ='Texto entre comillas simples'
>>> #Comillas dobles
... cadd="Texto entre comillas dobles"
>>> print type(cads)
  File "<stdin>", line 1
    print type(cads)
             ^
SyntaxError: invalid syntax
>>> print (type(cads))
<class 'str'>
>>> print cads
  File "<stdin>", line 1
    print cads
             ^
SyntaxError: Missing parentheses in call to 'print'
>>> print (cads)
Texto entre comillas simples
>>> print (cadd)
Texto entre comillas dobles
>>> cads ='Entre comillas \n simples'
>>> print (cads)
Entre comillas 
 simples
>>> cadd="Entre comillas \n\t dobles"
>>> print (cadd)
Entre comillas 
	 dobles
>>> catri="""Hola como estas
... que haces
... q te cuentas
... ...
... dnd estas"""
>>> print (catri)
Hola como estas
que haces
q te cuentas
...
dnd estas
>>> 
>>> 
>>> #Reparticion y Concatenacion
... cad="Cadenda" *3
>>> print (cad)
CadendaCadendaCadenda
>>> cad1='Holi'
>>> cad2='Que hay'
>>> print (cad1 + cad2)
HoliQue hay
>>> 
>>> 
>>>
>>> #Valores booleanos
  File "<stdin>", line 1
    >>> #Valores booleanos
     ^
SyntaxError: invalid syntax
>>> >>> #Valores booleanos
  File "<stdin>", line 1
    >>> #Valores booleanos
     ^
SyntaxError: invalid syntax
>>> #Booleanos
... bt= True
>>> bf= False
>>> band= True and False
>>> bor= True or False
>>> bnot= not True
>>> print (band)
False
>>> print (bor)
True
>>> print(bnot)
False
>>> 