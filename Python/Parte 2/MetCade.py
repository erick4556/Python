course="Curso";
my_string='Código bueno';

"""Metodos de formatos"""

result="{} de {}".format(course, my_string); #Las variables course y my_string toma el lugar de las llaves {}.

print(result);

print("\n");

result="{b} de {a}".format(b= course, a= my_string);

print(result);

print("\n");

#result=result.lower(); #Minuscula

#result= result.upper();

result= result.title();

print(result);

print("-------------------\n");

"""Metódos de búsqueda"""

pos=result.find("Código")   ##Regresa en que posición empieza la palabra código.
count=result.count('C')		##Devuelve cuantas veces se repite la letra que indiquemos.
print(pos)
print(count)

print("\n");

new_string=result.replace('C', 'x');
print(new_string)

new_string=result.split(' ');

print(new_string)
