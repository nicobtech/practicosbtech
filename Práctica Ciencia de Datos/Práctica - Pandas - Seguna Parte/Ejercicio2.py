#Escribí un programa que guarde en una lista una columna de un DataFrame.
import pandas as pd
lista = []
diccionario = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} # y el valor es 4 en la columna 1.

df = pd.DataFrame(diccionario)
print(df)
lista2 = df[1].tolist()
print(lista2)

