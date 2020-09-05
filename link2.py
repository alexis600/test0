class Clase():
    def __new__(cls):
		print("xD")
        print("new")
   	    return super.__new__(cls)
	
	def _init__(self):
		print("init")
    
	@classmethod
	def saludar (cls, nombre):
		print("hola", nombre)
		
	##@staticmethod
	

Clase.saludar("Ale")
