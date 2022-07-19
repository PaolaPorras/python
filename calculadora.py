#hacer una calculadora, que solicite 2 números y resuelva operaciones básicas definidas por el usuario
def sumar(a,b):
    #suma 2 valores
    if a==None or b==None:
        error="Error en los valores, ingrese nuevamente los valores"
        return error
    else:
        c=a+b
        return c
def restar(a=None,b=None):
    #restar un valor de otro
    if a==None or b==None:
        error="Error en los valores, ingrese nuevamente los valores"
        return error
    else:
        c=a-b
        return c
def multiplicar(a=None,b=None):
    #multiplicar un valor de otro
    if a==None or b==None:
        error="Error en los valores, ingrese nuevamente los valores"
    else:
        c=a*b
        return c
def dividir(a=None,b=None):
    #dvidir un valor de otro
    if a==None or b==None:
        error="Error en los valores, ingrese nuevamente los valores"
        return error
    else:
        c=a/b
        return c

n=int(input("ingrese numero de operaciones"))
for i in range(n):
    a=int(input("ingrese el valor de a: "))
    b=int(input("ingrese el valor de b: "))
    menu=int(input("ingrese la operación a realizar: 1.sumar 2.restar 3.multiplicar 4.dividir"))
    if menu==1:
        sum=sumar(a,b)
        print("a + b = ", sum)
    elif menu==2:
        rest=restar(a,b)
        print("a - c = ", rest)
    elif menu==2:
        mult=multiplicar(a,b)
        print("a * c = ", mult)
    elif menu==2:
        div=restar(a,b)
        print("a / b = ", div)
    else:
        print("la operación ingresada no corresponde a las opciones presentadas.")
