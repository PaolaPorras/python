nom=input("Ingrese el nombre completo, hasta fin para terminar")
personas=[]
cantidad=[]
while nom!="fin":
    cantp=len(nom.split())
    cantidad.append(cantp)
    personas.append(nom)
    nom=input("Ingrse el nombre completo, hasta fin para terminar")
print(personas)
print(cantidad)