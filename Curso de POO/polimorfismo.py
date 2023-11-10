class Gato():
    def sonido(self):
        return 'Miau'
    
class Perro():
    def sonido(self):
        return 'Guau'
    

gato = Gato()
perro = Perro()

print(gato.sonido())

# Esto es polimorfismo de funcion (cambia el parametro de la
# funcion pero la funcion no cambia)
def hacer_sonido(animal):
    print(animal.sonido())
    
hacer_sonido(gato)

# polimorfismo de herencia

#Estudiar Duck Typing:
#Enlaces dinamicos
#Enlaces estaticos
#Tipo real
#Tipo declarado
