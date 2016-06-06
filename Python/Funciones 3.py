Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def cal(a,e):
... 	div=a/e
... 
>>> w=int(input("Numeor 1 :"))
Numeor 1 :6
>>> n=int(input("Numero 2 : "))
Numero 2 : 3
>>> def cal(a,e):
... 	div=a/e
... 	print(div)
... 
>>> cal(w,n)
2.0
>>> def cal(a,e):
... 	div=a/e
... 	return div
... 
>>> cal(w,n)
2.0
>>> print("La division es : ",cal(w,n))
La division es :  2.0
>>> 