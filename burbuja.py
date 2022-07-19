def llenar(lista,n): #llenar una lista vacía
    for i in range(n):#llenar la lista
        elemento=input("ingrese un valor ")
        lista.append(elemento)
    return lista
def ordenar():
    for i in range(n):
        for j in range(i+1, n):
            if lista[i]>lista[j]:
                temporal=lista[i]
                lista[i]=lista[j]
                lista[j]=temporal
    return lista

lista=[]
n=int(input("ingrese la cantidad de elementos de la lista: "))
lista=llenar(lista,n) #función que llena la lista vacía
print(lista)
lista=ordenar(lista,n) #función ordenar la lista
print(lista)