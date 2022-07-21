N=int(input())
total_ventas=0
total_iva=0
codigo=[]
nombre=[]
cantidad=[]
valor_unitario=[]
tipo=[]
valor_producto=[]
iva=[]
valor_final=[]
for i in range(N):
    codigo.append(int(input()))
    nombre.append(input())
    cantidad.append(float(input()))
    valor_unitario.append(float(input()))
    tipo.append(int(input()))
print(len(codigo))
print(len(nombre))
print(len(cantidad))
print(len(valor_unitario))
print(len(tipo))
for i in range(N):
    valor_producto.append(cantidad[i]*valor_unitario[i])
    if tipo[i]==1:
        iva.append(0)
    elif tipo[i]==2:
        iva.append(valor_producto[i]*0.05)
    else:
        iva.append(valor_producto[i]*0.19)
    valor_final.append(valor_producto[i]+iva[i])
    total_iva+=iva[i]
    total_ventas+=valor_final[i]
    print(codigo[i])
    print(nombre[i])
    print(valor_producto[i])
    print(valor_final[i])
print(total_ventas)
print(total_iva)