diccionario = {
    "nombre": "lucas",
    "apellido": "Dalto",
    "subs": 1000000
}

for key in diccionario:
    print(key)
    
# accedemos a la clave valor (nos devuelve una tupla con par clave valor)
for key in diccionario.items():
    print(key)
    
# accedemos a la clave valor (nos devuelve una tupla con par clave valor)
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es:{value}')