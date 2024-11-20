# -*- coding: utf-8 -*-

def cargar_tablero_goles(ruta_archivo: str)->list:
    """
    Esta función carga la información de un tablero de goles 
    a partir de un archivo CSV.
    La primera fila del archivo contiene la dimensión del tablero (cuadrado)
    Parámetros:
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con el tablero de goles
    """
    archivo = open(ruta_archivo)
    dimensiones = archivo.readline().split(",")
    filas = int(dimensiones[0])
    columnas = filas
    
    tablero = []
    for i in range(0,filas):
        tablero.append([0] * columnas)

    linea = archivo.readline()
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,columnas):
            tablero[i][j] = int(datos[j])
        i += 1 
        linea = archivo.readline()

    archivo.close()
    return tablero

def cargar_equipos(ruta_archivo: str)->dict:
    """
    Esta función carga la información de los equipos 
    a partir de un archivo CSV.
    La primera fila del archivo contiene la cantidad de equipos
    Parámetros:
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: dict
        Un diccionario en el cual las llaves son los nombres de los equipos y 
        los valores son unos índices consecutivos
    """
    archivo = open(ruta_archivo)
    equipos = {}
    linea = archivo.readline()
    
    while len(linea) > 0:
        datos = linea.split(",")
        equipos[datos[0]] = int(datos[1])
        linea = archivo.readline()

    archivo.close()
    return equipos

def anotar_marcador(tablero_goles: list, equipos:dict, equipo1:str, equipo2: str, marcador:str)->list:
    """
    Esta función registra el marcador de un partifo en el tablero de goles 
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
        equipos (dict): diccionario de los equipos del campeonato
        equipo1 (string): nombre del primer equipo del partido
        equipo2 (string): nombre del segundo equipo del partido
        marcador (string): string con formato goles1-goles2, donde goles1 son los goles que equipo1
        marcó a equipo2 y goles2 son los goles que equipo2 marcó a equipo1
    Retorno: list
        La matriz de goles actulizada
    """
    posEquipo1 = int(equipos.get(equipo1))
    posEquipo2 = int(equipos.get(equipo2))
    marcador = marcador.split("-")
    tablero_goles[posEquipo1][posEquipo2] = int(marcador[0])
    tablero_goles[posEquipo2][posEquipo1] = int(marcador[1])
    return tablero_goles

def total_goles(tablero_goles: list)->int:
    rta = 0
    for lista in tablero_goles:
        for i in lista:
            if i != -2 and i != -1:
                rta += i
        
    return rta

def partidos_jugados(tablero_goles: list)->int:
    rta = 0
    for lista in tablero_goles:
         for i in lista:
             if i != -2 and i != -1:
                 rta += 1
        
    return rta/2

def equipo_mas_goleador(tablero_goles: list, equipos:dict)->list:
    maxi_goles = 0
    for i in range(len(tablero_goles)):
        suma = 0
        for j in range(len(tablero_goles[i])):
            if tablero_goles[i][j] != -2 and tablero_goles[i][j] != -1:
                suma += tablero_goles[i][j]
        if suma > maxi_goles:
            maxi_goles = suma
            equipo_mas_goleador = i
    return equipos[equipo_mas_goleador]
    
        

def equipo_mas_goleado(tablero_goles: list, equipos:dict)->str:
    """
    Esta función retorna el nombre del equipo al cual le han marcado más goles en el
    campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
        equipos (dict): diccionario de los equipos del campeonato
    Retorno: str
        El nombre del equipo más goleado del campeonato
    """
    columna_goleada = 0
    maxi = 0
    lista = [0] * 8
    for i in range(len(tablero_goles)):
        suma = 0
        for j in range(len(tablero_goles[i])):
            if tablero_goles[j][i] != -2 and tablero_goles[j][i] != -1:
                suma += tablero_goles[j][i]
        lista[j] = suma
    for i in range(len(lista)):
        if lista[i] > maxi:
            maxi = lista[i]
            columna_goleada = i
    return equipos[columna_goleada]


def partidos_empatados(tablero_goles: list)->int:
    goles = []
    rta = 0
    for equipo in tablero_goles:
        puntos = 0
        for i in equipo:
            if i >0:
                puntos += i
        goles.axppend(puntos)
        
    for comparacion in goles:
        for equipo in goles:
            contador=0
            if comparacion== equipo:
                contador+= 1
            if contador>1:
                rta += 1
                
    return rta

def mayor_numero_goles(tablero_goles: list)->int:
    """
    Esta función calcula el mayor número de goles marcados en un partido del campeonato 
    (sumando los goles de los dos equipos)

    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
    Retorno: int
        El mayor número de goles marcados en un partido del campeonato
    """
    rta = 0
    for i in range(len(tablero_goles)):
        for j in range(len(tablero_goles[i])):
            if tablero_goles[i][j] + tablero_goles[j][i] > rta:
                rta = tablero_goles[i][j] + tablero_goles[j][i]
    return rta



