from numpy.core.numeric import outer
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import seaborn as sns
import numpy as np
from sklearn import datasets 
from sklearn.cluster import KMeans, DBSCAN 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import AgglomerativeClustering
import scipy.stats as ss
import sklearn.linear_model as ln
from sklearn.model_selection import train_test_split

path = r"C:\Users\nicol\OneDrive\Escritorio\informatica\personas_2011.csv"
df = pd.read_csv(path, ";") 
# print(df)
# print(df.info())
# print(df.describe())

# print(df.isnull().sum())

for i in df.columns:
    print((df[i].isnull().sum())/ len(df[i])*100, "%")

#sns.heatmap(df.isnull(), cmap='viridis')
#plt.show()

def limpieza(df):   

    df.fillna(df['categoria_conicet_id'].mean(), inplace=True)
    df.fillna(df['categoria_incentivos'].mean(), inplace=True)
    df.fillna(df['max_dedicacion_horaria_docente_id'].mean(), inplace=True)
    df.fillna(df['institucion_cargo_docente_id'].mean(), inplace=True)
    df.fillna(df['clase_cargo_docente_id'].mean(), inplace=True)
    df.fillna(df['tipo_condicion_docente_id'].mean(), inplace=True)

print(limpieza(df))

# print(df.info())
# print(df.describe())

df.drop(["seniority_level"], axis =1, inplace = True)
for columna in df.columns: #Para usar esta función las columnas tienen que ser de int o float
    if df[columna].max() >= (df[columna].mean() + (df[columna].std() *3)) or df[columna].min() <= (df[columna].mean() - (df[columna].std() *3)):
        print("Esta columna puede tener outliers:  ", columna)

sns.boxplot(df["persona_id"]) #La función boxplot te permite reconocer los outliers por columna
#plt.show()
df= df[df["persona_id"]<= 73500]
plt.show()
sns.boxplot(df["institucion_cargo_docente_id"])
df= df[df["persona_id"]<= 2050]
plt.show()
