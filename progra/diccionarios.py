diccionario=dict()
op='s'
while op == 's':
    color=input('\nIngrese color: ')
    frase=input('\nIngrese una frase con el color: ')
    diccionario[color]=frase
    op=input('\n¿Quiere ingresar otro color? \n\t[SI:s NO:n]: ')
print(diccionario)
