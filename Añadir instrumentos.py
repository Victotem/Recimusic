#Añadir:
'''
import pandas


usuario = "victor"

df = pandas.DataFrame({"Usuario":["iiiiiii"],
                    "Contraseña":["oooooooo"]
                       })


df.to_csv("Usuarios.csv",mode="a", header=False)
'''
#Crear:

import pandas as pd

# Crear una lista de diccionarios que contienen los datos
data = [
    {"Instrumentos": "Tubófono", "Color/es": "Azul y Rojo", "Stock": 10, "Disponible": "Si"},
    {"Instrumentos": "Palarra", "Color/es": "Negro", "Stock": 0, "Disponible": "No"},
    {"Instrumentos": "Raquetarra", "Color/es": "Amarillo y Verde", "Stock": 2, "Disponible": "Si"},
   
]

# Crear un DataFrame a partir de la lista de diccionarios
tabla = pd.DataFrame(data)

#Crear la tabla
tabla.to_csv("instrumentos.csv", index=False)
# Mostrar la tabla
print(tabla)