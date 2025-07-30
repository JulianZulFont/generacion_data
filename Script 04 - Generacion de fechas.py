import pandas as pd
import numpy as np

import random
from datetime import datetime, timedelta

def random_date(start, end, n):
    lista = list()
    delta = end - start
    for i in range(0,n):
        random_second = random.randrange(delta.total_seconds())
        rand_date = (start + timedelta(seconds=random_second)).strftime("%Y - %m - %d %H:%M:%S")
        lista.append(rand_date)
    lista = pd.Series(lista)
    lista = pd.to_datetime(lista)
    return lista

def random_numb_uniform(start_n, end_n, n):
    random_numbers = np.random.uniform(start_n, end_n, n)
    random_serie = pd.Series(random_numbers)
    #print(random_serie)
    random_serie = pd.to_timedelta(random_serie, unit="h")
    return random_serie

#Generación de fecha con hora inicial para la falla
fechas_iniciales = random_date(datetime(2023,1,1), datetime(2024,1,1), 10000)



#Se genera un número aleatorio entre 0.25 y 4 para generar espacios de horas que pueden durar la falla
horas_random = random_numb_uniform(0.25, 4, 10000)

#En base a la fecha anterior inicial y la hora se genera la fecha y hora final a la cual terminó la falla
fechas_finales = fechas_iniciales.add(horas_random)




fechas_iniciales = pd.DataFrame(fechas_iniciales)
fechas_iniciales.columns = ["Fecha inicial"]


fechas_finales = pd.DataFrame(fechas_finales)
fechas_finales.columns = ["Fecha final"]

#fechas_iniciales.to_excel("Archivo fechas iniciales.xlsx", index=False)
#fechas_finales.to_excel("Archivo fechas finales.xlsx", index=False)

#print(random_date(start_time, end_time, 10))
#print(random_numb_uniform(0.25, 5, 5))

#print(datetime(2024,1,1) + timedelta(hours=0.25))