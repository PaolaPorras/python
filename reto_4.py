def orden( ordename:list() ):
    ordename.sort()
    for i in ordename:
        i.pop(0)
        for salida in i:
            for final in salida:
                print(final)


CantidadP = int(input())
ValorTotal = 0
ValorToltalIva = 0
codigos = []
nombres = []
CantidadCompra = []
Valor_U = []
tipoIva = []
iva = []
ValorProducto = []
ValorProductoF = []
ValorToltalIva = []
ivaT = 0

compras = []
for i in range(0,CantidadP):
    codigos.append(int(input()))
    nombres.append(input())
    CantidadCompra.append(float(input()))
    Valor_U.append(float(input()))
    tipoIva.append(int(input()))
    ValorProducto.append(CantidadCompra[i] * Valor_U[i])
    if tipoIva[i] == 1 :
        iva.append( 0 )
    elif tipoIva[i] == 2:
        iva.append(ValorProducto[i] * 0.05)
    else:
        iva.append(ValorProducto[i] * 0.19)
    ValorProductoF.append(ValorProducto[i] + iva[i])
    compras.append([[nombres[i]] ,[codigos[i], nombres[i], ValorProducto[i], ValorProductoF[i] ]])
    ValorToltalIva.append(iva[i])
    ivaT += ValorToltalIva[i]
    ValorTotal += ValorProductoF[i]
orden(compras)
print(ValorTotal)
print(ivaT)


""" print( codigos[i] )
print( nombres[i] )
print( ValorProducto[i] )
print( ValorProductoF[i] ) """