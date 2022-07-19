from multiprocessing.connection import deliver_challenge


def mergesort(lista):#ordena de manera de listas
    if len(lista) == 1:
        return lista[0]
    else:
        m=len(lista)//2
        izql=lista[:m]
        derl=lista[m:]
        print(m)
    mergesort(lista)
    mergesort(lista)
    listav=[]
    i=0
    j=0
    k=0

    while i<len(izql) and j<len(derl):
        if izql[i]<derl[j]:
            lista[k]=izql[i]
            i=i+1
        else:
            lista[k]=derl[j]
            j=j+1
        k=k+1

    while i<len(izql):
            lista[k]=izql[i]
            i=i+1
            k=k+1
    while j<len(derl):
            lista[k]=derl[j]
            j=j+1
            k=k+1
    return lista

            


lista=[1,2,5,7,8,9,2,12,2]
mergesort(lista)