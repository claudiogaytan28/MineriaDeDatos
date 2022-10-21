"""
1.	Se desea crear un programa para manipular Empleado -> (nombre, edad, numeroEmpleado, Salario) 
se desea crear un programa que sea capaz de capturar N empleados y guardarlos en un archivo .csv, 
posteriormente desplegar un menú con
a.	AgregarEmpleado
b.	BuscarEmpleado -> usar el número de empleado
c.	EliminarEmpleado -> usar el número de empleado
d.	EditarEmpleado (Se puede usar el número de empleado para saber que empleado se editara)
No puede haber dos empleados con el mismo número de empleado ni tampoco menores de edad, 
Uso de clases y objetos obligatorio se debe crear métodos que impriman los datos del empleado, 
se deben reflejar los cambios en el archivo (40 pts)
"""
nombreArchivo = "datosEmpleado.csv"

class Empleado:
    def __init__(self, nombre, edad, numeroEmpleado, salario):
        self.nombre = nombre
        self.edad = edad
        self.numeroEmpleado = numeroEmpleado
        self.salario = salario
    
    def __str__(self):
        return self.nombre + " , " + str(self.edad) + " , " + str(self.numeroEmpleado) + " , " + str(self.salario) + "\n"

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

i = 1
while i != 6: #While para controlar el menu
    i = int(input("\n¿Que accion requiere hacer? \n 1-Agregar empleado nuevo \n 2-Buscar empleado \n 3-Eliminar un empleado\n 4-Editar un empleado\n 5-Mostrar empleados\n 6-Salir\n>>>[1-6]: "))
    if i == 1: #Agregar empleado
        nombre = input("\nNombre del empleado: ")
        o = None
        while o == None: #While para validar mayoria de edad
            o = 1
            edad = int(input("\nEdad: "))
            if edad < 18 :
                print("\nRango de edad rechazado, el empleado debe ser mayor de edad")
                o = None

        o = None
        while o == None:
            o = 1
            numeroEmpleado = int(input("\nNumero de empleado: ")) 

            empleadosLeidos = leerArchivo(nombreArchivo)
            for empleado in empleadosLeidos:    #For para validar si ya existe el numero de empleado ingresado
                datosEmpleado = empleado.strip().split(" , ")
                if datosEmpleado[2] == str(numeroEmpleado):
                    print("\nEl numero de empleado ya existe, intente de nuevo ")
                    o = None
            

        salario = int(input("\nSalario: "))
        empleado = Empleado(nombre,edad,numeroEmpleado,salario)
        agregarAlArchivo(nombreArchivo, empleado.__str__())

    elif i == 2: #Buscar empleado por numero
        empleadosLeidos = leerArchivo(nombreArchivo)
        o = None
        while o == None:
            numeroBuscado = int(input("\nNumero de empleado a buscar: "))
            for empleado in empleadosLeidos:
                datosEmpleado = empleado.strip().split(" , ")
                if datosEmpleado[2] == str(numeroBuscado):
                    o=1
                    print("\nNombre: " + datosEmpleado[0] + "\nEdad: " + datosEmpleado[1] + "\nNumero de empleado: " + datosEmpleado[2] + "\nSalario: " + datosEmpleado[3])
            if o == None:
                print("Numero de empleado no existe, intente de nuevo ")

    elif i == 3: #Eliminar empleado
        empleadosLeidos = leerArchivo(nombreArchivo)
        o = None
        listaEmpleados = []
        while o == None:
            numeroBuscado = int(input("\nNumero de empleado a eliminar: "))

            for empleado in empleadosLeidos:    #For para validar si existe el numero ingresado
                datosEmpleado = empleado.strip().split(" , ")
                if datosEmpleado[2] == str(numeroBuscado):
                    o=1
            
            if o == 1: 
                for empleado in empleadosLeidos: #For para agregar los elementos diferentes al numero ingresado a la listaEmpleados
                    datosEmpleado = empleado.strip().split(" , ")
                    if datosEmpleado[2] != str(numeroBuscado): 
                        listaEmpleados.append(Empleado(datosEmpleado[0],datosEmpleado[1],datosEmpleado[2],datosEmpleado[3]))
                
                for empleado in listaEmpleados:
                    escribirArchivo(nombreArchivo,empleado.__str__())
            else:
                print("Numero de empleado no existe, intente de nuevo ")

    elif i == 4: #Editar empleado 
        empleadosLeidos = leerArchivo(nombreArchivo)
        o = None
        listaEmpleados = []
        while o == None:
            numeroBuscado = int(input("\nEmpleado a modificar, ingrese su numero de empleado para buscarlo: "))

            for empleado in empleadosLeidos: #For para validar si existe el numero ingresado
                datosEmpleado = empleado.strip().split(" , ")
                if datosEmpleado[2] == str(numeroBuscado):
                    o = 1
            
            if o == 1:

                o1 = 1

                while o1 != 5: #While para validar opcion o1
                    o1 = int(input("\n¿Que requiere modificar?\n1-Nombre\n2-Edad\n3-Numero de empleado\n4-Salario\n5-Nada\n[1-5] >>"))
                    #Los elif sirven para modificar el dato deseado
                    if o1 == 1:
                        Nuevo = input("\nNombre de empleado nuevo: ")
                    elif o1 == 2:
                        Nuevo = int(input("\nEdad de empleado nuevo: "))
                    elif o1 == 3:
                        Nuevo = int(input("\nNumero de empleado nuevo: "))
                    elif o1 == 4:
                        Nuevo = int(input("\nSalario de empleado nuevo: "))
                    elif o1 == 5:
                        break
                    else:
                        print("\nError en la opcion ingresada, intente de nuevo ")
                        continue
                    
                    for empleado in empleadosLeidos: 
                        datosEmpleado = empleado.strip().split(" , ")
                        if datosEmpleado[2] == str(numeroBuscado):  #Se usa el numero de empleado para buscar el empleado
                            datosEmpleado[ o1-1 ] = Nuevo # Se modifica el dato deseado usando el numero de opcion menos uno en el indice 
                        listaEmpleados.append(Empleado(datosEmpleado[0],datosEmpleado[1],datosEmpleado[2],datosEmpleado[3]))
                
                    for empleado in listaEmpleados: #Sobre-escribimos el archivo con el nuevo numero de empleado
                        escribirArchivo(nombreArchivo,empleado.__str__())
                if o1 == 5:
                    break   
                
            
            else:
                print("Numero de empleado no existe, intente de nuevo ")

    elif i == 5: #imprimir empleados
        print("\n\t\t REPORTE DE EMPLEADOS\n")
        empleadosLeidos = leerArchivo(nombreArchivo)
        listaEmpleados = []
        for empleado in empleadosLeidos:
            datosEmpleado = empleado.strip().split(" , ")
            cadenaEmpleado = "Nombre: " + datosEmpleado[0] + "\nEdad: " + datosEmpleado[1] + "\nNumero de empleado: " + datosEmpleado[2] + "\nSalario: " + datosEmpleado[3] + "\n"
            print(cadenaEmpleado)
