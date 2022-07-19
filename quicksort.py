def partir(lista):
    pivote=lista[0]
    menores=[]
    mayores=[]
    for i in range(1,len(lista)):
        if lista[i]>pivote:
            menores.append(lista[i]) 
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores

def quicksort(lista):
    if len(lista)==1:
        return lista
    menores,pivote,mayores=partir(lista)
    ordenado=quicksort(menores)+[pivote]+quicksort(mayores)
    return ordenado

lista=[2,3,1]
print(lista)
print(quicksort(lista))