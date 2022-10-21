class Alumnos:
    def __init__(self,matricula=None,nombre="",edad=None):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
    
    def asignar(self,matricula,nombre,edad):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nMatricula: " + str(self.matricula) + "\nEdad: " + str(self.edad) + "\n"

listaAlumnos = [0]
op=1
n=0
while op==1 : #While para seguir capturando alumnos
    i=1
    while i==1: #While para verificar si se repite la matricula
        i=0
        num=int(input("\nIngrese la matricula del alumno: \n>>"))
        listaAlumnos[n]=Alumnos(num)

        for j in range(len(listaAlumnos)-1):
            if listaAlumnos[j].matricula == num :
                print("\n\t\t\t ERROR\nLa matricula ingresado, ya existe. Intente de nuevo")
                i=1
    name=input("\nIngrese el nombre del alumno: \n>>")
    age=int(input("\nIngrese la edad del alumno: \n>>"))
    listaAlumnos[n].asignar(num,name,age)
    n+=1 
    
    op=int(input("\n\t¿Quiere ingresar los datos de otro alumno? [SI-1, NO-2]\n>>"))
    if op==2:
        break
    listaAlumnos.append(Alumnos())


print("\n\t\tREPORTE DE ALUMNOS")
#Ordenamos de menor a mayor la listaAlumnos por el metodo burbuja
for i in range(n):
    for j in range(i,n-1):
        if listaAlumnos[i].matricula > listaAlumnos[j+1].matricula : 
            m = listaAlumnos[i]
            listaAlumnos[i] = listaAlumnos[j+1]
            listaAlumnos[j+1] = m

#Imprimimos la lista
for alumno in listaAlumnos:
    print(alumno)
