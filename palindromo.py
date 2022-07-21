def palindromo(palabra): #se dejan los espacios entre funciones
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run(): #funcion principal por buenas prácticas
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:print("No es palíndromo")


if __name__ == '__main__': #punto de entrada de un programa de python
    run()