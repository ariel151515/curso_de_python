# 2 lista, una con nombres otra con apellidos
nombres = ["lucas","matias","camila","pedro","roberto"]
apellidos = ["dalto","zing","dalto","robetix","tarado"]

#mostrar esta informacion en un txt de forma optima
with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\Apellido: {a}\n--------------\n") for n,a in zip(nombres, apellidos)]
