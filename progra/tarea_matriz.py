
def llenadoMatriz(matrix):
    #For para la creación y relleno de la matriz.
    for i in range(n):
        matrix.append([]) #Creamos la columna cada una de las filas con el .append
        for j in range(m):
            matrix[i].append(int(input("Ingrese el elemento [%d][%d]: " % (i, j)))) #Creamos las columnas de la fila y rellenamos al mismo tiempo
    return matrix

def sumRowCol(matrix):
    #For para la suma de los renglones 
    for i in range(len(matrix)): 
        s=sum(matrix[i])
        matrix[i].append("="+str(s))
    a=[0]*(len(matrix[0]))
    #For para la suma de las columnas
    for j in range(len(matrix[0])-1):
        s=0
        for i in range(len(matrix)):
            s=s+matrix[i][j]
        a[j]="="+str(s)
    a[j+1]=" "
    matrix.append(a)
    return matrix

def ImprimirMatriz(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print()

    

n=int(input("Ingrese el numero de renglones: "))
m=int(input("\nIngrese el numero de columnas: "))

matriz = []

matriz=llenadoMatriz(matriz)
matriz=sumRowCol(matriz)
ImprimirMatriz(matriz)



