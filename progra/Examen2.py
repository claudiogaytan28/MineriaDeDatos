class MatrizNColumnas:

    def __init__(self, valorN):
        self.valorN = valorN


m=int(input("Ingrese el numero de renglones: "))
n=int(input("\nIngrese el numero de columnas: "))
matrixN = []

for i in range(m): #Llenado de matriz
    fila = []
    for j in range(n):
        fila.append(int(input("Ingrese el elemento [%d][%d]: " % (i, j)))) 
    matrixN.append(MatrizNColumnas(fila))

print("\nMatriz original")
for i in range(m): #Impresion de la matriz original
    for j in range(n):
        print(matrixN[i].valorN[j], end="\t")
    print()

print("\nMatriz orden invertido")
for i in range(len(matrixN)): #Impresion de la matriz orden invertido
    matrixN[i].valorN.reverse()
    for j in range(len(matrixN[0].valorN)):
        print(matrixN[i].valorN[j], end="\t")
    print()
