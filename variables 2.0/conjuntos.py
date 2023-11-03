#creando un conjunto con set, NOTA: los datos de set o son modificables
conjunto = set(["Dato 1", "Dato 2"])

#metiendo un conjunto dentro de otro conjunto
#frozenset es para meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}

#teorias de conjuntos

conjunto1 = {1,2,3,5,7}
conjunto2 = {1,3,7}

#verificando si conjunto2 en un subconjunto de conjunto1 ? devuelve true o false
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto 
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun
resultado =  conjunto2.isdisjoint(conjunto1)



print(resultado)