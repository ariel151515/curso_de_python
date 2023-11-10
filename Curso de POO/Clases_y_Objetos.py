class Celular():
    # este es el metodo constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")
       
# Instanciar un bjeto, 
# un objeto es una instancia de una clase
celular1 = Celular("Samsung","s23","48MP")     
celular2 = Celular("iphone","15","48MP") 

celular1.llamar()