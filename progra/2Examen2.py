"""
2.	Escribir un programa que lea un archivo txt que contendrá una secuencia de números 
separados por diagonales “1/2/3/4”, el programa debe pedir el nombre del archivo 
leerlo y después desplegar el contenido en pantalla, así como la suma y el promedio 
"""
nombreArchivo = input("\nIngrese el nombre del archivo: ")

secuencia = open(nombreArchivo,'r')
numeros = secuencia.readlines()

print("\n Secuencia de numeros:")
for n in numeros: #For para crear una lista con los numeros del archivo
    print(n)
    numero = n.strip().split("/")

listaNumeros = []
for n in numero: #For para modificar cada cadena y convertirla a numero
    listaNumeros.append(int(n))

suma = sum(listaNumeros)
promedio = suma/len(listaNumeros)

print("Suma: " + str(suma) + "\nPromedio: " + str(promedio))



