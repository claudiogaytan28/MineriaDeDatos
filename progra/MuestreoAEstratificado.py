o=1
import numpy as np
import math 

def capturaDatos(L):
    datos = []
    ni = [] #Contiene las ni
    Ni = [] #Contiene el tamaño de poblacion de cada estrato
    for i in range(L): 
        print("\n\t\t ESTRATO %d"%(i+1))
        Ntemp = int(input("\n Tamaño de la poblacion en este estrato: "))
        Ni.append(Ntemp) 
        yj =[] #Arreglo temporal
        j = 0
        while True :
            print("\nDato %d"%(j+1))
            y = float(input(">>>")) #Captura de datos
            yj.append(y) #Arreglo temporal
            o = int(input("Otro? [1-Si,0-No]: ")) 
            if o == 0:
                break
            j += 1
        ni.append(j+1) #Arreglo con el tamaño de muestra de cada estrato
        datos.append(yj)
    return Ni,ni,datos
    

while True :
    print("\n \t\t MUESTREO ALEATORIO ESTRATIFICADO")
    op1 = int(input("Que dato encontrar: \n 1.-Media poblacional\n 2.-Total Poblacional\n 3.-Proporcion poblacional \n 4.-Tamaño de muestra\n [1-4]:"))
    L = int(input("\n Numero de estratos: "))

    if op1 == 1 or op1 == 2: #Calculo de media y poblacion
        Ni,ni,datos = capturaDatos(L)

        #print("\n\nj: ", j, "\n n:", ni,"\nDatos: ",datos)
        N = sum(Ni)  #Tamaño de la poblacion
        n = sum(ni)  #Tamaño de muestra total
        
        #Calculo de la media poblacional
        medias = []

        #Se guardan cada y barra 
        for estrato in datos:
            medias.append(np.mean(estrato)) 
        #Media estimada poblacional
        Miu = 1/N * sum(np.array(Ni)*np.array(medias)) 
        
        #Calculo de la varianza del estadistico
        indicadorVarianza = int(input("\n Varianza conocida? [0-No,1-Yeah]: "))
        #Varianza conocida
        sigmai = []
        if indicadorVarianza == 1:
            for i in range(L):
                print("\n\u03C3^2 de estrato %d"%(i+1)) #Sigma \u03C3
                sigma = float(input(">>>"))
                sigmai.append(sigma)
            #Varianza del estadistico
            varianza = 1/N**2 * sum(np.array(Ni)**2 * (np.array(Ni)-np.array(ni))/(np.array(Ni)-1) * np.array(sigmai)/np.array(ni))
            
        else: #Varianza desconocida
            for estrato in datos: #Obtencion de varianzas muestrales
                sigmai.append(np.var(estrato, ddof=1)) #Como es la varianza muestral, se cambia el parametro a ddof = 1
            #Estimacion de varianza del estadistico  
            varianza = 1/N**2 * sum(np.array(Ni)**2 * (np.array(Ni)-np.array(ni))/np.array(Ni) * np.array(sigmai)/np.array(ni))

        if op1 == 1: #Caso de media
            #Cota del estadistico
            B = 2 * np.sqrt(varianza)

            #Intervalo de confianza
            IC = [math.floor(Miu-B),math.ceil(Miu+B)]

            #Error Medio
            EM = B/Miu*100

            #Impresion de resultados
            print("\n \u03BC gorro: ", Miu, "\n Var(\u03BC): ",varianza," \n Cota B: ", B, "\n Intervalo de confianza: ",IC, "\n Error medio: ",EM,"%" )
            #Media por estrato
            print("\nEstimacion \u03BC por estrato: ")
            i=0
            for mediai in medias:
                print("\n \u03BC gorro ",i+1,":",mediai)
                i+=1
        
        else: #Caso de total poblacional

            #Estadistico del total poblacional
            t = N * Miu  

            #Como ya se calculo la varianza
            varianza = varianza * N**2 #ya que se relacionan por esa constante
            
            #Cota del estadistico
            B = 2 * np.sqrt(varianza)

            #Intervalo de confianza
            IC = [math.floor(Miu-B),math.ceil(Miu+B)]

            #Error Medio
            EM = B/Miu*100

            #Impresion de resultados
            print("\n t gorro: ", t, "\n Var(t gorro): ",varianza," \n Cota B: ", B, "\n Intervalo de confianza: ",IC, "\n Error medio: ",EM,"%" )
    
    elif op1 == 4: #Calculo del tamaño de muestra
        B = float(input("\nLimite de error de estimacion B: "))
        
        op2 = int(input("\n¿Que vas a estimar?: \n 1.-Media poblacional\n 2.-Total Poblacional\n 3.-Proporcion poblacional \n[1-3]: "))
        
        indicadorVarianza = int(input("\n Varianza conocida? [0-No,1-Yeah]: "))
        
        sigmai = []
        if op2 == 1 or op2 ==2 or op2 == 3 and indicadorVarianza == 1: #Varianza conocida
            Ni = [] #Contiene el tamaño de poblacion de cada estrato 
            for i in range(L):
                print("\n\t\t ESTRATO %d"%(i+1))
                Ntemp = int(input("\n Tamaño de la poblacion en este estrato: "))
                Ni.append(Ntemp) 
                print("\n\u03C3^2 de estrato %d"%(i+1)) #Sigma \u03C3
                sigma = float(input(">>>"))
                sigmai.append(sigma)

        
        elif op2 == 1 or op2 ==2 and indicadorVarianza == 0: #Varianza desconocida
            #Como no se conoce, se calcula pero se piden los datos
            Ni,ni,datos = capturaDatos(L)

            for estrato in datos: #Obtencion de varianzas muestrales
                sigmai.append(np.var(estrato, ddof=1)) #Como es la varianza muestral, se cambia el parametro a ddof = 1

        elif op2 == 3: #Captura de p gorro
            Ni = [] #Contiene el tamaño de poblacion de cada estrato
            pi = []
            for i in range(L):
                print("\n\t\t ESTRATO %d"%(i+1))
                Ntemp = int(input("\n Tamaño de la poblacion en este estrato: "))
                Ni.append(Ntemp) 
        
                print("\np gorro de estrato %d"%(i+1)) 
                p = float(input(">>>"))
                pi.append(p) 
            sigmai = np.array(pi)*(1-np.array(pi))

        op3 = int(input("\n¿Como vas a asignar el peso de las observaciones?: \n 1.-Con costos iguales\n 2.-Costos diferentes\n 3.-Proporcional Ni/N \n 4.-Equitativa 1/N\n[1-4]: "))
        
        if op3 == 1: #Calculo de wi con costos iguales
            wi = np.array(Ni)*np.sqrt(np.array(sigmai))/sum(np.array(Ni)*np.sqrt(np.array(sigmai)))        
        
        elif op3 == 2: #Calculo de wi con costos diferentes
            ci = []
            for i in range(L):
                print("\nCosto por observacion de estrato %d"%(i+1)) 
                c = float(input(">>>"))
                ci.append(c)
            wi = np.array(Ni)*np.sqrt(np.array(sigmai))/np.sqrt(np.array(ci))/sum(np.array(Ni)*np.sqrt(np.array(sigmai))/np.sqrt(np.array(ci)))        

        elif op3 == 3: #Calculo de wi proporcional
            wi = np.array(Ni)/sum(np.array(Ni))
       
        else: #Equitativa
            wi = [1/L]*L

        #Calculos de D
        if op2 == 1 or op2 == 3:
            D = B**2/4

        else:
            D = B**2/(4*N**2)

        n = math.ceil(sum(np.array(Ni)**2*np.array(sigmai)/np.array(wi))/(sum(Ni)**2*D + sum(np.array(Ni)*np.array(sigmai))))
        print("\n El tamaño de la muestra debe ser de: ", n)
        ni = n*np.array(wi)
        i=0
        print(wi)
        for muestra in ni:
            print("\n Tamaño de muestra para estrato ", i+1,": ", math.ceil(muestra))
            i+=1