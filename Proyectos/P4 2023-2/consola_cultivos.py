"""
Ejercicio nivel 4: Rendimiento de cultivos en colombia por año
Interfaz basada en consola para la interaccion con el usuario.

@author: Cupi2
"""

import cultivos as mod
import pandas as pd

def ejecutar_cargar_datos() -> pd.DataFrame:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos del rendimiento de cultivos en Colombia.
    Retorno: dataframe
        El diccionario de departamentos con la informacion de los departamentos en el archivo
    """
    datos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la informacion del rendimiento de cultivos en Colombia: ")
    datos = mod.cargar_datos(archivo)
    if len(datos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la informacion.")
    else:
        print("Se cargaron los siguientes datos a partir del archivo csv: ")
        print(datos)
    return datos

def ejecutar_crear_matriz(dataframe: pd.DataFrame) -> tuple:
    """Ejecuta la opcion que construye la matriz de Departamento vs Tipo_Cultivo.
    """
    matriz = mod.crear_matriz(dataframe)
    print("La matriz armada de Departamento vs. Tipo_Cultivo es: ")
    print(matriz)
    return matriz

def ejecutar_piechart_tipo_cultivo(dataframe: pd.DataFrame)->None:
    """Ejecuta la opcion de hacer una gráfica de pie sobre la distribución de los tipos de cultivos
    en un departamento.
    """
    departamento = input("Digite el departamento: ")
    mod.requ1(departamento, dataframe)
    
    
def ejecutar_diagrama_barras(dataframe: pd.DataFrame) -> None:
    """Ejecuta la opcion de hacer una grafica de barras del top 10 de cultivos
    que tuvieron mayor producción de toneladas por hectarea.
    """
    mod.requ2(dataframe)
    

def ejecutar_toneladas_tipo_cultivo(dataframe: pd.DataFrame) -> None:
    """Ejecuta la opcion que hace un diagrama de caja y bigotes de la distribución 
    de las toneladas producidas en los tipos de cultivos en un rango proporcionado por el usuario. 
    """
    
    minimo = int(input("Digite digito maximo: "))
    maximo = int(input("Digite digito minimo: "))
    mod.requ3(dataframe, minimo, maximo)

def ejecutar_depto_mayor_o_menor_productor(matriz:tuple) -> None:
    """Ejecuta la opcion que encuentra el departamento con la mayor/menor cantidad de 
    toneladas producidas . El mensaje  que se le muestra al usuario debe tener el siguiente formato:
        'El departamento que es el (mayor/menor) productor de un tipo de cultivo en toneladas es (departamento) con (cantidad) toneladas'.
    """
    departamento = input("Digite el departamento: ")
    print(mod.requ5(matriz, departamento))
    
            
def ejecutar_cantidad_toneladas_departamento(matriz:tuple) -> None:
    """Ejecuta la opcion que cuenta la cantidad de toneladas producidas en un departamento. 
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'Se produjeron un total de (cantidad) toneladas en el departamento de (departamento).'
    """
    
    mayor = input("Digite True si quiere el mayor, sino False: ")
    if mayor == "True":
        mayor = True
    else:
        mayor = False
    print(mod.requ6(mayor, matriz))

def ejecutar_departamento_estrella(matriz:tuple) -> None:
    """Ejecuta la opcion que determina si hay un departamento estrella.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El departamento (departamento) el una estrella, sus cultivos estrella son: (tc1), (tc2), (tc3).'
    Si no hay ningún departamento estrella le muestra el siguiente mensaje:
        'El departamento estrella es Ninguno.'
    """
    minimo = int(input("Digite digito minimo: "))
    print(mod.requ7(matriz, minimo))
        
def ejecutar_mapa(matriz:tuple) -> None:
    """Ejecuta la opcion que muestre el mapa con la producción de cada departamento en un tipo.
        Muestra en pantalla el mapa de Colombia con la producción de cada departamento según dicho tipo'
    """
    cultivo = input("Digite el tipo de cultivo : ")
    mod.requ8(cultivo, matriz)
        
def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar datos sobre el rendimiento de cultivos en Colombia.")
    print("2. Ver distribucion de los tipos de cultivo en un departamento")
    print("3. Ver top 10 de cultivos con mayor producción de toneladas X hectarea cosechada.")
    print("4. Ver diagrama de caja y bigotes respecto a la cantidad de toneladas producidas en un departamento.")
    print("5. Construccion de la matriz de Departamentos vs. Tipo_Cultivo.")
    print("6. Consultar la cantidad total de toneladas cosechadas en un departamento.")
    print("7. Consultar el departamento mayor/menor productor de un tipo de cultivo. ")
    print("8. Consultar si existen departamentos estrella")    
    print("9. Generar mapa de la producción de cada departamento para un tipo de cultivo en particular.")    
    print("10. Salir.") 

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
        elif opcion_seleccionada ==2:
            ejecutar_piechart_tipo_cultivo(datos)
        elif opcion_seleccionada ==3:
            ejecutar_diagrama_barras(datos)
        elif opcion_seleccionada ==4:
            ejecutar_toneladas_tipo_cultivo(datos)
        elif opcion_seleccionada ==5:
            matriz = ejecutar_crear_matriz(datos)
        elif opcion_seleccionada ==6:
            ejecutar_cantidad_toneladas_departamento(matriz)
        elif opcion_seleccionada ==7:
            ejecutar_depto_mayor_o_menor_productor(matriz)            
        elif opcion_seleccionada ==8:
            ejecutar_departamento_estrella(matriz)
        elif opcion_seleccionada ==9:
            ejecutar_mapa(matriz)
        elif opcion_seleccionada ==10:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()