diccionario = {
    "nombre": 'lucas',
    "apellido": 'dalto',
    "subs": 1000000
}

# devuelve las claves
claves = diccionario.keys()

# devuelve el valor u obteniendo un elemento con get
claves = diccionario.get("apellido")

# eliminando todo del diccionario
diccionario.clear()

# eliminando un elemento del diccionario
diccionario.pop("nombre", "subs")

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)
print(diccionario_iterable)
