import os
class Maestros:
    def __init__(self,numeroEmpleado=None,nombre="",edad=None):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.edad = edad
    
    def asignar(self,numeroEmpleado,nombre,edad):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nEdad: " + str(self.edad) + "\nNumero de empleado: " + str(self.numeroEmpleado) + "\n"

listaMaestros = [0]
op=1
n=0
while op==1 : #While para seguir capturando maestros
    i=1
    while i==1: #While para verificar si se repite el numero de empleado
        i=0
        num=int(input("\nIngrese el numero de empleado del maestro: \n>>"))
        listaMaestros[n]=Maestros(num)

        for j in range(len(listaMaestros)-1):
            if listaMaestros[j].numeroEmpleado == num :
                print("\n\t\t\t ERROR\nEl numero de empleado ingresado, ya existe. Intente de nuevo")
                i=1
    name=input("\nIngrese el nombre del maestro: \n>>")
    age=int(input("\nIngrese la edad del maestro: \n>>"))
    listaMaestros[n].asignar(num,name,age)
    n+=1 
    
    op=int(input("\n¿Quiere ingresar los datos de otro maestro? [SI-1, NO-2]\n>>"))
    if op==2:
        break
    listaMaestros.append(Maestros())

os.system("cls")
i=1
while i == 1:
    print("\t\t\tMENU")
    print("\nIngrese opcion: \n1-Imprimir los maestros\n2-Mostrar maestros con edad minima ingresada")
    print("3-Mostrar maestros con el nombre ingresado\n4-Buscar maestro con su numero de empleado\n5-Salir")
    op=int(input("[1-5]>>"))
    os.system("cls")
    if op==1:
        for maestro in listaMaestros:
            print(maestro)
    elif op==2:
        min=int(input("\nIngrese la edad minima: "))
        for maestro in listaMaestros:
            if maestro.edad > min:
                print(maestro)
    elif op==3:
        name=input("\nIngrese el nombre a buscar: ")
        for maestro in listaMaestros:
            if maestro.nombre == name:
                print(maestro)
    elif op==4:
        num=int(input("\nIngrese el numero de empleado: "))
        for maestro in listaMaestros:
            if maestro.numeroEmpleado == num:
                print(maestro)
    elif op==5:
        break
    else:
        print("\nError ingrese un numero valido\n")
    os.system("pause")
    os.system("cls")




    

    
