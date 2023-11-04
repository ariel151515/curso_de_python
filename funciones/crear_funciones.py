# creando una funcion simple
#def saludar():
#    print("Hola Ariel")
    
#saludar()

#convierte todo a minuscula
#sexo.lower()

#funciones con parametros
def saldar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivio = "reina"
    elif(sexo == "hombre"):
        adjetivio = "titan"
    else:
        adjetivio = "crack"
        
    print(f"Hola {nombre}, mi {adjetivio} ¿Como andas?")


saldar("Camila","mujer")


#crear una funcion que nos retorna valores
def crear_contraseña_random(num):
    chars = "soopihhdasda"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
password = crear_contraseña_random(98)
frase = f"Tu contraseña nueva es: {password}"
print(frase)

