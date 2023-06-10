# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Modulo de Funciones

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""
import pandas as pd 
import matplotlib.pyplot as plt

def cargar_matriz_estadisticas(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """  
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0,facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,elementos+1):
            estadisticas[i][j] = datos[j].strip()
        i += 1 
        linea = archivo.readline()
    archivo.close()
    
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0,oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,ocupantes+1):
            puestos[i][j] = datos[j].strip()
        i += 1 
        linea = archivo1.readline()
    archivo1.close()
    
    return puestos

def cargar_matriz_dobles(ruta_archivo: str)-> list:
    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    lista = []
    
    for i in range(0, 36):
        lista.append([0]* 36)

    i = 0;
    
    while len(linea) > 0:    
        datos = linea.split(",")
        for j in range(0, 36):
            lista[i][j] = datos[j].strip()
        i += 1
        linea = archivo2.readline()
    archivo2.close()
    
    return lista

prueba =cargar_matriz_estadisticas("estadisticas_facultades.csv")
prueba1 = cargar_matriz_puestos("matriz_puestos.csv")
prueba2 = cargar_matriz_dobles("matriz_dobles.csv")

#TODO Implemente las demas funciones de su programa

def puestos_atendidos(matriz_puestos: list, facultad: str)-> int:
    suma = 0
    for i in range(0, len(matriz_puestos)):
        if matriz_puestos[i][0] == facultad:
            guardado = i
    for j in range(1, (len(matriz_puestos))+1):
        suma += int(matriz_puestos[guardado][j])
    return suma

def puestos_ocupados(matriz_puestos: list, facultad: str)-> int:
    suma = 0
    for i in range(0, len(matriz_puestos)):
        if matriz_puestos[0][i] == facultad:
            g = i
    for j in range(1, len(matriz_puestos)):
        suma += int(matriz_puestos[j][g])
    return suma

def facultad_mas_servicial(matriz_puestos: list)-> tuple:
    respuesta = [0]
    for i in range(1,12):
        facultad = matriz_puestos[i][0]
        total = puestos_atendidos(matriz_puestos, facultad)
        cada_facultad = matriz_puestos[i][i]
        a = total- int(cada_facultad)
        humildad = round(((a/total)*100),2)
        if humildad > respuesta[0]:
            respuesta.clear()
            respuesta.insert(1, facultad)
            respuesta.insert(0, humildad)
    respuesta = respuesta[::-1]
    respuesta = [respuesta[0], str(respuesta[1]) + "%"]
    return tuple(respuesta)

def hay_facultad_generosa(matriz_puestos: list, facultad: str, porcentaje: int)-> tuple:
    total1 = puestos_ocupados(matriz_puestos, facultad)
    total = total1*(porcentaje/100)
    guardado = ""
    respuesta = ("No existe facultadad", 0)
    for i in range(len(matriz_puestos)):
        if matriz_puestos[i][0] == facultad:
            guardado = i 
    for j in range(1, (len(matriz_puestos))):
        a = matriz_puestos[j][guardado]
        nombre = matriz_puestos[j][0]
        humildad = round(((int(a)/total1)*100),2)    
        if nombre != facultad:
            if float(a) > total:
                respuesta = (nombre, str(humildad) +"%")
                break
    return respuesta
        
def calcular_autocubrimiento(matriz_puestos: list, matriz_estadisticas: list)-> list:
    matriz_estadisticas[0].append("Autocubrimiento")
    for a in range(1, len(matriz_puestos)):
        facultad = matriz_puestos[a][0]
        autocubrimiento = round((puestos_ocupados(matriz_puestos, facultad))/(puestos_atendidos(matriz_puestos, facultad)),2)
        matriz_estadisticas[a].append(autocubrimiento)       
    return matriz_estadisticas
        
def doble_mas_comun(matriz_dobles: list)-> tuple:
    suma = 0 
    for i in range(1, len(matriz_dobles)):
        for j in range(1, len(matriz_dobles[0])):
            suma_2=int(matriz_dobles[i][j]) + int(matriz_dobles[j][i])
            if int(suma) < suma_2:
                suma = suma_2
                respuesta = (matriz_dobles[0][i]+ "-"+ matriz_dobles[j][0], suma)
    return respuesta

def mostrar_pga_promedio(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)
    df.set_index("Unnamed: 0", inplace= True)
    df_sorted = df.sort_values(by="PGA promedio")
    promedio = df_sorted["PGA promedio"]
    promedio.plot.bar(figsize = (7,5), width=0.95)
    plt.xlabel("Facultad")
    plt.ylabel("PGA Promedio")
    plt.title("PGA Promedio")
    plt.ylim(3.5, 4.2)
    plt.show()

def mostrar_puestos_estudios_dirigidos(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)
    df.set_index("Unnamed: 0", inplace = True)
    a = df["Estudios Dirigidos"]
    separacion = [0.02] * len(df)
    a.plot.pie(figsize = (7,5), explode= separacion)
    plt.ylabel("")
    plt.title("Uso puesto Estudios Dirigidos")
    plt.show()
    

#if x+i>=0 and x+i<alto and y+j>=0 and y+j<ancho: 

#mostrar_pga_promedio("estadisticas_facultades.csv")

mostrar_puestos_estudios_dirigidos("matriz_puestos.csv")


