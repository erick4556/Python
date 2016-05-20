Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a=4
>>> b=6
>>> suma=a+b
>>> print (" La suma es :"suma)
  File "<stdin>", line 1
    print (" La suma es :"suma)
                             ^
SyntaxError: invalid syntax
>>> print (" La suma es :",suma)
 La suma es : 10
>>> #Division
... divi=a/b
>>> print (" La division es ",divi)
 La division es  0.6666666666666666
>>> #Multiplicacion
... multi=a*b
>>> print ("La Multiplicacion es ",multi);
La Multiplicacion es  24
>>> #Potenciacion
... pon=b **2
>>> print ("La Potenciacion es ",pon);
La Potenciacion es  36
>>> pon=b **3
>>> print ("La Potenciacion es ",pon);
La Potenciacion es  216
>>> pon=b *3
>>> print ("La Potenciacion es ",pon);
La Potenciacion es  18
>>> pon=b ***3
  File "<stdin>", line 1
    pon=b ***3
            ^
SyntaxError: invalid syntax
>>> pon=b **3
>>> print ("La Potenciacion es ",pon);
La Potenciacion es  216
>>> #Otra division
... divia=float b /a
  File "<stdin>", line 2
    divia=float b /a
                ^
SyntaxError: invalid syntax
>>> divia=float (b) /a
>>> print
<built-in function print>
>>> print ("La otra division es ",divia);
La otra division es  1.5
>>> 