lista1=list()
lista2=list()
op='s'
print('lista 1 ')
while op == 's':
    a=input('\nIngrese elemento: ')
    lista1.append(a)
    op=input('\n¿Quiere ingresar otro elemento? \n\t[SI:s NO:n]: ')
print('lista 2 ')
op='s'
while op == 's':
    a=input('\nIngrese elemento: ')
    lista2.append(a)
    op=input('\n¿Quiere ingresar otro elemento? \n\t[SI:s NO:n]: ')
lista3=list(set(lista1))+lista2
print('\nlista 1 sin duplicados:\n',list(set(lista1)))
print('\nlista 2:\n',lista2)
print('\nlista 3:\n',lista3)
