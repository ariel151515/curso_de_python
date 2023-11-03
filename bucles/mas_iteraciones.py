#El bucle for in recorre listas o duplas

frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]

#saltea la 'granada' con continue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'Me voy a comer una {fruta}')
    

print("--------------------------------------------")
    
    
#termina en 'pera'
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
    
print('bucle terminado')


print("--------------------------------------------")

cadena = 'HOLA'

#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
print("--------------------------------------------")


numeros_mios = [2,5,8,10]
numeros_duplicados = list()

#for en una sola linea de codigo
for num in numeros_mios:
    numeros_duplicados.append(num * 2)
    
print(numeros_duplicados)
    
    
print("--------------------------------------------")

numdu = [2,3,4,5]

#se puede hacer un fomr en una sola linea de codigo 
numeros_duplicados = [x*2 for x in numdu]
print(numeros_duplicados)
    