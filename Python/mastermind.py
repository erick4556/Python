import random  #Para seleccionar numero de manera aleatoria

continuar=1;


while continuar ==1:
	print("Bienvenido/a a MasterMind");
	print("Elija la dificultad del juego <1=Easy, 2=Hard, 3=Nightmare");
	dificultad=int(input("Digite el numero de dificultad: "));
	#Asignamos cantidad de digitos para cada dificulta.
	if dificultad ==1:
		cant_digitos=3
	elif dificultad==2:
		cant_digitos=4;
	elif dificultad==3:
		cant_digitos=5;



	digitos=('0','1','2','3','4','5','6','7','8','9');
	codigo='' #Aqui el codigo se ira almacenando..

	for i in range(cant_digitos):
		elegido=random.choice();	
		
		while elegido in codigo:	##Mientras que el numero elegido se encuentre almacenado en el codigo.
			elegido=random.choice(digitos);

		codigo=codigo + elegido;


	print("Tienes que adivinar  un codigo de ",cant_digitos, "digitos distintos");
	propuesta=input("Que codigo propones? : ");

	intentos=1;	

	while propuesta != codigo :
		intentos= intentos+1;
		aciertos=0;
		coincidencias=0;
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:    #Accedemos a la tupla mediante su indice...
				aciertos=aciertos+ 1;
			elif propuesta[i] in codigo:
				coincidencias= coincidencias+1;	
		print("Tu propuesta (",propuesta,") tiene ",aciertos," aciertos y",coincidencias," coincidencias");		
		propuesta=input("Propon otro código: ");

		#Este codigo se va repetor hasta que el usuario haya acertado al codigo correctamente..

	print("Felicidades! Adivinaste el codigo en ",intentos," intentos");
	continuar=int(input("Desea seguir jugando? : <1=si, 0=no"))

		 