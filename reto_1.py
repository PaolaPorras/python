codigoDelProducto=int(input())
nombreDelProducto=str(input())
cantidadComprada=float(input())
valorUnitario=float(input())
valorIva=0.19
valordelProducto=cantidadComprada*valorUnitario
valorFinal=valordelProducto+(valordelProducto*valorIva)

print(codigoDelProducto)
print(nombreDelProducto)
print(valordelProducto)
print(valorFinal)