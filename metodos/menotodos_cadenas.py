cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

# dir() mustra las distintas cosas que podesmo hacer con el
# tipo de dato, en este caso un texto
print(dir(cadena1))

resultado = dir(cadena1)

# convierte a mayuscula
resultado1 = cadena1.upper()

# convierte a minuscula
resultado2 = cadena1.lower()

# primer letra en mayuscula
resultado3 = cadena1.capitalize()

# buscamos una cadena en otra cadena (devuelve el indice)(si no encunetra
# nada nos devuelve -1)
resultado4 = cadena1.find("o")

# buscamos una cadena en otra cadena (devuelve el indice)(si no encunetra
# nada nos un error)
resultado5 = cadena1.index("o")

# devolvemos True o False si es un numero
resultado6 = cadena1.isnumeric()

# verifica si es alfanumerico
resultado7 = cadena1.isalpha()

# nos devuelvela cantidad de veces que coincida
resultado8 = cadena1.count("a")

# contamos cuantos caracteres tiene una cadena
resultado9 = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si
# es asi devuelve True / False
resultado10 = cadena1.startswith("Hola")

# verificamos si una cadena empieza con otra cadena dada, si
# es asi devuelve True / False
resultado11 = cadena1.endswith("Hola")

# remplaza un pedazo de la cadena dada por otra dada
resultado12 = cadena1.replace("Hola", "Holisss")

# separar cadenas con la cadena que le pasamos
resultado13 = cadena1.split(",")


# print(resultado1)
# print(resultado2)
# print(resultado3)
# print(resultado4)
# print(resultado5)
# print(resultado6)
# print(resultado7)
# print(resultado8)
# print(resultado9)
# print(resultado10)
# print(resultado11)
# print(resultado12)
print(resultado13)


# comprueba el tipo de dato
print(isinstance(resultado13, list))
