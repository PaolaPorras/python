def run():
    mi_diccionario = {
        'llave 1': 1,
        'llave 2': 2,
        'llave 3': 3,
    }

    poblacion_paises = {
        'Argentina':44938712,
        'Brasil' : 210147125,
        'Colombia' : 50372424
    }

    for pais in poblacion_paises.keys(): #devuelve las llaves del diccionario
        print(pais)

    for pais in poblacion_paises.values(): #devuelve los valores de las llaves las llaves del diccionario
        print(pais)

    for pais, poblacion in poblacion_paises.items(): #devuelve las llaves y sus valores del diccionario
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')




if __name__ == '__main__':
    run()