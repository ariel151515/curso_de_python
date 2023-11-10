class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} fuerza: {self.fuerza}, velocidad: {self.velocidad}"
    
    
    def __add__(self,otro_pi):
        nuevo_nombre = self.nombre + "-" + otro_pi.nombre
        nuevo_fuerza = ((self.fuerza)/2)**2
    
goku = Personaje("Goku",100,100)
print(goku)
        