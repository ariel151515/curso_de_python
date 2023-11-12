# Todos se sirven de Notificador
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificador(self):
        raise NotImplementedError


class NotficadorEmail(Notificador):
    def notificador(self):
        print(f"Enviando mensaje a {self.usuario.email}")
        
class NotficadorSMS(Notificador):
    def notificador(self):
        print(f"Enviando mensaje SMS a {self.usuario.sms}")
        

class NotficadorWhatsapp(Notificador):
    def notificador(self):
        print(f"Enviando mensaje whatsapp a {self.usuario.whatsapp}")
        

        