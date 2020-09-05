class Persona():
    def __init__ (self,nombre):
        self.nombre = nombre
    edad = 32
    
    def deInstancia(self):
        print("Método de instancia")
        pass
    
    @classmethod
    def deClase(cls):
	    print("Método de clase")
	    
    @staticmethod
    def estatico():
        print("Método estatico")
	
persona1 = Persona("Pepe")
print ("chau", persona1.nombre)
print ("chau", Persona.edad)

persona1.deInstancia()
Persona.deClase()
Persona.estatico()

