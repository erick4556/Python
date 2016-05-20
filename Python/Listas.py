Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> l=[2,"tres",True,["uno"]];
>>> print (l);
[2, 'tres', True, ['uno']]
>>> l2=1[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> l2=1[2];
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> l2=l[2];
>>> print (l2);
True
>>> l2=l[3][0];
>>> print (l)
[2, 'tres', True, ['uno']]
>>> print (l2)
uno
>>> l=[2,"tres",True,["uno",10]];
>>> l2=l[1];
>>> print (l2);
tres
>>> l[1]=4
>>> print (l)
[2, 4, True, ['uno', 10]]
>>> print l2
  File "<stdin>", line 1
    print l2
           ^
SyntaxError: Missing parentheses in call to 'print'
>>> print (l2)
tres
>>> l2=l[0:3];
>>> print (l2)
[2, 4, True]
>>> l2=l[0:3:2]; #va saltando de 2 en 2
>>> print (l2)
[2, True]
>>> print (l)
[2, 4, True, ['uno', 10]]
>>> print (l2)
[2, True]
>>> l2=[1::2];
  File "<stdin>", line 1
    l2=[1::2];
         ^
SyntaxError: invalid syntax
>>> l2=l[1::2];
>>> print (l2)
[4, ['uno', 10]]
>>> l[0:2]=[4,3]
>>> print (l)
[4, 3, True, ['uno', 10]]
>>> l[0:2]=[4]
>>> print (l)
[4, True, ['uno', 10]]
>>> l2=l[-1];
>>> print (l2)
['uno', 10]
>>> 