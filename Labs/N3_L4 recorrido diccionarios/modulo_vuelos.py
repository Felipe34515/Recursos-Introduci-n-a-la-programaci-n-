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
    archivo = open(ruta_archivo, "r")
    titulos = archivo.readline().split(",")

    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_vuelo = datos[1]
        vuelo = {}
        vuelo["aerolinea"] = datos[0]
        vuelo["origen"] = datos[2]
        vuelo["destino"] = datos[3]
        vuelo["distancia"] = int(datos[4])
        vuelo["salida"] = datos[5]
        vuelo["duracion"] = int(datos[6])
        vuelo["retraso"] = int(datos[7].strip("\n"))
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()

    archivo.close()
    return vuelos

    
def vuelos_directos(vuelos: dict, origen: str, destino: str)->list:
    pass

def vuelos_con_una_escala(vuelos: dict, origen: str, destino: str)->list:
    pass

def sugerir_aerolinea(vuelos: dict, origen: str, destino: str)->str:
    rta = {}
    retraso = 100000000
    for i in vuelos.keys():
        if vuelos[i]["origen"] == origen and vuelos[i]["destino"] == destino:
            if vuelos[i]["retraso"] < retraso:
                retraso = vuelos[i]["retraso"]
                rta = vuelos[i]
    return rta

def generar_reporte_adelantados(vuelos:dict)->None:
    pass