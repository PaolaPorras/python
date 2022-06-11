numero=int(input("Ingreso un npumero entero"))
par=0
impar=0
while True:
    if numero%2==0:
        print(numero," es par")
        par=par+1
        continue
    else:
        print(numero," es impar")
        impar=impar+1
    numero=int(input("Ingreso un numero entero"))
print("cantidad de numeros pares ", par)
print("cantidad de numero impares ", impar) 