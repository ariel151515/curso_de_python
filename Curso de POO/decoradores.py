def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Dalto")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

#Lo de arriba es exactamente lo mismo que lo de abajo

# @decorador
# def saludo():
#     print("Hola Dalto como andas")
    
# saludo()

