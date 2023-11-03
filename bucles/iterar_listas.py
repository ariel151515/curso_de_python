animales = ["perro","gato","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista de animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

print("--------------------------------------")

#recorriendo la lista numeros y multiplicando cada vallr por 10
for numero in numeros:
    resultado = numero * 10
    print(f'Ahora la variable numero es igual a: {resultado}')
    
print("--------------------------------------")

#recorremos dos listas al mismo tiempo con zip
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
print("--------------------------------------")

#ejecuta numeros del 5 al 10
#primer parametro es donde arranca y el segundo 
# deonde termina, y si solo ponemos un partametros arranca desde el 0 

for num in range(5,10):
    print(num)
    
#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su 
# indice el prier valor que devuelve es el indice y el segundo el valor
for num in enumerate(numeros):
    #print(num)
    print(num[0])
    

#forma correcta de recorrer una lista con su 
# indice el prier valor que devuelve es el indice y el segundo el valor
# mostramos el indice y el valor
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
    
#usando el else dentro del for
# si no hay elementos por recorrer muestra el else
for numero in numeros:
    print(f"ejecutando el ultimo bicle, valor actual: {numero}")
else:
    print("el bucle termino")