#programa que calcula el valor del servicio mensual del consumo  de agua para N usuarios

n=int(input("ingrese la cantidad de usuarios "))
for i in range(n):
    codigo=input("ingrese codigo ")
    nombre=input("ingrese el nombre ")
    estado=input("su estado es :v de vigente o s de suspendido ")
    estrato=int(input("ingrese el número de su estrato: 1,2,3,4,5,6 "))
    consumo=float(input("ingrese el consumo "))
    if estado =="v":
        if estrato==1:
            tbasica=10000
        elif estrato==22:
            tbasica=20000
        elif estrato==3:
            tbasica=30000
        elif estrato==4:
            tbasica=45000
        elif estrato==5:
            tbasica=60000
        elif estrato==6:
            tbasica=70000
        else:
            print("Ingrese si estracto entre 1 a 6")
        vconsumo=consumo*200
        vpagar=tbasica+vconsumo
        print("nombre del usuario es: ",nombre)
        print("tarifa basica es: ",tbasica)
        print("el valor del consumo es: " ,vconsumo)
        print("el valor a pagar es: " ,vpagar)