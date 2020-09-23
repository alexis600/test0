class Clase():

#	def __new__(cls, radio):
#		#print("xD")
#		print("new")
#		return super().__new__(cls)
	
	def __init__(self, radio):
		print("init")
		self.radio = radio

	@ classmethod 
	def saludar(cls, nombre):
		print("hola", nombre)
		
	
	@property
	def area(self):
		return 3.1416*(self.radio**2)
		
		##@staticmethod


Clase.saludar("Ale")


circulo = Clase(10)
print("el radio es:",circulo.radio)
print("el área es:", str(circulo.area))
			
