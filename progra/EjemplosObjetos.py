class Persona:

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad = edad
    
    def __str__(self):# Nos ayuda a poder imprimir la informacion del objeto con un print
        return "Nombre :" + self.nombre + " edad :" + str(self.edad)

matrizPersona = [
    #Fila fuera una persona 
    #Columnas fueran sus datos
    ["Luis", 22],
    ["Brenda", 23]
]
'''
arregloNombrePersona = ["Luis", "Brenda"]
arregloEdadPersona = [22,23]
arregloPersona = []
persona = Persona("Luis",22)
arregloPersona.append(persona)
for persona in arregloPersona:
    print(persona)
    '''
'''
class SegurosTipo1:

    def __init__(self, sumaAsegurada, edad, fumar=None, duracion = 0):
        self.sumaAsegurada = sumaAsegurada
        self.edad = edad
        self.fumar = fumar 
        self.duracion = duracion

    def obtenerPrima(self):
        prima = self.sumaAsegurada / self.edad
        if self.fumar is not None and self.fumar == "S":
            prima = prima -100
        return prima

seguroPersona = SegurosTipo1(100000,25, "S")
print(seguroPersona.obtenerPrima())
'''


arreglo = [0,0,0]
matriz = [# n filas pero solo 3 columnas
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

class Matriz3Columnas:

    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
    
    def __str__(self):# Nos ayuda a poder imprimir la informacion del objeto con un print
        return str(self.valor1) + "," + str(self.valor2) + ","+ str(self.valor3)
'''
matrizDosXTres = [] #Toda lista objetos siempre tiene el comportamiendo de una matriz
matrizDosXTres.append(Matriz3Columnas(0,1,2))
matrizDosXTres.append(Matriz3Columnas(4,5,6))
matriz = [# n filas pero solo 3 columnas
    Matriz3Columnas(0,1,2),
    Matriz3Columnas(0,1,2),
]
for fila in matrizDosXTres:
    print(fila.valor3)
'''
class MatrizNColumnas:

    def __init__(self, valorN):#Valor N tiene que ser una lista o arreglo
        self.valorN = valorN

    def __str__(self):# Nos ayuda a poder imprimir la informacion del objeto con un print
        return str(self.valorN)

matrizN = []
matrizN.append(MatrizNColumnas([1,2,3,4]))
matrizN.append(MatrizNColumnas([5,6,7,8]))
for fila in matrizN:
    print(fila.valorN[2])