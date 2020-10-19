import sys

print(sys.path)

from Paquete import moduloA, moduloB

moduloA.metodo()

moduloB.metodo()


import csv

doc = open("archivoW.csv", "w")

doc_csv_w = csv.writer(doc)

lista = ["Ale", 480]

#doc_csv_w.writerow(lista)

doc.close()