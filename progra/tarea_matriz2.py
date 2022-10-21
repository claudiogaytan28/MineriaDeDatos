def llenadoMatriz(matrix):
    #For para la creación y relleno de la matriz.
    for i in range(n):
        matriz.append([]) #Creamos la columna cada una de las filas con el .append
        for j in range(m):
            matriz[i].append(int(input("Ingrese el elemento [%d][%d]: " % (i, j)))) #Creamos las columnas de la fila y rellenamos al mismo tiempo
    return matrix

def sumRowCol(matrix):
    for i in range(len(matrix)):
        s=sum(matrix[i])
        matrix[i].append(s)
    a=[0]*(len(matrix[0]))
    for j in range(len(matrix[0])-1):
        s=0
        for i in range(len(matrix)):
            s=s+matrix[i][j]
        a[j]=s
    matrix.append(a)
    return matrix

#def ImprimirMatriz(matrix):
'''
    No es necesaria la función crearMatriz
    ya que la matriz se va creando dentro
    del for con el .append
'''    

n=int(input("Ingrese el numero de renglones: "))
m=int(input("\nIngrese el numero de columnas: "))

matriz = [] #Declaramos la matriz nula, 0 filas, 0 columnas
matriz=llenadoMatriz(matriz)
print(matriz)
#matriz=sumRowCol(matriz)
#ImprimirMatriz(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()



