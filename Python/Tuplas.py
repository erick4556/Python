Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> t= 1,True,"Hola";            #tuplas no es necesario poner los corchetes al principio al final..
>>> print (t);
(1, True, 'Hola')
>>> print t;
  File "<stdin>", line 1
    print t;
          ^
SyntaxError: Missing parentheses in call to 'print'
>>> t= (3,'Hola',False);
>>> print(t)
(3, 'Hola', False)
>>> print type(t)
  File "<stdin>", line 1
    print type(t)
             ^
SyntaxError: invalid syntax
>>> a= (2,"Hola",False);
>>> print (type(t));
<class 'tuple'>
>>> #Ahi esta indicando que es tipo tupla..
... 
>>> print (t[1]);
Hola
>>> # A las tuplas no se le puede agregar mas elementos y alas lista si se le puede agregar mas elementos...
... 
>>> 