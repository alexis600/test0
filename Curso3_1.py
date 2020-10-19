print("\n" * 15)

cadena = "  Hola ALE   "


reemplazada = cadena.replace("hola", "Chau").swapcase() # cambia mayusculas y minusculas


import re

patronMod = re.compile(r"hola", re.IGNORECASE)
reemplazadaconRE = re.sub(patronMod, "Chau", cadena)

print(cadena)
print(reemplazada)
print(reemplazadaconRE)

#sacar espacios
nueva = cadena.strip()
print(nueva)
lnueva = cadena.lstrip() #saca espacios a la izq y rstrip a la derecha
print(lnueva)

#cadena.upper() y cadena.lower() les cambia el case

cadenaSplit = "hola ! chau ! mierda ! joder"
#cadenaSplit.split(cadenaSplit('!'))

print(cadenaSplit.split('!'))


lista = [3,56,1,3,0,9,8,5]
print(sorted(lista, reverse=True))
print(sorted(lista))
print(lista)

#con lista.sort() ya queda guardada la original, antes la original no sufria cambios

#tambien aplica a letras


#CONJUNTOS
conju1 = {'1', '2', '3', '4'}
conju2 = set('456378')
print(conju1)
print(conju2)
print(conju1, conju2, sep='\n')

print(conju1 & conju2)
print(conju1.intersection(conju2))

print(conju1 | conju2)


print(sorted(conju1 | conju2))


print(sorted(conju2 | conju1))