class Circulo:
	
	#pi=3.1416

	def __init__(self,radio):
		self.radio = radio


	def area(self):
		return self.radio * self.radio * self.devl_pi()

	@staticmethod	
	def devl_pi():
		return 3.1416	


obj = Circulo(7)

print(obj.area())
print(obj.devl_pi())