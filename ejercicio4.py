#Escriba un algoritmo que basado en la tabla, permita leer un número e imprima e nombre correspondiente
#1. invierno, 2. verano, 3. otoño, 4. primavera

codEstacion=int(input("Ingrese el código de la estación: "))

if (codEstacion==1):
    print("Invierno")
elif (codEstacion==2):
    print("Verano")
elif (codEstacion==3):
    print("Otoño")
elif (codEstacion==4):
    print("Primavera")
else: 
    print("El codigo de estación ingresado es erróneo")