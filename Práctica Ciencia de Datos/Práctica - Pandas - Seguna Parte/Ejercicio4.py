import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
def eliminar(df, fila):
    df2 = df.iloc[fila:]
    return df2
print(df)
print(eliminar(df,3)) #elimina las primeras 3 filas