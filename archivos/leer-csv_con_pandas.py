import pandas as pd

#usando la funcion read_csv parta leer el archivo CSV
df = pd.read_csv("archivo\\datos.csv")
df2 = pd.read_csv("archivo\\datos.csv")

#obteniendo los datos de la columna nombre
nombre = df["nombre"]

cadena = "0123456776"

#accedemeos desde el 0 hasta el 3
#print(cadena[:3])

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando de forma descendente (de mayor a menor)
df_orden_descendente = df.sort_values("edad", ascending=False)

# concatenando los 2 daraframes
df_concatenado = pd.concat([df,df2])

#accediendo a las fila indicadas con head()
primer_fila = df.head(2)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape

#accediendo a la cantidad de filas y columnas desempaquetando
filas_totales, columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a un elemento especifico del df con iloc (por indice)
elemento_especifico_loc = df.iloc[2, "edad"]

#accediendo a todas los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas los apellidos con iloc
apellidos_iloc = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con loc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30) 