# class Dicionario:
#     def verificar_palabra(self,palabra):
#         #logica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Dicionario()
        
#     def correguir_texto(self, texto):
#         #usamos el dccionario para corregir texto
#         pass

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        #logica para verificar palabras
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta 
        # en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def correguir_texto(self, texto):
        #usamos el verificador para correguir textos
        