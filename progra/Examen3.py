class MatrizNColumnas:

    def __init__(self, valorN):
        self.valorN = valorN


n=int(input("\nIngrese la dimension de la matriz cuadrada: "))
matrixN = []
sumaRenglon = []
sumaColumna = []

for i in range(n): #Llenado de matriz
    fila = []
    for j in range(n):
        fila.append(int(input("Ingrese el elemento [%d][%d]: " % (i, j)))) 
    matrixN.append(MatrizNColumnas(fila))

for fila in matrixN: #Suma de renglones
    sumaRenglon.append(sum(fila.valorN))

for j in range(n): #Suma de columnas
    s=0
    for i in range(n):
        s=s+matrixN[i].valorN[j]
    sumaColumna.append(s)

print("\nMatriz original")
for i in range(len(matrixN)): #Impresion de la matriz original
    for j in range(len(matrixN[0].valorN)):
        print(matrixN[i].valorN[j], end="\t")
    print()

print("\nLista con la suma de los renglones: ",sumaRenglon)
print("Promedio: ", sum(sumaRenglon)/len(sumaRenglon))


print("\nLista con la suma de las columnas: ",sumaColumna)
print("Promedio: ", sum(sumaColumna)/len(sumaColumna))
