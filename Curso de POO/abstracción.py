class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self.__estado = "encendido"
        print("El autoesta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
           self.encender()
        print("Conduciendo el auto")
        
# Esta abstra hace referencia a crear clases abstractas 
mi_auto = Auto()
mi_auto.conducir()