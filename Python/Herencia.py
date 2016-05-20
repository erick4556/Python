class CasaStark: #Super clase 
	"""Personajes  de Game of Thrones
		Casa Stark"""
	print("Hijos de Eddard Stark y Lady  Catelyn")
	def _init_(self, apellido_stark):
		self.apellido_stark= apellido_stark


class CasaTargaryen:
	"""Personajes  de Game of Thrones
		Casa Stark"""
	print("Hijos de Aerys - EL rey loco")
	def _init_(self, apellido_targaryen):
		self.apellido_targaryen= apellido_targaryen


class HerederoStark(CasaStark): #Clase hijo
	"""Sub-Clase que hereda de la clase CasaStark"""
	def nombre(self, nombre, apellido_stark):
		print("Mi nombre es ", nombre, "Heredero de la casa", apellido_stark)


class HerederoTargaryen(CasaTargaryen): #Sub-clase
 		"""Sub-Clase que hereda de la clase Targaryen"""
 		def nombre_tar(self, nombre, apellido_targaryen):
		print("Mi nombre es ", nombre, "Heredero de la casa", apellido_targaryen)



#Instanciamos objetos de la clase  derivada  HerederoStark
robb= HerederoStark("Stark")
sansa= HerederoStark("Stark")
arya=HerederoStark("Stark")
bran=HerederoStark("Stark")
rickon=	HerederoStark("Stark")

#Accedemos  a métodos y atributos (objeto.metodo)

print(robb.nombre("Robb", robb.apellido_stark))
print(sansa.nombre("Sansa", sansa.apellido_stark))
print(arya.nombre("Arya", arya.apellido_stark))	
print(bran.nombre("Bran", bran.apellido_stark))
print(rickon.nombre("Rickon", rickon.apellido_stark))


#Instanciamos objetos de la clase  derivada  HerederoStark

daenerys= HerederoTargaryen("Targaryen")
viserys= HerederoTargaryen("Targaryen")

print(daenerys.nombre_tar("Daenerys ", daenerys.apellido_targaryen))
print(viserys.nombre_tar("Viserys ", viserys.apellido_targaryen))





