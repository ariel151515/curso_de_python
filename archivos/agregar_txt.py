with open("archivo\\texto_de_dalto.txt", encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")
    