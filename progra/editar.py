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