Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> print(time.asctime())
Fri Apr  8 15:08:59 2016
>>> from time import asctime #Estamos diciendo que del module time nos importe asctome...!
>>> print(asctime())
Fri Apr  8 15:11:33 2016
>>> 