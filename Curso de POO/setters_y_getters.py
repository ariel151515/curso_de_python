# Getters es un concepto que hace referencia
# a un valor privado 
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    #Setters establece un nuevo valor a la variable
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
        
    
# creamos el objeto dalto de la clase Persona
dalto = Persona("Lucas",21)

# de esta forma accedemos a la propiedad que 
# esta privada
#nombre = dalto.get_nombre()

nombre = dalto.get_nombre()        
print(nombre)
dalto.set_nombre("Pedro")
nombre = dalto.get_nombre()
print(nombre)


        