#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print("Te pedi un numero salame, no te hagas el gracioso")
            print(f"ERROR: {e}") #para que nos diga el nombre de la exception type(e).__name__
        else:
            break
        #el finally se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")
            
    return resultado

print(sumar_dos())