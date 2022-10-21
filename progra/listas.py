op1='s'
j=0
aprobados=0
reprobados=0
alumno=dict()
while op1 == 's':
    i=0
    calif=list()
    op2='s'
    while op2 == 's':
        print('\nIngrese calificacion',i+1,' de alumno',j+1,':')
        a=int(input())
        calif.append(a)
        op2=input('\n¿Quieres introducir otra calificacion? \n\t[SI:s NO:n]: ')
        i+=1
    prom=float(sum(calif))/float(len(calif))
    calif.append(prom)
    alumno[j]=calif
    op1=input('\n\n\t¿Quieres introducir otro alumno? \n\t[SI:s NO:n]: ')
    j+=1

for a in range(j):
    if alumno[a][-1] >= 70:
        aprobados+=1
    else:
        reprobados+=1
print('\nCalificaciones aprobatorias: ')
for a in range(aprobados):
    if alumno[a][-1] >= 70:
        print('\n',alumno[a][-1])

print('\nPasaron: %d \nReprobaron: %d' %(aprobados,reprobados))
