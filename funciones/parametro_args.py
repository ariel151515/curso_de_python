#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9])

#utilizamos el parametro args
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resulatado = suma("Lucas", 5,3,9)
print(resulatado)


def suma_total(numeros):
    return suma(*numeros)

resulatado2 = suma_total(([5,3,9]))
print(resulatado2)
