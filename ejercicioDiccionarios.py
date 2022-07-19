def validar():
    while True:
        try:
            n=int(input("la cantidad de artículos "))
            break
        except:
            error="error de cantidad, ingrese un valor entero"
            print(error)
        return n

n=validar()
articulos={1:"lapiz", 2:"cuadernos", 3:"borrador", 4:"calculadora", 5:"escuadra"}
valores={1:2500, 2:3800, 3:1200, 4:3500, 5:3700}
valortotalcompra=0

for i in range(n):
    codigo=int(input("ingrese el código "))
    cantidad=int(input("Ingrese la cantidad "))
    valoru=valores.get(codigo,"código no valido")
    valorcompra=cantidad*valoru
    valortotalcompra+=valorcompra
    nombre=articulos.get(codigo)
    print(f"nombre articulo {nombre} la cantidad {cantidad}")
    print("valor unitario ", valoru)
    print("valor compra", valorcompra)
    print(f"valor tipo de las compras es ${valortotalcompra:, 2f}")
