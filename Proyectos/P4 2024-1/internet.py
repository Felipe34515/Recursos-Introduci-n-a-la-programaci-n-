# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Modulo de funciones.

@author: Cupi2
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
import math

# Parte 1
# Requerimiento 0
def cargar_datos(ruta: str) -> pd.DataFrame:
    return pd.read_csv(ruta)

# Parte 2
# Requerimiento 1
def piechart_anio (dataframe:pd.DataFrame, anio:str) -> pd.DataFrame:
    """
    se nos pide que creemos una grafica tipo pie que 
    muestre el porcentage de accesos fijos en una año especificado
    

    Parameters
    ----------
    anio : str
        DESCRIPTION.
        el año que se ingresa
    dataframe : pd.DataFrame
        DESCRIPTION.

    Returns
    -------
    excel : TYPE
        DESCRIPTION.

    """
    rta = dataframe[dataframe["AÑO"]== anio]
    rta = rta.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum()
    rta = rta.sort_values(ascending = False).head(20)
    rta.plot(kind="pie", autopct = "%1.1f%%", textprops = {"fontsize":6.5}, title = "Top 20 departamentos con Accesos Fijos a internet en el " + str(anio))
    plt.ylabel("")
    plt.show()
    
def piechart_anioV2(df: pd.DataFrame, año: int):
    df_año = df[df["AÑO"] == año]
    top_20 = df_año.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum().nlargest(20)
    plt.figure(figsize=(10, 8))
    top_20.plot.pie(autopct='%1.1f%%')
    plt.title(f"Top 20 departamentos con mayor número de accesos fijos a internet en {año}")
    plt.ylabel("")
    plt.show()

# Requerimiento 2
def bar_chart_top_20_ratio ( dataframe:pd.DataFrame, departamento: str) -> pd.DataFrame:
    """
    se nos pide que creemos una grafica de diagrama de barras donde grafiquemos 
    el "ratio" que es igual al numero de accesos fijo dividido sobre la poblacion dane,
    se nos pide que grafiquemos el ratio por los municipios de un departamento especificado

    Parameters
    ----------
    departamento : str
        DESCRIPTION.
    dataframe : pd.DataFrame
        DESCRIPTION.

    Returns
    -------
    excel : TYPE
        DESCRIPTION.

    """
    rta = dataframe[dataframe["DEPARTAMENTO"]== departamento]
    rta = rta.groupby("MUNICIPIO")[["No. ACCESOS FIJOS", "POBLACIÓN DANE"]].sum()
    rta["ratio"] = rta["No. ACCESOS FIJOS"]/ rta["POBLACIÓN DANE"]
    rta = rta.groupby("MUNICIPIO")["ratio"].sum()
    rta = rta.sort_values( ascending = False).head(20)
    rta.plot(kind = "bar", title = "Top 20 municipios con mayor relacion de Accesos Fijos a Internet por Poblacion en " + str(departamento))
    plt.ylabel("Relacion Accesos Fijos a Internet por Poblacion") 
    plt.show()
    
def bar_chart_top_20_ratioV2(df: pd.DataFrame, departamento: str):
    df_depto = df[df["DEPARTAMENTO"] == departamento]
    df_depto["Ratio"] = df_depto["No. ACCESOS FIJOS"] / df_depto["POBLACIÓN DANE"]
    top_20 = df_depto.groupby("MUNICIPIO")["Ratio"].sum().nlargest(20)
    
    plt.figure(figsize=(13, 7))
    top_20.plot.bar()
    plt.title(f"Top 20 Municipios con mayor relacion de Accesos Fijos por Poblacion en {departamento}")
    plt.xlabel("Municipios")
    plt.ylabel("Relacion Accesos Fijos a Internet por Poblacion")
    plt.show()

# Requerimiento 3
def boxplot_provincias (dataframe:pd.DataFrame, departamento: str) -> pd.DataFrame:
    """
    aqui se nos pide que hagamos un diagrama de cajas y bigotes de los accesos fijos de por provincias  
    de un departamento especificado

    Parameters
    ----------
    departamento : str
        DESCRIPTION.
    dataframe : pd.DataFrame
        DESCRIPTION.

    Returns
    -------
    None.

    """
    rta = dataframe[dataframe["DEPARTAMENTO"]== departamento]
    provincias = sorted(rta["PROVINCIA"].unique())
    columnas = 2
    numero_de_provincias = len(provincias)
    filas = ((numero_de_provincias+1)//2)
    imagen, coordenadas = plt.subplots(filas, columnas, figsize = (13,7),constrained_layout = True)
    coordenadas = coordenadas.flatten()
    for elemento in zip(coordenadas, provincias):
    #aqui lo que hago es guardar en tuplas las provincias en su respectivo puesto 
    #usando una lista vacia [puesto en la lista, provincia] 
        grafica_provincias = rta[rta["PROVINCIA"] == elemento[1]]["No. ACCESOS FIJOS"]
        #aqui lo que hago es filtrar para que nos den el numero de accesos fijos por provincia
        bigotes = elemento[0].boxplot(grafica_provincias,vert = False)
        elemento[0].set_title(elemento[1])
        elemento[0].set_ylabel("No. ACCESOS FIJOS")
    if numero_de_provincias % 2 != 0:
        
        for i in range (numero_de_provincias, len(coordenadas)):
            imagen.delaxes(coordenadas[i])
    plt.show()
    
def boxplot_provinciasV2(df: pd.DataFrame, departamento: str, fontsize: str = 'small'):
    df_depto = df[df["DEPARTAMENTO"] == departamento]
    provincias = df_depto["PROVINCIA"].unique()
    
    n_provincias = len(provincias)
    n_cols = 2
    n_rows = math.ceil(n_provincias / n_cols)
    
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(14, 8), sharey=False)
    axes = axes.flatten()  # Para facilitar el acceso a los ejes
    
    for ax, provincia in zip(axes, provincias):
        df_provincia = df_depto[df_depto["PROVINCIA"] == provincia]
        df_provincia.boxplot(column="No. ACCESOS FIJOS", ax=ax, grid=False, vert=False)
        ax.set_title(provincia, fontsize=fontsize)
        ax.set_xlabel("", fontsize=fontsize)
        ax.set_ylabel("", fontsize=fontsize)
    
    # Eliminar subplots vacíos si los hay
    for i in range(len(provincias), len(axes)):
        fig.delaxes(axes[i])
    
    plt.suptitle(f"Distribución de accesos fijos por provincias en {departamento}", fontsize=fontsize)
    plt.subplots_adjust(hspace=0.4, left=0.2, right=0.8, top=0.9, bottom=0.1)
    plt.show()

# Parte 3
# Requerimiento 4
def crear_matriz(dataframe: pd.DataFrame):
    deptos = sorted(dataframe["DEPARTAMENTO"].unique())
    dept_dict = dict(list(enumerate(deptos)))

    anios = sorted(dataframe["AÑO"].unique())
    anios_dict = dict(list(enumerate(anios)))
    
    matriz = dataframe.pivot_table(index='DEPARTAMENTO', columns='AÑO', values='No. ACCESOS FIJOS', aggfunc='sum', fill_value=0)
    return matriz, anios_dict, dept_dict

# Requerimiento 5
def accesos_por_año(matriz, dict_columnas, año):
    if año in dict_columnas.values():
        col_idx = list(dict_columnas.keys())[list(dict_columnas.values()).index(año)]
        return matriz.iloc[:, col_idx].sum()
    return 0

# Requerimiento 6
def crecimiento_porcentual(matriz, dict_columnas, año, porcentaje):
    if año not in dict_columnas.values() or año == max(dict_columnas.values()):
        return "Ninguno", -101
    col_idx = list(dict_columnas.keys())[list(dict_columnas.values()).index(año)]
    next_col_idx = col_idx + 1
    crecimiento = ((matriz.iloc[:, next_col_idx] - matriz.iloc[:, col_idx]) / matriz.iloc[:, col_idx]) * 100
    crecimiento = crecimiento[crecimiento > porcentaje]
    if crecimiento.empty:
        return "Ninguno", -101
    departamento = crecimiento.idxmax()
    return departamento, round(crecimiento[departamento], 2)

# Requerimiento 7 BONO
def cargar_coordenadas(nombre_archivo:str) -> dict:
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    titulos = archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]), int(datos[2]))
        linea = archivo.readline()
    return deptos

def mapa_accesos(df: pd.DataFrame, coordenadas: dict, año: int):
    df_año = df[df["AÑO"] == año]
    accesos = df_año.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum()

    colores = {
        "0 a <5000": [0.94, 0.10, 0.10],  
        "5000 a <10000": [0.94, 0.10, 0.85],  
        "10000 a <20000": [0.10, 0.50, 0.94], 
        "20000 a <50000": [0.34, 0.94, 0.10], 
        ">50000": [0.99, 0.82, 0.09]
    }

    mapa = mpimg.imread("mapa.png").tolist()
    plt.imshow(mapa)
    
    for depto, total in accesos.items():
        x, y = coordenadas[depto]
        color = None
        if total < 5000:
            color = colores["0 a <5000"]
        elif total < 10000:
            color = colores["5000 a <10000"]
        elif total < 20000:
            color = colores["10000 a <20000"]
        elif total < 50000:
            color = colores["20000 a <50000"]
        else:
            color = colores[">50000"]
        plt.gca().add_patch(plt.Rectangle((x-6, y-6), 13, 13, color=color))

    legends = []
    for i in colores:
        legends.append(mpatches.Patch(color = colores[i], label=i))
    plt.legend(handles = legends, loc = 3, fontsize='x-small')
    plt.title("Accesos fijos a internet por departamento en el año" + str(año), fontsize='x-small')
    plt.show()