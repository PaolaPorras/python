#continuidad reto 2
cantidadProducto = int(input())
valorTotal=0
valorTotalIva=0
for i in range(0,cantidadProducto):
    codigoDelProducto=int(input())
    nombreDelProducto=str(input())
    cantidadComprada=float(input())
    valorUnitario=float(input())
    tipoIva=int(input())

    valorProducto=cantidadComprada*valorUnitario
    if tipoIva==1:
            iva=0
    elif tipoIva==2:
        iva = valorProducto*0.05
    elif tipoIva==3:
        iva = valorProducto*0.19
    valordelProductoFinal=valorProducto+iva
    print(codigoDelProducto)
    print(nombreDelProducto)
    print(valorProducto)
    print(valordelProductoFinal)
    valorTotal += valordelProductoFinal
    valorTotalIva += iva
  
print(valorTotal)
print(valorTotalIva)