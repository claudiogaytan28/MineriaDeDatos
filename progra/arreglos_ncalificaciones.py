def leer_arreglo(a):
    b=1
    while b==1:
        c=int(input("\n Ingrese la calificación:"))
        a.append(c)
        print("\n\n ¿Desea ingresar otra calificación? [Si:1 No:2]")
        b=int(input("\n >>"))
    return a

def prom_arreglo(a):
    suma=0
    for i in range(len(a)):
        suma=suma+a[i]
    prom=suma/len(a)
    print("\n\n Promedio : ",prom)
    
    return prom


def imp_arreglo(a):
    print("\n\n Calificaciones : \n")
    print(a)

arreglo=list()

leer_arreglo(arreglo)
prom_arreglo(arreglo)
imp_arreglo(arreglo)