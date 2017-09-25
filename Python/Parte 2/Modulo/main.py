#import calculadora Forma 1
#from calculadora import (suma, resta, mul, division) Forma 2
from calculadora import *;

n1=int(input("Escribe numero 1 = "))

n2=int(input("Escribe numero 2 = "))


#resultado = calculadora.mul(n1,n2) Forma 1

resultado = suma(n1,n2) + mul(n1,n2)

print("Suma = ",suma(n1,n2),"+ Multipicacion = ",mul(n1,n2)," resultado  = ",resultado)