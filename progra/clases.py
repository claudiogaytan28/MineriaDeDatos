'''
class Carro :
    color = ""
    cantLlantas = 4

    def acelerar(self):
        print("el carro acelera es de color:" + self.color)

carro1 = Carro()
carro1.color = "rojo"
carro1.acelerar()
carro2 = Carro()
carro2.color = "Azul"
carro2.acelerar()
carro1.acelerar()
'''

class Carro:
    #Atributo va a ser compartido por todos los objetos
    cantLlantas = 4
    
    def asignarColor(self, color):
        self.color = color # crea el atributo color y le asigna el color que se le manda
    
    def imprimiColor(self):
        print(self.color) # imprime el atributo color siempre y cuando este creado y tenga valor

carro1 = Carro()
# carro1.color = "rojo" # crea el atributo color y le asigna un color
# carro1.asignarColor("azul")
# carro1.imprimiColor() # no funcionara si no asignamos el atributo color antes
# print(carro1.color)# no funcionara si no asignamos el atributo color antes
# print(carro1.aceleracion) No se puede porque no has creado el atributo aceleracion

class Persona :

    #Atributos cantOjos tipoNariz colorOjos colorCabello, altura, peso, edad, nombre
    cantOjos = 2
    cantBrazos = 2


    def __init__(self, nombre = "", edad = 0, colorOjos = "", peso = 0.0):
        self.nombre = nombre
        self.edad = edad
        self.colorOjos = colorOjos
        self.peso = peso

    def asignarNombreAndEdad(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def inicializarObjeto(self, nombre, edad, colorOjos, peso):
        self.nombre = nombre
        self.edad = edad
        self.colorOjos = colorOjos
        self.peso = peso
  
    #Metodos hacerEjercicio hablar caminar comer dormir
    def informarObjeto(self):
        print("Soy " + self.nombre + " tengo " + str(self.cantOjos) + " ojos son de color " + self.colorOjos )

    def informarNombreEdad(self):
        print("Soy " + self.nombre + " tengo la edad de "  + str(self.edad))
'''
persona1 = Persona('Eduardo', 24, 'Cafe' , 70)
persona2 = Persona()
persona2.asignarNombreAndEdad("Luis", 22)
# persona2.nombre = "Luis"
# persona2.edad = 22
# persona1.inicializarObjeto('Luis', 24, 'Cafe' , 70)
print(persona2.nombre,persona2.edad)
# persona1.informarObjeto()
'''
#Leer el nombre y edad de n personas
listaPersonas = []
opc = 's'
while opc == 's':
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    persona = Persona()
    persona.asignarNombreAndEdad(nombre,edad)
    listaPersonas.append(persona)
    opc = input("Quieres introducir otro si(s) no(n)")
# print(listaPersonas)

for persona in listaPersonas:
    print(persona.nombre)
    # persona.informarNombreEdad()

