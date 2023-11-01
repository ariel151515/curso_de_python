edad = 9

if edad >= 18:
    print("Podes pasar")
else:
    print("No podes pasar")


contraseña_almacenada = "relectura"
contraseña_escrita = '''123'''

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESION...")
else:
    print("CONTRASENA INVALIDA, INTENTE DE NUEVO...")


ingreso_mensual = 1100

if ingreso_mensual > 9000:
    print("Estas bien en cualquier parte del mundo")

elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")

else:
    print("sos pobre")


salario = 900
gastos = 700

if salario > 1000:
    if gastos < 600:
        print("Estas bien economicamente")
    else:
        print("Estas jodido")
elif salario < 1000:
    print("Cagaste, sos pobre")
