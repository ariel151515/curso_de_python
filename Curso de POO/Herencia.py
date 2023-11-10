class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")


"""# la clas empleado hereda todo de la clase persona
class Empleado(Persona):
    pass"""


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print("Mi habilidad es: {self.habilidad}")
        

# la clas empleado hereda todo de la clase persona
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
     

# la clas empleado hereda todo de la clase persona
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,nota,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.nota = nota
        self.universidad = universidad
        

# Esto es herencia multipla porque hereda dos clases
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona().__init__(self,nombre,edad,nacionalidad)
        Artista().__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def mostrar_habilidad(self):
        print("No tengo")
    
    def presentarse(self):
        print(f'Hola,soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

       
# Se creo una instancia para la clas empleado
roberto = Empleado("Roberto",43,"argentino", "programador","100000")

# Tru si hereda de la clase artista
herencia = issubclass(EmpleadoArtista, Artista)

roberto.hablar()
print(herencia)