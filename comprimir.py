import zipfile

from zipfile import ZipFile

#with zipfile.ZipFile("archivo.zip","w") as fzip:
    #fzip.write ("docx.docx")
    #fzip.write ("png.png")
    #fzip.printdir()
    #fzip.extractall()


import gzip 
#with open ("docx.docx", "rb") as original:
#    with gzip.open("archivo.txt.gz", "wb") as archivo1:
#        archivo1.writelines(original)


import bz2

#cadena = b"cadena Cadena Cadena"
#cadena_c = bz2.compress(cadena)

#print(cadena)
#print(cadena_c)

#print(bz2.decompress(cadena_c))


import tarfile
archivo_tar = tarfile.open("primer.tar.gz", "w:gz")
archivo_tar.add('docx.docx')
archivo_tar.add('png.png')
archivo_tar.close()
