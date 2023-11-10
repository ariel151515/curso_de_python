class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nombre: {self.edad}')
        
        
# Hereda de Persona
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        # super para heredar de Persona nombre y edad (si usamos
        # la funcion super() self no s epasa como parametro)
        super().__init__(nombre,edad)
        self.grado = grado
    
    def mostrar_grado(self):
        print(f'Mostrar: {self.grado}')


# creamos el onjeto
estudiante =  Estudiante('Juan','24','10mo')

estudiante.mostrar_datos()
estudiante.mostrar_grado()