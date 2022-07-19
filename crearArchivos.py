#programa crear archivos de texto
#importar del módulo io el método open, para crear y abrir un archivo externo

from io import open
'''
#1. crear un archivo externo

archivo_texto=open("archivo.txt","w") 
#manipular el archivo: usar método write
frase="bueno dias"
archivo_texto.write(frase) #método que permite escribir en un archivo
archivo_texto.close() #cerrar el archivo en memoria'''

'''#2. para leer un archivo método read

archivo_texto=open("archivo.txt","r") #con el argumento r, se permite la lectura del archivo
leer=archivo_texto.read() 
archivo_texto.close() #cerrar el archivo en memoria'''

'''#3. para leer un archivo método readlines
archivo_texto=open("archivo.txt","r") 
lista_texto=archivo_texto.readlines() #extraer todas las líneas del archivo.txt y lo almacena en lista_texto
archivo_texto.close()
print(lista_texto[1]) #imprimir la lista creada apartir del archivo.txt'''

''' #4. agregar información a un archivo
archivo_texto=open("archivo.txt", "a") #permiso de agregar información al archivo.txt
archivo_texto.white("siempre es un gusto")
archivo_texto.close()
'''

''' #5. leer archivo desde la linea anterior
archivo_text=open("archivo.txt", "r") #permiso de lectura del archivo
leer=archivo_texto.read()#leer archivo desde cero
print("primera lectura ", leer)
leer=archivo_texto.read() #leer archivo desde fin de la linea anterior
print("segunda lectura leer", leer)'''

''' #6. reubicar puntero con el método seek(), parámetros de posición de ubicación del puntero
archivo_texto=open("archivo.txt", "r")
leer=archivo_texto.read()
print("primera lectura", leer)

archivo_texto.seek(70) #reubicar puntero desde la linea indicada
leer=archivo_texto.read(10) #leer archivo desde fin de la linea anterior
print("segunda lectura", leer)
'''

''' #7. sobre escribir texto
with open("archivo.txt", "r+") as archivo_texto: #permiso de lectura y escritura
    leer=archivo_texto.read()
    archivo_texto.write("titulo")'''

#print("archivo_texto.closed) no es necesario en el caso with

'''with open("archivo_texto.txt", "r") as archivo_texto: #permiso de solo lectura
    leer=archivo_texto.read()
    print(leer)'''

''' #8. buscar ruta especifica en archivos
with open("musica/bicicleta.text", "r") as bicicleta:
    lista=bicicleta.readlines()
    leer=lista[12:14]
    print(leer)
'''