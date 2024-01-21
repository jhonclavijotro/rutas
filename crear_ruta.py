import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import uniform, randint
import ecuaciones


def poste():
    """Devuelve un poste con sus características"""
    lat = uniform(2.003724, 2.0226823)
    lon = uniform(-77.017380, -77.014211)
    alt = uniform(900, 1100)
    nodo = randint(105000, 106000)
    return [nodo, lat, lon, alt, 1800, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]


def ruta_postes(cant=1):
    """Genera lista de postes con características
    en valor np.nan, para pruebas"""
    lista_postes = []
    for _ in range(cant):
        lista_postes.append(poste())
    lista_postes = pd.DataFrame(data=lista_postes, columns=[
                                'Nodo', 'Latitud', 'Longitud', 'Altitud', 'Ruptura', 'vp1', 'vp2', 'vv1', 'vv2', 'fx', 'fy', 'fz'])
    return lista_postes


def invocar_tabla(tabla="", db=''):
  """tabla será alguna de las tablas ya creadas en la
  base de datos db, retornando un dataframe de dicha consulta"""
  conn = sqlite3.connect(database=db)
  consulta = "SELECT * FROM "+tabla
  cable = pd.read_sql_query(sql=consulta, con=conn)
  return cable


# bases de datos con tipos de cables y los tramos de linea
cables = invocar_tabla(
    tabla='cable', db='E:/Python/Datos/071023_sql/ruta_marias.db')
lineas = invocar_tabla(
    tabla='linea', db='E:/Python/Datos/071023_sql/ruta_marias.db')
postes = ruta_postes(cant=10)

# print(cables.head(3))
# print(postes.head(3))

cond = cables[cables['codigo']=='penguin']
carga_uni = ecuaciones.carga_unitaria(conductor=cond, alt=6, v=2)
print(carga_uni)

