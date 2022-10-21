#5  BUSQUEDAS
def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas

especialidad = ["Consultas generales","Cardiologia","Pediatria","Urgencias","Cirugia"]

op5 = 4
while op5 != 1 and op5 != 2 and op5 != 3: #While para controlar el menu
    op5 = int(input("\n\tBUSQUEDAS\n¿Que requiere buscar? \n 1-Habitaciones disponibles \n 2-Pacientes \n 3-Doctores \n>>>[1-3]: "))
    
    if op5 == 1: #Disponibilidad de las habitaciones
        nombreH = "HABITACIONES.csv"
        habitaciones = leerArchivo(nombreH)
        o = None
        while o == None: 
            piso = int(input("\nNumero de piso a buscar: "))
            o = None
            print("\n\tHOSPITAL Y CLINICA OCA, S.A. DE C. V.")
            print("\nPiso: " + str(piso))
            print("Numero de habitacion")
            for linea in habitaciones:
                habitacion = linea.strip().split(",")
                if habitacion[2] == str(0) and habitacion[0] == str(piso): #0 significa que si esta disponible
                    print(habitacion[1] + "\tDisponible") #Informacion de la habitacion 
                    o = 1
            if o == None:
                print("\nNo hay habitaciones disponibles")

    elif op5 == 2 : #Informacion de los pacientes 
        o = int(input("\n\tPACIENTES\n¿Que requiere buscar? \n 1-Todos los pacientes \n 2-Por piso en especifico \n>>>[1-2]: "))
        nombrePC = "PACIENTECONSULTA.csv"
        consultados = leerArchivo(nombrePC)

        nombrePI = "PACIENTEINGRESO.csv"
        ingresados = leerArchivo(nombrePI)

        if o == 1: #Todos los pacientes
            print("\n\tHOSPITAL Y CLINICA OCA, S.A. DE C. V.")
            for linea in consultados: #consultados
                consultado = linea.strip().split(",")
                print("\nNombre: " + consultado[1] + "\nNSS:" + consultado[4] + "\nEnfermedad: " + consultado[5] + "\nConsultorio: " + consultado[6])

             
            for linea in ingresados: #ingresados
                ingresado = linea.strip().split(",")
                print("\nNombre: " + ingresado[1] + "\nNSS:" + ingresado[4] + "\nHabitacion: " + ingresado[6] + "\nDescripcion: " + ingresado[7] )
        
        elif o == 2: #Por piso
            o = None
            while o == None:
                o = None
                piso = int(input("\nNumero de piso a buscar: "))
                if piso == 1: #Se separa el piso 1 del resto porque son consultorios
                    print("\n\tHOSPITAL Y CLINICA OCA, S.A. DE C. V.")
                    print("\nPiso " + str(piso) + ": "+ especialidad[piso-1])

                    for linea in consultados:
                        paciente = linea.strip().split(",")
                        if int(paciente[6]) >= 10 * (piso -1) + 1 and int(paciente[6]) <= 10 * piso :
                            print("\nNombre: " + paciente[1] + "\nNSS:" + paciente[4] + "\nEnfermedad: " + paciente[5] + "\nConsultorio: " + paciente[6])
                    o = 1

                elif piso > 1 and piso < 6: #Del piso 2 al 5 son habitaciones de internos
                    print("\n\tHOSPITAL Y CLINICA OCA, S.A. DE C. V.")
                    print("\nPiso " + str(piso) + ": "+ especialidad[piso-1]) 
                    
                    for linea in ingresados:
                        paciente = linea.strip().split(",")
                        if int(paciente[6]) >= 10 * (piso -1) + 1 and int(paciente[6]) <= 10 * piso :
                            print("\nNombre: " + paciente[1] + "\nNSS:" + paciente[4] + "\nHabitacion: " + paciente[6] + "\nDescripcion: " + paciente[7])
                    
                    o = 1
                
                else:
                    print("\nError no existe el piso, intente de nuevo\n")
                    continue
        else:
            print("\nError en la opcion ingresada, intente de nuevo")
    
    elif op5 == 3: #Lista de doctores
        print("\n\tHOSPITAL Y CLINICA OCA, S.A. DE C. V.")
        nombreD = "DOCTOR.csv"
        doctores = leerArchivo(nombreD)

        for linea in doctores:
            doctor = linea.strip().split(",")
            print("\nDoctor: " + doctor[1] + "\nEspecialidad: " + doctor[2] + "\nCorreo: " + doctor[3] + "\nTelefono: " + doctor[4] + "\nTarifa: " + doctor[5])

    else:
        print("\nError en la opcion ingresada, intente de nuevo")
