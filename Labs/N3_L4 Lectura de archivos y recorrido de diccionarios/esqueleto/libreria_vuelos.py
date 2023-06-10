# -*- coding: utf-8 -*-


def cargar_vuelos(ruta_archivo: str)->dict:
    """
    Esta función carga la información un conjunto de vuelos a partir de un archivo CSV.
    Los valores dentro del archivo deben estar separados por comas y estar en el siguiente orden:
        aerolinea,codigo_vuelo,origen,destino,distancia,salida,duracion,retraso
    La primera línea del archivo debe corresponder a los títulos de las columnas.
    Parámetros:
        ruta_archivo: la ruta del archivo que se quiere cargar
    Retorno:
        Un diccionario con la información de los vuelos.
        Las llaves del diccionario corresponderán a los códigos de los vuelos.
        Los valores del diccionario deben ser también diccionarios con las siguientes llaves:
            aerolinea,origen,destino,distancia,salida,duracion,retraso
    """
    vuelos = {}
    archivo = open(ruta_archivo)
    titulos = archivo.readline().split(",")

    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_vuelo = datos[1]
        vuelo = {}
        vuelo["aerolinea"] = datos[0]
        vuelo["origen"] = datos[2]
        vuelo["destino"] = datos[3]
        vuelo["distancia"] = datos[4]
        vuelo["salida"] = datos[5]
        vuelo["duracion"] = datos[6]
        vuelo["retraso"] = datos[7]
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()

    archivo.close()
    return vuelos

    
def vuelos_directos(vuelos: dict, origen: str, destino: str)->list:
    lista = []
    
    
    for i in vuelos:
        if vuelos[i]["origen"] == origen and vuelos[i]["destino"] == destino:
            dic ={}
            dic[i] = vuelos[i]
            lista.append(dic)
            
    return lista


def vuelos_con_una_escala(vuelos: dict, origen: str, destino: str)->list:
    lista   = []
    escala  = []
    primeros_vuelos = []
    segundos_vuelos = []
    primer_destino = ""
    destino_final = ""
    
    
    for i in vuelos:
        if  vuelos[i]["destino"] == destino and vuelos[i]["origen"] != origen:
            escala.append(i)
    
    for i in vuelos :
        if vuelos[i]["origen"] == origen and vuelos[i]["destino"] != destino:
            primer_destino = vuelos[i]["destino"]
        for i in escala:
            if primer_destino == vuelos[i]["origen"]:
                segundos_vuelos.append(i)
                destino_final = vuelos[i]["destino"]
            for i in vuelos:
                if vuelos[i]["origen"] == origen and vuelos[i]["destino"]== destino_final:
                    primeros_vuelos.append(i)
                
    lista.append(primeros_vuelos)
    lista.append(segundos_vuelos)
            
    return lista
                
                
    

def sugerir_aerolinea(vuelos: dict, origen: str, destino: str)->str:
    
    lista = []
    
    for i in vuelos :
            if vuelos[i]["origen"] == origen and vuelos[i]["destino"] == destino:
                dic ={}
                dic[i] = vuelos[i]
                lista.append(dic)
    
    minimo = 1000      
    for i in lista:
        
        if minimo > i ["retraso"]:
            minimo = i ["retraso"]
            rta = i ["aerolinea"]
            
        else:
            None
            
    return rta

