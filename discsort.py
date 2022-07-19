def nombres(dat):
    return dat[nombres]
datos=[{
    "nombre": "pedro",
    "edad":18,
    "cod":1},
    {
    "nombre": "sandra",
    "edad":24,
    "cod":5},
    {
    "nombre": "oscar",
    "edad":14,
    "cod":2},
    {
    "nombre": "ana",
    "edad":50,
    "cod":4}
    ]

print("datos originales")
print(datos)
datos.sort(key=nombres)
print(datos)