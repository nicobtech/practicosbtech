#Ejercicio 1
#Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.

import pandas as pd
from pandas.core.algorithms import value_counts
una_serie = pd.Series([1, 3, 5, 7, 9]) 
otra_serie = pd.Series([1, 4, 10, 14, 19])
print(una_serie + otra_serie)
print(una_serie - otra_serie)
print(una_serie * otra_serie) 
print(una_serie / otra_serie)  

#Ejercicio 2
#Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.

serie_tres = pd.Series([3, 7, 9, 14, 25])
serie_cuatro = pd.Series([1, 7, 10, 16, 19])
print(serie_tres==serie_cuatro)
print(serie_tres > serie_cuatro)
print(serie_tres < serie_cuatro)

#Ejercicio 3
#Escribí un programa para convertir un diccionario a una serie de Pandas.

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
df = pd.DataFrame([[key, dict1[key]] for key in dict1.keys()], columns=['Letra', 'Numero'])
print(df)

#Ejercicio 4
#Escribí un programa que dado un diccionario cuyos valores son listas de números, 
# cree otro diccionario con las mismas claves, pero donde los valores sean una lista de números donde 
# se potencia un número por el siguiente, tomándolos de a pares. Para ser más claros miremos este ejemplo 
# donde si un diccionario es:
import pandas as pd

dict1 = {"a": [1,3,5,2], "b": [4,2,3,5]}
dict2 = {}
for clave,valor in dict1.items():
    pares = []
    impares = []
    potencia = []
    for i in range(0,len(valor), 2):
        pares.append(valor[i])
    for i in range(1, len(valor), 2):
        impares.append(valor[i])
    for i in range(len(pares)):
        potencia.append(pares[i]** impares[i])
    dict2[clave] = potencia

print(dict2)

new_df = pd.DataFrame(dict2)
print(new_df)            

#Ejercicio 5
#Realizá un programa para crear y mostrar un DataFrame a partir de un diccionario y de unas etiquetas (o labels).

import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(datos_ejemplo, index=labels)
print(df)

#Ejercicio 6
#Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(datos_ejemplo, index=labels)
print(df.info())

#Ejercicio 7
#Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(datos_ejemplo, index=labels)
print(df[0:3])

#Ejercicio 8
#Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" del DataFrama anterior.

import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
lista = list(datos_ejemplo.items())

for clave,valor in lista[0:2]:
    print(clave,valor)

#Ejercicio 9
#Escribí un programa que dado el DataFrame anterior imprima los nombres en mayúscula y 
# la longitud de los mismos en una nueva tabla.

#CORREGIR
import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
lista = list(datos_ejemplo.items())
lista[0]

for clave,valor in lista[0]:
    valor = valor.upper()
    print(clave,valor)

