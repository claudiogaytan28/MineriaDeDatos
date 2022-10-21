class Carro:

    def __init__(self, color, cantLLantas,velocidad, motor = None):
        self.color = color
        self.cantLLantas = cantLLantas
        self.motor = motor
        self.velocidad = velocidad

    def avanzar(self):
        respuesta = "velocidad " + str(self.velocidad)
        if  self.motor is not None and isinstance(self.motor,Motor): 
            respuesta = respuesta + " Velicida Maxima: " + str(self.motor.calcularVelocidadEstandar())
        print(respuesta)

class Motor:
    def __init__(self, nombre, velocidadMaxima):
        self.nombre = nombre
        self.velocidadMaxima  = velocidadMaxima
    
    def calcularVelocidadEstandar(self):
        return self.velocidadMaxima*.30

motor300 = Motor("Motor300",300)  
carro = Carro("Azul", 4 , 100,motor300)
carro.avanzar()
# Carro("Azul", 4 , 100,Motor("Motor600",600)).avanzar()
print(type(carro))
print(isinstance(motor300,Motor)) # preguntamos si el objeto es una instancia de la Clase Motor

