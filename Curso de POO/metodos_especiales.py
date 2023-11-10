class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # str tiene una funcion
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'  
      
    # 
    def __repr__(self):
        return f'Persona({self.nombre}, {self.edad})'
    
    # 
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)


dalto = Persona("Lucas", 21)
# print(dalto)
# lista = (1,2,3)

# print(lista)

repre = repr(dalto)
resultado = eval(repre)

print(resultado.nombre)


dalto = Persona("Lucas",21)
pedro = Persona("Pedro",30)

nueva_persona = dalto + pedro
print(nueva_persona.edad)

escalera al Cielo 
boy over flowers