num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
print("1 suma", "2 resta", "3 multiplicación", "4 división", sep="\n")
operacion=int(input("Ingrese el codigo de la operación: "))
s=num1+num2
r=num1-num2
m=num1*num2
d=num1/num2

if(operacion==1):
    print("El resultado de la suma es: ",s)
elif(operacion==2):
    print("El resultado de la resta es: ",r) 
elif(operacion==3):
    print("El resultado de la multiplicación: ",m)
elif(operacion==4):  
    if(num2==0):
        print("No es posible dividir por cero")
    else:
        d=num1/num2
        print("El resultado de la división: ",d)
else: 
    print("Opcion no valida")