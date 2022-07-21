numero=int(input("Ingrese un numero entero"))
par=0
impar=0
while numero!=-1:
    if numero%2==0:
        print(numero, "es par")
        par=par+1
    else:
        print(numero, "es impar")
        impar=impar+1
    numero=int(input("Ingrese un numero entero"))
print("cantidad de numeros pares ", par)
print("cantidad de numeros impares ", impar)