def leer_arreglo(a):
    for i in range(0,10):
        n=0
        n=int(input("\n Ingrese la calificación : "))
        a.append(n)    
    return a

def prom_arreglo(a):
    suma=0
    for i in range(0,10):
        suma=suma+(a[i]/10)
    print("\n\n Promedio : ",suma)
    return suma

def imp_arreglo(a):
    print("\n\n Calificaciones : \n")
    print(a)

arreglo=list()

leer_arreglo(arreglo)
prom_arreglo(arreglo )
imp_arreglo(arreglo)








    
