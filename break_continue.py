
def run():
    #imprimir todos los numeros pares desde 0 a 1000
    # for contador in range(1000):
    #     if contador %2 != 0:
    #         continue #continua el ciclo
    #     print(contador)
        
    # for i in range(1000):
    #     print(i)
    #     if i == 678:
    #         break #rompe el ciclo

    texto = input('Escribe un texto:')
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == '__main__':
    run()
