
"""
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    compañeros.append(cantidad_de_compañeros)
    return compañeros

resultado = obtener_compañeros('Juan','Pedro')

print(resultado)
"""


"""
def obtener_compañeros_dos(*nombres):
    compañeros = list(nombres)
   return compañeros

resultado = obtener_compañeros('Juan','Pedro')
print(resultado)
"""


"""
def obtener_compañeros(*nombres):
    nombre_uno = nombres[1][0]
    return nombre_uno

resultado = obtener_compañeros('Juan','Pedro')
print(resultado)
"""


"""
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: ")) 
        compañero = (nombre, edad)
        compañeros.append(compañero)
        
    return compañeros

resultado = obtener_compañeros(2)
print(resultado)
"""


def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []

    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: ")) 
        compañero = (nombre, edad)
        compañeros.append(compañero)
        
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    
    # accedemos al ultimo elemento que es el profesor y con [0] a su nombre
    profesor = compañeros[-1][0]
    return asistente,profesor

#estamos desempaquetando los valores de la funcion
asistente, profesor = obtener_compañeros(5)
print(f"El asistente es: {asistente} y el profesor es {profesor}")
