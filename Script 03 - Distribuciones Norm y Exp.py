import pandas as pd
import numpy as np

#Se entrega una lista con las categorías y un número de datos necesarios y retorna una lista con los datos en una distribución exponencial
def dist_exp(categorias, n):
    scale = 1
    exp_values = np.random.exponential(scale, len(categorias))
    exp_values_normalized = exp_values / np.sum(exp_values)
    probabilities = np.sort(exp_values_normalized)[::-1]
    print("Probabilidades normalizadas:", probabilities)
    data = np.random.choice(categorias, size=n, p=probabilities)
    data_list = list(data)
    df = pd.DataFrame(data, columns=['Category'])
    print(df.head())
    print(df["Category"].value_counts())
    return(data_list)

dist_exp(["A", "B", "C"], 1000)


#Se entrega una lista con las categorías y un número de datos necesarios y retorna una lista con los datos en una distribución normal
def dist_unif(categorias, n):
    probabilidades = list()

    for i in range(0,len(categorias)):
        probabilidades.append(1/(len(categorias)))

    data = np.random.choice(categorias, size=n, p=probabilidades)
    df = pd.DataFrame(data, columns=['Category'])
    print(df.head())
    print(df['Category'].value_counts())

dist_unif(["A", "B", "C"], 1000)