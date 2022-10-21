#En Python no existen los arreglos ni las matrices
#En python existen las colecciones de datos siendo las Listas las dominantes
# lista = list() o []
arreglo = [1,2,3,4] # es una lista comportandose como arreglo
#Opcion manejar como lista.
'''
entrada = int(input("Introduce la cantidad de elementos del arreglo: "))
array = []
for i in range(entrada):
    dato = input('Introduce el dato %d del arreglo: ' % (i))
    array.append(int(dato))
print(array)'''
#Solucion dada un arreglo ya creado
'''
cantidad = int(input("Introduce la cantidad de elementos del arreglo: "))
array = [0] * cantidad
for i in range(cantidad):
    dato = input('Introduce el dato %d del arreglo: ' % (i))
    array[i] = int(dato)
print(array)
'''

def tamañoArreglo(arreglo):
    return len(arreglo)

def crearArreglo(n):
    arreglo = [0] * n
    return arreglo

def crearArregloSets(n):
    arreglo = set()
    for i in range(n):
        arreglo.add(i)
    return arreglo

def buscarPosicionArreglo(arreglo, dato):
    for i in range(tamañoArreglo(arreglo)):
        if arreglo[i] == dato:
            return i
def existeEnArreglo(arreglo, dato):
    if dato in arreglo:
        return True
    else:
        return False

# array = [1,2,3,4,5]
# print(array.index(1))
# array = crearArreglo(5)
# print(existeEnArreglo(array,10))
# arregloSet = crearArregloSets(5)
# print(arregloSet)

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matriz)
'''
for fila in matriz:#matriz[0] -> matriz[1] -> matriz[2]
    print(fila)
for fila in matriz:#matriz[0] -> matriz[1] -> matriz[2]
    for columna in fila:#fila[0] -> fila[1] -> fila[2]
        # print(columna)
        pass
filas = len(matriz)
columnas = len(matriz[0])
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print()
'''
#print(matriz[2][2])
#matriz[2][2] = 5
#print(matriz[2][2])
'''
matrizCeros = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
matrizCeros = [[0] * 3] * 3  # forma simplificada
matrizCeros = []
for i in range(3):
    columnas = [0] *3
    matrizCeros.append(columnas)
matrizCeros = [0] *3
for i in range(3):
    columnas = [0] *3
    matrizCeros[i] = columnas

print(matrizCeros)
'''
def imprimiMatriz(matriz):
    for fila in matriz:#matriz[0] -> matriz[1] -> matriz[2]
        print(fila)

def creacionMatriz(n,m):
    matrizCeros = []
    for i in range(n):
        columnas = [0] *m
        matrizCeros.append(columnas)
    return matrizCeros

def creacionMatrizSimplificada(n,m):
    matrizCeros = [[0] * m] * n
    return matrizCeros

def filas(matriz):
    return len(matriz)

def columnas(matriz):
    return len(matriz[0])

def inicializarMatriz(matriz, dato):
    for i in range(filas(matriz)):
        for j in range(columnas(matriz)):
            matriz[i][j] = dato
    # return matriz

def crearMatrizConValor(n,m,valor=None):
    dato = 0
    if valor is not  None:
        dato = valor
    matrizCeros = [[dato] * m] * n
    return matrizCeros

def crearMatrizConValorEnteros(n,m,valor=0):
    matrizCeros = [[valor] * m] * n
    return matrizCeros

matriz = creacionMatrizSimplificada(4,4)
imprimiMatriz(matriz)
inicializarMatriz(matriz, 5)
print()
imprimiMatriz(matriz)
matrizValor = crearMatrizConValorEnteros(2,2)
imprimiMatriz(matrizValor)
#Explicacion parametros 
'''    
def cambiarValor(entero):
    entero = 5
def incrementarVerctor(vector2):
    vector2.append(5)

numero = 4
vector = [1]
print(vector)
cambiarValor(numero)
incrementarVerctor(vector)
print(vector)
'''
