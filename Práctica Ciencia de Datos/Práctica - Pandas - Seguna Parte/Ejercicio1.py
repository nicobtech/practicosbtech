# Escribí un programa que dado un diccionario cuyos valores sean listas de números cree un DataFrame y 
# luego seleccione e imprima las filas del DataFrame basado en un valor de una columna.#

import pandas as pd

diccionario = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} # y el valor es 4 en la columna 1.
df = pd.DataFrame(diccionario)

print(df)
print(df.loc[df[1] == 4])


