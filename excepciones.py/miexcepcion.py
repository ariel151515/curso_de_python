# Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")
        
# Lanzando mi propia excepcion
raise MiExcepcion("jajajaj, perosna poco culta")

# Manejandola
try:
    raise MiExcepcion("jajajaj, perosna poco culta")
except:
    print("Como vas a cometer ese error?")