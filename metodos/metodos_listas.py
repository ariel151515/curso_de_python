# creando una lista con list()
lista = list([34, 56, 23, True])

# devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# agregando elementos a la lista con append
lista.append(65)

# agregando elementos a la lista en un indice especifico
lista.insert(2, "TOMA")

# agregando varios elementos a la lista
# (Los para metros se pasan dentro de los corchetes)
lista.extend([False, 2030])

print(len(lista))

# eliminamos un elementos de la lista por su indice
lista.pop(0)

# eliminamos el ultimo elementos de la lista
lista.pop(-1)

# eliminamos el ante ultimo elementos de la lista
lista.pop(-2)

# removiendo un elemento de la lista segun su valor
lista.remove("TOMA")

# Ordena los elementos de forma asendente
lista.sort()

# Ordena al revez o en reversa
# lista.sort(reverse=True)

# Invierte los elementos de una lista
lista.reverse()

# Eliminando todos los elementos de una lista
# lista.clear()


print(lista)

print(len(lista))
