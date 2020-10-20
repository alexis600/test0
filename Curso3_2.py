import sys

print(sys.path)

from Paquete import moduloA, moduloB

moduloA.metodo()

moduloB.metodo()


import csv

doc = open("archivoW.csv", "a")
# modo , "a" append
# modo , "w" escribe, sobreescribe, crea

doc_csv_w = csv.writer(doc)

#lista = [["Ale", 300], ["Maxi", 500], ["Fiore", 600]]
lista = [["Momo", 2]]
#doc_csv_w.writerows(lista)

#for x in lista:
#    doc_csv_w.writerow(x)
doc.close()

#para solo leer , "r"

doc = open("archivoW.csv", "r")
doc_csv = csv.reader(doc)

for nombre, nro in doc_csv:
    print(nombre, nro)

doc.close()