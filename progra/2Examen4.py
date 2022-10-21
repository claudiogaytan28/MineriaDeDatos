'''4.	Escribir un programa que leerá dos archivos y compara si la información es igual en los dos '''


def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas
    
def conteoDatos(nombreArchivo):
    Leido = leerArchivo(nombreArchivo)
    a = 0
    for dato in Leido:
        datos = dato.strip().split(",")
        for elemento in datos:
            a=a+1
    return a

nombreA1 = "Archivo1.csv"
nombreA2 = "Archivo2.csv"

Leido1 = leerArchivo(nombreA1)
Leido2 = leerArchivo(nombreA2)
    
if conteoDatos(nombreA1) == conteoDatos(nombreA2):
    k = 0
    for dato1 in Leido1: #For para iterar las lineas del archivo 1
        datos1 = dato1.strip().split(",")

        for dato2 in Leido2: #For para iterar las lineas del archivo 2
            datos2 = dato2.strip().split(",")

            for elemento1 in datos1:

                for elemento2 in datos2:
                    if elemento1 == elemento2:
                        k += 1
                        continue   
    if k == conteoDatos(nombreA1):
        print("\nLos archivos son iguales")
    else:
        print("\nLos archivos son diferentes")    
else:
    print("\nLos archivos son diferentes")

