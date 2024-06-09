# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Interfaz basada en consola para la interaccion con el usuario.

@author: Cupi2
"""

import internet as mod
import pandas as pd

def ejecutar_cargar_datos() -> pd.DataFrame:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos del acceso a internet en Colombia.
    Retorno: dataframe
        El dataframe con los datos cargados del archivo CSV.
    """
    datos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la informacion del acceso a internet en Colombia: ")
    datos = mod.cargar_datos(archivo)
    if len(datos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la informacion.")
    else:
        print("Se cargaron los siguientes datos a partir del archivo csv: ")
        print(datos)
    return datos

def crear_matriz(dataframe: pd.DataFrame) -> tuple:
    """Crea una matriz con la cantidad de accesos fijos a internet por departamento y anio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    Retorno: tuple
        La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    matriz = mod.crear_matriz(dataframe)
    print("Se ha creado la matriz con la cantidad de accesos fijos a internet por departamento y anio.")
    print(matriz)
    return matriz

def ejecutar_piechart_anio(datos: pd.DataFrame):
    """Solicita al usuario que ingrese un anio y muestra un piechart con la distribucion de accesos fijos a internet por departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    año = int(input("Ingrese el año para el cual desea ver la distribución de accesos fijos a internet: "))
    mod.piechart_anio(datos, año)

def ejecutar_diagrama_barras(datos: pd.DataFrame):
    """Muestra un diagrama de barras con la relacion entre el numero de accesos fijos a internet y la poblacion por municipio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    departamento = input("Ingrese el nombre del departamento para el cual desea ver la relación de accesos fijos a internet: ")
    mod.bar_chart_top_20_ratio(datos, departamento)

def ejecutar_diagrama_cajas(datos: pd.DataFrame):
    """Muestra un diagrama de cajas con la distribucion de accesos fijos a internet por provincia en un departamento especifico.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    departamento = input("Ingrese el nombre del departamento para el cual desea ver la distribución de accesos fijos por provincias: ")
    mod.boxplot_provincias(datos, departamento)

def ejecutar_cantidad_accesos_anio(matriz: pd.DataFrame):
    """Solicita al usuario que ingrese un anio y muestra la cantidad de accesos fijos a internet en ese anio.
    Parametros:
        matriz (pd.DataFrame): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    año = int(input("Ingrese el año para el cual desea consultar la cantidad de accesos fijos a internet: "))
    total_accesos = mod.accesos_por_año(matriz[0], matriz[1], año)
    print(f"La cantidad de accesos fijos a internet en el año {año} es de {total_accesos}")

def ejecutar_departamento_en_ascenso(matriz: pd.DataFrame):
    """Solicita al usuario que ingrese un anio y un porcentaje para consultar el departamento con mayor crecimiento de accesos fijos a internet.
    Parametros:
        matriz (pd.DataFrame): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    año = int(input("Ingrese el año para el cual desea consultar el crecimiento de accesos fijos a internet: "))
    porcentaje = float(input("Ingrese el porcentaje de crecimiento que desea consultar: "))
    departamento, crecimiento = mod.crecimiento_porcentual(matriz[0], matriz[1], año, porcentaje)
    if departamento == "Ninguno":
        print("No se encontró ningún departamento que supere el porcentaje especificado.")
    else:
        print(f"{departamento} tuvo un crecimiento del {crecimiento}% del año {año} al año {año+1}")

def ejecutar_departamentos_mapa(datos: pd.DataFrame):
    """Solicita al usuario que ingrese un anio y muestra un mapa con la cantidad de accesos fijos a internet por departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    coordenadas = mod.cargar_coordenadas("coordenadas.txt")
    año = int(input("Ingrese el año para el cual desea ver la distribución de accesos fijos a internet en el mapa: "))
    mod.mapa_accesos(datos, coordenadas, año)

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nMenu de opciones:")
    print("1. Cargar datos sobre el acceso a internet en Colombia.") 
    print("2. Mostrar Top 20 departamentos con mayor numero de accesos fijos a internet en un anio.") 
    print("3. Mostrar Top 20 municipios con mayor numero de accesos fijos por población en un departamento.")
    print("4. Mostrar diagrama de cajas con la distribucion de accesos fijos a internet por provincia en un departamento.")
    print("5. Construir matriz de Departamentos vs Año.")
    print("6. Consultar la cantidad de accesos fijos a internet en un anio.")
    print("7. Consultar si existe un departamento en ascenso en un anio dado.")
    print("8. Generar mapa de la cantidad de accesos fijos a internet por departamento en un anio.")
    print("9. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = None
    matriz = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_piechart_anio(datos)
        elif opcion_seleccionada == 3:
            ejecutar_diagrama_barras(datos)
        elif opcion_seleccionada == 4:
            ejecutar_diagrama_cajas(datos)
        elif opcion_seleccionada == 5:
            matriz = crear_matriz(datos)
        elif opcion_seleccionada == 6:
            ejecutar_cantidad_accesos_anio(matriz)
        elif opcion_seleccionada == 7:
            ejecutar_departamento_en_ascenso(matriz)
        elif opcion_seleccionada == 8:
            ejecutar_departamentos_mapa(datos)
        elif opcion_seleccionada == 9:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    iniciar_aplicacion()

