def buscar(numeros, busca):
    for i in range(len(numeros)):
        if busca==numeros[i]:
            return i
        return -1

numeros=[2,4,1,5,30,6,3,6,8,9,12,20]
busca=35
x=buscar(numeros,busca)
if x==-1:
    print("no encontrado")
else:print("encontrado en posición ",x)