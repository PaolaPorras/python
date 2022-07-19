codigos=[]
cantidades=[]
tiposIVA=[]
valoresProducto=[]
valoresIVA=[]
valoresFinales=[]
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
N=int(input()) #cantidad de productos a procesar
for i in range(N):
    codigos.append(int(input()))
    cantidades.append(float(input()))
    tiposIVA.append(int(input()))
    valoresProducto.append(cantidades[i]*precios.get(codigos[i]))
    if tiposIVA[i]==1:
        valoresIVA.append(0)  #agregamos un cero porque esta exento de IVA
    elif tiposIVA[i]==2:
        valoresIVA.append(valoresProducto[i]*0.05)
    elif tiposIVA[i]==3:
        valoresIVA.append(valoresProducto[i]*0.19)
    valoresFinales.append(valoresProducto[i]+valoresIVA[i])
def ordenamiento():
    for i in range(1,N):
        for j in range(N-i):
            if codigos[j]>codigos[j+1]:
                codigos[j] , codigos[j+1] = codigos[j+1] , codigos[j]
                cantidades[j] , cantidades[j+1] = cantidades[j+1] , cantidades[j]
                valoresProducto[j] , valoresProducto[j+1] = valoresProducto[j+1] , valoresProducto[j]
                valoresFinales[j] , valoresFinales[j+1] = valoresFinales[j+1] , valoresFinales[j]
ordenamiento()
for i in range(N):
    print(codigos[i])
    print(articulos.get(codigos[i]))
    print(valoresProducto[i])
    print(valoresFinales[i])
print(sum(valoresFinales))
print(sum(valoresIVA))