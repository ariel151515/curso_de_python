#creando una funcion que nos devuelva los numeros primos 
#entre 0 y el argumento que pasamos


def es_primo(num):
    for i in range(2, num -1 ):
        if num % i == 0:  return False
    return True
        

def primos_hasta(num):
    primos = []
    #iteramos num pero arrancamos desde 2, + 1 significa una posicion mas
    for i in range(3,num + 1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)

