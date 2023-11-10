# class Persona:
#     def __init__(self,nombre,edad):
#         self._nombre = nombre
#         self._edad = edad
    
#     # con esto le indicamos que es un setter (no vas a ser una funcion
#     # sino que vs a ser una propiedad)
#     @property
#     def get_nombre(self):
#         return self._nombre

        
# dalto = Persona("Lucas",21)

# # podemos llamar a get_nombre como si fiera una propiedad y no
# # una funciona gracias al @property
# nombre = dalto.get_nombre

# print(nombre)


class Persona:
    def __init__(self,nombre,edad):
         self.__nombre = nombre
         self._edad = edad
    
    # para poder modificar la propiedad
    @property
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    # para poder modificar la propiedad
    @property.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
        
    # para poder modificar la propiedad
    @property.deleter
    def nombre(self):
        del self.__nombre

        

dalto = Persona("Lucas",21)
nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

#para eliminar
del dalto.nombre()

