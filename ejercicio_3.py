#Escriba un algoritmo que lea una edad y valide la entrada a una discoteca, si una persona es menor de 18 años, 
# el sistema debe mostrar en pantalla un mensaje de advertencia. 
# "usted no puede ingresar. Solo mayores de 18 años

edad=int(input("ingrese la edad "))
if (edad <18):
    print("Usted no puede ingresar. Solo mayores de 18 años")
else:
    print("Usted puede ingresar. Es mayores de 18 años")