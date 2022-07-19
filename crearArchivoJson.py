#programa para crear un archivo json, partiendo de tipo lista
#importar el módulo json

import json

lista=[10,20,30,40,50,60,70,80,90] #estructura para crear archivo
diccionario={"1":"lapiz","2":"borrador","3":"cuaderno","4":"lapicero"}

'''#1. instrucciones para crear el archivo - apertura - crearlo - método open
with open("lista.json", "w") as file:
    json.dump(lista, file)

print(file.closed)'''


'''#2. instrucciones para crear un diccionario
with open("diccionario.json", "w") as archivo:
    json.dump(diccionario, archivo)'''


'''#3. Leer un archivo json creado apartir de una lista
with open("lista.json", "r") as file:
    leer=json.load(file)
    #print(leer) #mostrar toda a información guardada en la variable
    for i in range(len(leer)):
        print([1])'''

'''#4. leer un archivo json creado apartir de un diccionario
with open("diccionario.json", "r") as archivo:
    dic=json.load(archivo)
    print(dic[""])
    '''

'''#5. programa para saber si existe un archivo o si no lo cree
archivo="hola.json"

try:
    with opn(archivo,"r") as file:
        leer=json.load(file)
        print(leer)
except FileNotFoundError:
    with open(archivo,"w") as file:
        jsondump(diccionario.file)
else:
    print(leer)
    #print(leer["3"])
'''