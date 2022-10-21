"""
Escribir un programa que leerá un archivo que tendrá en cada fila 
nombre-apellido-matricula ojo está dividido con guiones “-“
el programa debe pedir el nombre del archivo y posteriormente desplegar
a. Mostrar los datos
b. Buscar
    i. Nombre
    ii. Apellido
    iii. Matricula"""

nombreArchivo = input("Ingrese el nombre del archivo: ") #"datosAlumnos.csv"

def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas

i = 1
while i !=3: #While para controlar menu principal
    i = int(input("\n¿Que accion requiere hacer? \n 1-Mostrar los datos \n 2-Buscar alumno \n 3-Salir\n>>>[1-3]: "))
    
    if i == 1: #Impresion de los alumnos
        print("\n\t\t REPORTE DE ALUMNOS\n")
        alumnosLeidos = leerArchivo(nombreArchivo)
        for alumno in alumnosLeidos:
            datosAlumno = alumno.strip().split("-")
            print("\nNombre: " + datosAlumno[0] + "\nApellido: " + datosAlumno[1] + "\nMatricula: " + datosAlumno[2] )
    
    if i == 2: #Busqueda por nombre, apellido o matricula
        j = int(input("\n¿Que dato es el que tiene? \n 1-Nombre \n 2-Apellido \n 3-Matricula \n>>>[1-3]: "))
        if j == 1:
            a = "Nombre a buscar"
        elif j == 2:
            a = "Apellido a buscar"
        elif j == 3:
            a = "Matricula a buscar"
        else:
            continue
        o = None
        alumnosLeidos = leerArchivo(nombreArchivo)
        while o == None: 
            Buscado = input("\n" + a + ": ")

            for alumno in alumnosLeidos:
                datosAlumno = alumno.strip().split("-")
                if datosAlumno[j-1] == str(Buscado):
                    o=1
                    print("\nNombre: " + datosAlumno[0] + "\nApellido: " + datosAlumno[1] + "\nMatricula: " + datosAlumno[2] )
            
            if o == None:
                print("No existe, intente de nuevo ")

