#Para acceder a un archivo se puede hacer de tres maneras, r (read), w (write), a (append)

from io import open #importa la funcionalidad de open para ser usada
archivo = open("J.txt", 'r') 
# primerLinea = archivo.readline() # readline nos da una linea del archivo
# print(primerLinea)

lineasArchivo = archivo.readlines()
print(lineasArchivo)
for linea in lineasArchivo:
    print(linea.strip()) # strip lo que es eliminar los espacios en blanco a la izquierda y derecha ejemplo "   asss    " -> "asss"
archivo.close()
"""
archivo = open("J.txt", 'a') 
archivo.write("Esto es desde python 3\n")
archivo.write("Esta es una segunda linea\n")
archivo.close()

archivo = open("J.txt", 'r')

lineasArchivo = archivo.readlines()
print(lineasArchivo)
for linea in lineasArchivo:
    print(linea.strip()) # strip lo que es eliminar los espacios en blanco a la izquierda y derecha ejemplo "   asss    " -> "asss"
archivo.close()"""

"""
def crearArchivo(nombreArchivo):
    archivo = open(nombreArchivo, 'w')
    archivo.close()

def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def escribirArchivo(nombreArchivo, datos):
    archivo = open(nombreArchivo, 'w')
    archivo.write(datos)
    archivo.close()

def agregarAlArchivo(nombreArchivo, datos):
    archivo = open(nombreArchivo, 'a')
    archivo.write(datos)
    archivo.close()

def escribirArchivoLista(nombreArchivo, datos):
    archivo = open(nombreArchivo, 'w')
    if len(datos) != 0 :
        for dato in datos:
            archivo.write((dato + '\n'))
    archivo.close()

def agregarAlArchivoLista(nombreArchivo, datos):
    archivo = open(nombreArchivo, 'a')
    if len(datos) != 0 :
        for dato in datos:
            archivo.write((dato + '\n'))
    archivo.close()"""