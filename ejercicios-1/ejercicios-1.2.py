#le pedimos al usuario que nos diga una frase o varias
frase = input("Decime una frase y te calculo cuanto tardarias en decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco, tampoco te pedi un testamento")
    

#calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'Dijiste  {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo')
print(f'Dijiste  {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo')

