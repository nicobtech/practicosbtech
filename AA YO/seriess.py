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


# una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile']) #Crear una serie
# print(una_serie)
# print(una_serie[0]) #Se lo puede tratar como una lista


# paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
# print(paises_latam)

#Crear DatFrames -> Valores asociados a las columnas deben agregarse en el mismo nro que las columnas
clientes = pd.DataFrame(columns = ["nombre", "edad"], data ={"nombre": ["Juan", " ignacio"], "edad": [40, 50]}, index = [1,2])
print(clientes)


df = pd.DataFrame()
df[1] = [1, 4, 3, 4, 5]
df[2] = [4, 5, 6, 7, 8]
df[3] = [7, 8, 9, 0, 1]
print(df)


concateado = pd.concat([clientes,df])
print(concateado)

print(clientes.head())