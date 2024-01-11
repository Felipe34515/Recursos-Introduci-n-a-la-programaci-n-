# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:11:12 2023

@author: felip

"""
import pandas as pd
import matplotlib.pyplot as plt

def gafricaPie():
    df = pd.read_csv("exportaciones.csv")
    # Agrupamos por producto y sumamos las unidades
    grouped = df.groupby('Producto')['ValorMilesDolar'].count()
    # Ahora podemos hacer un gráfico de tarta con estos datos
    grouped.plot(kind='pie', autopct='%1.1f%%')
    # Especificamos el título del gráfico
    plt.title("Unidades vendidas por producto")
    # Mostramos el gráfico
    plt.show()


def gafricaPie2():
    df = pd.read_csv("exportaciones.csv")
    # agrupado = df.groupby('Producto')
    agrupado = df.groupby('Producto').ValorMilesDolar.sum()
    # agrupado = agrupado[agrupado["Cavendish  Valery"] == 1]
    
    agrupado = agrupado[agrupado.index != 'Cavendish  Valery']
    agrupado.plot(kind='pie', autopct='%1.1f%%')
    
    plt.title("Unidades vendidas por producto")
    plt.show()
    
    

gafricaPie2()
df = pd.read_csv("exportaciones.csv")
# agrupado = df.groupby('Producto')
agrupado = df.groupby('Producto').ValorMilesDolar.sum()




