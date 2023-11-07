# Esta forma es mas rapida y mas eficiente 
# Abriendo el archivo con with open
with open("archivo\\texto_de_dalto.txt", encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
# No es necesario cerrarlo al usar with open