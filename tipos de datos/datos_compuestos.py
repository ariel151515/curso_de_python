# Creando una lista (se puede modificar)
lista = ["Ariel Gentile", "Canal de You Tube", True, 1.85]

# Creando una tupla (no se puede modificar)
tuple = ("Ariel Gentile", "Canal de You Tube", True, 1.85)

# Creando un conjunto (set), se puede modificar pero los
# elementos no y no permite repetir valores o no almacena datos duplicados
conjunto = {"Ariel Gentile", "Canal de You Tube", True, 1.85}

# Creando un diccionario (dict)
diccionario = {
    'nombre': "Jesus Ariel",
    'apellido': "Gentile",
    'esta_emocionado': True,
    'altura': 1.65
}

# Crear un set usando llaves
mi_set = {1, 2, 3, 4, 5}

# Crear un set usando la función set()
otro_set = set([3, 4, 5, 6, 7])

# Esto es valido
lista[3] = "Maquinola"

# Esto no es valido
# tupla[3] = "Maquinola"

print(lista[0])
print(tupla[1])
print(diccionario['nombre'])
