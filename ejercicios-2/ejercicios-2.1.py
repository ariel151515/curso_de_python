#falto el profe y los pibes van a armar la clase.

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: ")) 
        compañero = (nombre, edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
        
    #ordenamos de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[2] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor 
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetaos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(5)

# mostramos el resultado
print(f"El profesor es: {asistente} y su asistente es {asistente}")
