# los diccionarios de crean con llaves {} o con la funcion dict()
diccionario = dict(nombre="lucas", apellido="Dalto")

# las listas no pueden ser claves
diccionario = {("dalto","rancio"):"jaja"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])

print(diccionario)