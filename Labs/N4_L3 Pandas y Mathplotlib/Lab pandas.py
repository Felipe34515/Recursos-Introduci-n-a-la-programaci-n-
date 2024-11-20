# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:11:12 2023

@author: felip

"""
import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos(nombreArchivo: str)->pd.DataFrame:
    rta = pd.read_csv(nombreArchivo)
    return rta

def distribucion_banano(df):
    # Agrupamos por producto y sumamos las unidades
    grouped = df.groupby('Producto')['ValorMilesDolar'].sum()
    # quitamos en indice Cavendish Valery
    grouped = grouped[grouped.index != 'Cavendish Valery']
    # Ahora podemos hacer un gráfico de tarta con estos datos
    ax = grouped.plot(kind='pie', autopct='%1.1f%%', fontsize=5)
    ax.set_ylabel("ValorMilesDolar", fontsize=5)
    # Especificamos el título del gráfico
    plt.title("Unidades vendidas por producto")
    # Mostramos el gráfico
    plt.show()

def graficaBar(df):
    # Filtramos por año
    df = df[df['Anio'] >= 2016]
    # Agrupamos por producto y sumamos las unidades
    grouped = df.groupby('Producto')['ValorMilesDolar'].sum()
    # quitamos en indice Cavendish Valery
    grouped = grouped[grouped.index != 'Cavendish Valery']
    # Ahora podemos hacer un gráfico de barras con estos datos
    plt.figure()
    extracto = grouped.head(10)
    print(extracto)
    extracto.plot(kind = 'bar', figsize=(10,5))
    plt.show()
    
def generar_reporte(df, archivo_salida):
    # Agrupamos por 'Año' y 'Departamento', y sumamos la cantidad exportada
    grouped = df.groupby(['Anio', 'DepartamentoOrigen'])['Cantidad'].sum()
    
    # Abrimos un archivo para escribir el reporte
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("Reporte de exportaciones por año y departamento\n")
        f.write("=" * 50 + "\n")
        
        # Iteramos por año y departamentos
        for anio, datos_anuales in grouped.groupby(level=0):  # Agrupamos por el nivel 'Año'
            f.write(f"Año: {anio}\n")
            f.write("-" * 50 + "\n")
            for departamento, cantidad in datos_anuales.items():
                f.write(f"{departamento}: {cantidad:.2f}\n")
            f.write("\n")

def evolucion_banano(df):
    df = df[df['Anio']%2 == 0]
    grouped = df.groupby('Anio')['ValorMilesDolar'].sum()
    plt.figure()
    extracto = grouped.head(10)
    extracto.plot(kind = 'bar', figsize=(5,5), color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
    plt.show()

def mas_importan(df):
    # Agrupamos por 'PaisDestino' y sumamos las cantidades
    grouped = df.groupby('PaisDestino')['Cantidad'].sum()
    # Ordenamos los países de mayor a menor
    grouped = grouped.sort_values(ascending=False)
    # Tomamos los 5 países con mayor cantidad
    extracto = grouped.head(5)
    # Graficamos con barras horizontales
    extracto.plot(kind='barh', figsize=(5, 5),fontsize=8,  color=['blue', 'orange', 'green', 'red', 'purple'])
    # Añadimos título y etiquetas para mayor claridad
    plt.title('Los 5 países que más importan banano son: ')
    plt.xlabel('kilos importantes')
    plt.ylabel('País')
    plt.show()



df = cargar_datos("exportaciones.csv")

# distribucion_banano(df)
# graficaBar(df)
generar_reporte(df, "reporte.txt")
# evolucion_banano(df)
# mas_importan(df)






