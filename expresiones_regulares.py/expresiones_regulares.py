import re

texto = """Hola maestro, estas en la cadena 1, como estas mi capitan?
Esta es la segunda linea de texto 2 3 y esta es la final dfinitiva mi capitan
1. hola todos
"""

# Busca todos los "Hola"
resultado = re.search("Hola",texto)

# Busca todos los "esta"  (flags=re.IGNORECASE ignora mayusculas y minusculas)
resultado2 = re.findall("Esta",texto, flags=re.IGNORECASE)

#\b - busca digitos numericos del 0 - 9
resultado = re.findall(r"\d", texto)

#\D - busca TODO MENOS digitos numericos del 0 - 9
resultado = re.findall(r"\D", texto)

#\w - Busca caracteres alfanumericos [a-z, A-Z, 0-9, _ ] TAMBIEN EL GUIN BAJO
# w minuscula
resultado = re.findall(r"\w", texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z  A-Z  0-9  _ ]
# M mayuscyla
resultado =  re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios tabs, saltos de linea
resultado = re.findall(r"\s", texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios tabs, saltos de linea
# mayuscula
resultado = re.findall(r"\s", texto)

# . -> busca TODO MENOS saltos de linea
resultado = re.findall(r'.',texto)

# \n -> busca saltos de linea
resultado = re.findall(r'.',texto)

#\ -> cancelamos caracteres especiales (son todos los que no son alfanumericos: ejempli: ? )

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f'\d\.\s', texto)

#busca el principio de una linea
#^ -> busca el comienzo de una linea
# quiero saber si Hola esta al principio de la cadena
# flags=re.M activa la multilinea
resultado = re.findall(f'^Hola', texto,flags=re.M)

# $ -> busca el final de una linea 
resultado = re.findall(f'esta$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}',texto)

#{n,m} -> al menos n,como maximo m
resultado = re.findall(r'\d{2,4}', texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}Hola', texto)

print(resultado)
