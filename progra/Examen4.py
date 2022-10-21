class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nEdad: " + str(self.edad) + "\nMatricula: " + str(self.matricula) + "\n"

class Materias:
    def __init__(self,nombreMat,cal):
        self.nombreMat = nombreMat
        self.cal = cal
    def __str__(self):
        return "Materia: " + str(self.nombreMat) + "\nCalificacion: " + str(self.cal) + "\n"

op=1

Data=[]

n=0
while op == 1:
    op1=1
    Data.append([])
    name=input("\nIngrese el nombre del alumno %d: " %(n+1))
    age=int(input("\nIngrese la edad del alumno %d: " %(n+1)))
    matri=int(input("\nIngrese la matricula del alumno %d: " %(n+1)))

    #Data[n].append(Alumnos(name,age,mat))
    
    matAndCalif=[]
    i=0
    while op1 == 1 :#Creacion de materias    
        mat = input("\nIngrese la materia %d: " % (i+1))
        calif = int(input("\nIngrese la calificacion: "))
        matAndCalif.append(Materias(mat,calif))
        op1=int(input("\n\t¿Quiere ingresar otra materia? [SI-1, NO-2]\n>>"))
        i+=1
        
    Data[n].append(Alumnos(name,age,matri))
    Data[n].append(matAndCalif)
    n+=1
    op=int(input("\n\t\t¿Quiere ingresar otro alumno? [SI-1, NO-2]\n>>"))

print("\n\t\tREPORTE")
i=0
for fila in Data:
    print("\n\tAlumno %d:"%(i+1))
    print(fila[0])
    s=0
    for materia in fila[1]:
        print(materia)
        s=s+materia.cal
    print("Promedio Final: ", s/len(fila[1]))
    i+=1


    