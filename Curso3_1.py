print("\n" * 15)

cadena = "Hola ALE   "


reemplazada = cadena.replace("hola", "Chau").swapcase() # cambia mayusculas y minusculas


import re

patronMod = re.compile(r"hola", re.IGNORECASE)
reemplazadaconRE = re.sub(patronMod, "Chau", cadena)

print(cadena)
print(reemplazada)
print(reemplazadaconRE)
