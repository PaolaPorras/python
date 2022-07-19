def sumarL(lista):
    print(lista)
    if len(lista) == 1:
        return lista[0]
    else:
        lista = lista[0]+sumarL(lista[1:])
        print(lista)
        return lista

lista=[1,3,5,7,8,9]
print(sumarL(lista))