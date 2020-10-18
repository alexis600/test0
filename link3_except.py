try:
    raise TypeError
except:
    print ("asdasd")

import threading
import time

class MiHilo (threading.Thread):
    def run (self):
        print("{} inicio".format(self.getName()))
        time.sleep(2)
        print("{} terminado".format(self.getName()))
        

if __name__=="__main__":
    for x in range(2):
        hilo=MiHilo(name="Thread-{}".format(x+1))
        hilo.start()
        time.sleep(.5)
        


def primerDeco(funcion):
    def decorada(*args, **kkwars):
        print("deco")
    return decorada
    
#@primerDeco
def funcion():
    print("funcion")
    
funcion()


def lower(elementos): return elementos.lower()

lista = ["ale", "ALEX", "AleXiS"]   

print(list(map(lower, lista)))
    
print([cad.lower() for cad in lista])


def saludo(idioma):
    def saludo_es():
        print ("hola")
    def saludo_en():
        print ("hi")
        
    idioma_func = {"es": saludo_es, "en": saludo_en}
    return idioma_func[idioma]
    
saludar = saludo("es")
saludar()


from functools import reduce
numeros = (1,2,3,4)
def suma(x, y):
    return x+y
    
sumar = reduce (suma,numeros)

print(sumar)


import re

print (re.search(r"\d\d","kilo45"))

patron = re.compile("\d\d")
print(str(patron)+"\n"*40)


print (patron.search("kilo89").group())


#con modificadores
patronMod = re.compile(r"ab", re.IGNORECASE)
print (patronMod.search("aBsAbcd"))
#aca si pones un numero despues del patron busca desde ese caracter
#no se como display las ocurrencias

if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
    print("se encontro el patron")
#$ es fin de cadena


#para sustitucion

cadena = "relacion123ado"
cadenaSus = re.sub(r"\d","*",cadena,1)
print(cadena, "\n", cadenaSus)





