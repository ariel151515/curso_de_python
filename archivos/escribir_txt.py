# Esto sobrescribe el archivo
# con permiso 'w' lee y 'a' agrega texto
with open("archivo\\texto_de_dalto.txt", 'w', encoding="UTF-8") as archivo:
    # Esto sobrescribe el archivo
    
    # Agregando 2 lineas con writelines
    archivo.writelines([" - Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto \n"])
    
    # Agregando otras 2 lineas
    archivo.writelines([" - Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto \n"])
    
    # Agregando otras 2 lineas
    archivo.writelines([" - Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto \n"])