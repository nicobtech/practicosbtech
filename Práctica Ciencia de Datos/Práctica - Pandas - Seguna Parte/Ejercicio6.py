import pandas as pd
uno = {1: ["a", "b", "c"], 2: ["d","e","f"]}
dos = {"a": [1, 2, 3], "b": [4,5,6], "c": [7,8,9]}
df1 = pd.DataFrame(uno)
df2 = pd.DataFrame(dos)

columnas = pd.concat([df1,df2])
filas = pd.concat([df1,df2], axis=1)