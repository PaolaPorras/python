#Escriba un algoritmo que lea un numero y determine si es positivo o negativo

numero=int(input("ingrese el número: "))
if numero<0:
    print("el número es negativo")
elif numero>0:
    print("el número es positivo")
else: 
    print("el número es cero")