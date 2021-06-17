import pandas as pd
df1 = pd.DataFrame({1: ["a", "b", "c"], 2: ["d","e","f"]})
df2 = pd.DataFrame({0: [1, 2, 3], 1:[4,5,6], 2:[7,8,9]})
result = pd.concat([df1,df2], join="inner", ignore_index=True)