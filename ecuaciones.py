import numpy as np
import pandas as pd
from math import sqrt, pow

def pres_viento(alt=0, v=0):
    """Calculo de la presión generada por el viento
    en el conductor"""
    Q = 0.603-0.0514*(alt/1000)
    pv = Q*(v**2)
    return pv

def carga_unitaria(conductor, alt, v):
    """conduc debe ser un dataframe y con un parámetro
    llamado diam"""
    PV = pres_viento(alt, v)
    diam = conductor['diam']
    cv = (PV/10)*(diam/1000)
    c_cond = conductor['ruptura']/1000
    cu = sqrt(pow(cv, 2)+pow(c_cond, 2))
    return cu

def catenaria(conductor, fac_seg):
    pass
