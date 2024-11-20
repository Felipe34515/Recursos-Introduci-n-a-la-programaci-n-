# -*- coding: utf-8 -*-
"""
Aplicación de Restaurantes

@author: Cupi2
"""

# Función 1:
def cargar_restaurantes(archivo: str) -> dict:
    """
    Carga un archivo CSV con la información de los restaurantes y los organiza por estado.

    Parámetros:
        archivo (str): Nombre del archivo CSV con la información de los restaurantes.

    Retorno:
        dict: Diccionario donde las llaves son los estados y los valores son listas de diccionarios,
              cada uno representando un restaurante con la siguiente estructura:
              {
                  "name": str,         # Nombre del restaurante.
                  "category": str,     # Categoría del restaurante.
                  "rating": float,     # Calificación del restaurante.
                  "latitude": float,   # Latitud de la ubicación del restaurante.
                  "longitude": float,  # Longitud de la ubicación del restaurante.
                  "city": str,         # Ciudad donde se encuentra el restaurante.
                  "state": str,        # Estado donde se encuentra el restaurante.
                  "price": str,        # Indicador de coste del restaurante ($, $$, $$$, $$$$).
                  "review_count": int, # Número de personas que han calificado al restaurante.
                  "delivery": bool,    # Indicador de si tiene servicio a domicilio (0: False, 1: True).
                  "address": str       # Dirección del restaurante.
              }
    """
    estados = {}  # Variable de retorno.
    archivo = open(archivo, "r", encoding="utf-8")
    archivo.readline()

    linea = archivo.readline().strip()
    while linea != "":
        linea = linea.split(",")

        restaurante = {
            "name": linea[0],
            "category": linea[1],
            "rating": float(linea[2]),
            "latitude": float(linea[3]),
            "longitude": float(linea[4]),
            "city": linea[5],
            "state": linea[6],
            "price": linea[7],
            "review_count": int(linea[8]),
            "delivery": linea[9] == "1",  # delivery cambia a bool
            "address": linea[10],
        }
        if restaurante["state"] not in estados:
            estados[restaurante["state"]] = []
        estados[restaurante["state"]].append(restaurante)

        linea = archivo.readline().strip()

    archivo.close()
    
    return estados  # Se usa un solo retorno.


# Función 2:                                        
def buscar_restaurantes_en_area(estados: dict, latitud_min: float, latitud_max: float, longitud_min: float, longitud_max: float) -> list:
    """
    Busca a los restaurantes ubicados en un área acotada por las latitudes y longitudes dadas por parámetro.

    Parámetros:
        estados (dict): Diccionario de estados.
        latitud_min (float): Límite inferior del área a analizar en latitud.
        latitud_max (float): Límite superior del área a analizar en latitud.
        longitud_min (float): Límite izquierdo del área a analizar en longitud.
        longitud_max (float): Límite derecho del área a analizar en longitud.

    Retorno:
        list: Lista de restaurantes ubicados en el área especificada.
              Si no se encuentran restaurantes en el área, retorna una lista vacía.
    """
    restaurantes_en_area = []  # Variable de retorno.
    
    for estado in estados:
        for restaurante in estados[estado]:
            if (latitud_min <= restaurante["latitude"] <= latitud_max) and (longitud_min <= restaurante["longitude"] <= longitud_max):
                restaurantes_en_area.append(restaurante)
                
    return restaurantes_en_area  # Se usa un solo retorno.


# Función auxiliar de Función 3:
def sucursales_de_un_restaurante_en_estado(estados: dict, nombre_restaurante: str, estado: str) -> list:
    """
    Busca a las sucursales de un restaurante en un estado específico.

    Parámetros:
        estados (dict): Diccionario de estados.
        nombre_restaurante (str): Nombre del restaurante del cual se buscan las sucursales.
        estado (str): Estado donde se buscan las sucursales del restaurante.

    Retorno:
        list: Lista con las sucursales del restaurante en el estado.
              Si no se encuentran sucursales del restaurante en el estado, retorna una lista vacía.
    """
    sucursales = []  # Variable de retorno.
    
    restaurantes = estados[estado]
    for restaurante in restaurantes:
        if restaurante["name"] == nombre_restaurante:
            sucursales.append(restaurante)
            
    return sucursales  # Se usa un solo retorno.

# Función 3:
def buscar_restaurante_mas_sucursales(estados: dict, estado: str) -> dict:
    """
    Busca el restaurante con más sucursales en un estado.
    Recuerde que las sucursales se refieren a sedes del restaurante que tienen el mismo nombre, pero diferentes ubicaciones.

    Parámetros:
        estados (dict): Diccionario de estados.
        estado (str): Estado del cual se quiere encontrar el restaurante con más sucursales.

    Retorno:
        dict: Diccionario con las llaves:
              - "nombre_restaurante": Nombre del restaurante con más sucursales en el estado.
              - "numero_sucursales": Número de sucursales del restaurante.
              Si no se encuentran restaurantes en el estado, retorna {"nombre_restaurante": "", "numero_sucursales": 0}.
    """
    
    respuesta = {
        "nombre_restaurante": "",
        "numero_sucursales": 0
    }   # Variable de retorno.
    
    max_sucursales_por_restaurante = 0
    restaurantes_estado = estados.get(estado, [])

    for restaurante in restaurantes_estado:
        nombre = restaurante["name"]
        sucursales = sucursales_de_un_restaurante_en_estado(estados, nombre, estado)
        
        cantidad_sucursales = len(sucursales)

        if cantidad_sucursales > max_sucursales_por_restaurante:
            respuesta["nombre_restaurante"] = nombre
            respuesta["numero_sucursales"] = cantidad_sucursales
            max_sucursales_por_restaurante = cantidad_sucursales

    return respuesta  # Se usa un solo retorno.


# Función 4:
def estandarizar_direcciones(estados: dict) -> None:
    """
    Reemplaza las abreviaciones en las direcciones de los restaurantes por su forma completa.

    Parámetros:
        estados (dict): Diccionario de estados.

    Retorno:
        None.
    """
    reemplazos = {
        "St": "Street",
        "Ave": "Avenue",
        "Sq": "Square",
        "Hwy": "Highway",
        "Blvd": "Boulevard",
        "Rd": "Road",
        "Dr": "Drive",
        "Ln": "Lane",
        "Ct": "Court",
        "Pl": "Place",
        "Pk": "Park",
        "Cir": "Circle",
        "Expy": "Expressway",
        "Trl": "Trail",
        "Rte": "Route",
        "Mt": "Mount",
        "Fwy": "Freeway",
    }
    
    for estado in estados:
        for restaurante in estados[estado]:
            direccion = restaurante["address"]
            palabras = direccion.split(" ")
            for i in range(len(palabras)):
                palabra_capitalizada = palabras[i].capitalize()
                if palabra_capitalizada in reemplazos:
                    palabras[i] = reemplazos[palabra_capitalizada]
            direccion = " ".join(palabras)
            restaurante["address"] = direccion


# Función 5:
def buscar_restaurantes_palindromos(estados: dict) -> list:
    """
    Busca a todos los restaurantes cuyos nombres sean palíndromos, ignorando mayúsculas y espacios.
    
    Ejemplo:
        Si un restaurante se llamara "Evil Olive", se consideraría un palíndromo.

    Parámetros:
        estados (dict): Diccionario de estados.

    Retorno:
        list: Lista de diccionarios con la información de los restaurantes cuyos nombres sean palíndromos.
              Si no se encuentra ningún restaurante con nombre palíndromo, retorna una lista vacía.
    """
    restaurantes_palindromos = []  # Variable de retorno.

    for estado in estados:
        restaurantes_estado = estados[estado]

        for restaurante in restaurantes_estado:
            nombre_limpio = restaurante["name"].replace(" ", "").lower()
            if nombre_limpio == nombre_limpio[::-1]:
                restaurantes_palindromos.append(restaurante)

    return restaurantes_palindromos  # Se usa un solo retorno.


# Función auxiliar de Función 6:
def distancia_cartesiana(latitud_min: float, latitud_max: float, longitud_min: float, longitud_max: float) -> float:
    """
    Calcula la distancia cartesiana entre dos puntos en un plano.

    Parámetros:
        latitud_min (float): Latitud del primer punto.
        latitud_max (float): Latitud del segundo punto.
        longitud_min (float): Longitud del primer punto.
        longitud_max (float): Longitud del segundo punto.

    Retorno:
        float: Distancia cartesiana entre los dos puntos.
    """
    return ((latitud_max - latitud_min) ** 2 + (longitud_max - longitud_min) ** 2) ** 0.5

# Función 6:
def buscar_restaurante_cercano(estados: dict, latitud_ref: float, longitud_ref: float) -> dict:
    """
    Busca el restaurante más cercano a un punto de referencia (latitud y longitud) ingresado por parámetro utilizando la distancia cartesiana.

    Parámetros:
        estados (dict): Diccionario de estados.
        latitud_ref (float): Latitud del punto de referencia.
        longitud_ref (float): Longitud del punto de referencia.

   Retorno:
        dict: Diccionario del restaurante más cercano al punto de referencia.
              En caso de que haya dos restaurantes a la misma distancia, retornar el último encontrado.
    """
    cercano = {}  # Variable de retorno.
    
    distancia_min = None
    for estado in estados:
        for restaurante in estados[estado]:
            distancia = distancia_cartesiana(latitud_ref, restaurante["latitude"], longitud_ref, restaurante["longitude"])
            if distancia_min is None or distancia < distancia_min:
                cercano = restaurante
                distancia_min = distancia
                
    return cercano  # Se usa un solo retorno.


#Función 7:
def buscar_restaurante_preferido(estados: dict, latitud_min: float, latitud_max: float, longitud_min: float, longitud_max: float, precio_maximo: str, minimo_reviews: int, rating_minimo: float) -> dict:
    """
    Busca el primer restaurante en un área determinada que cumpla con preferencias de precio, número de reviews y rating.

    Parámetros:
        estados (dict): Diccionario de estados.
        latitud_min (float): Límite inferior del área a analizar en latitud.
        latitud_max (float): Límite superior del área a analizar en latitud.
        longitud_min (float): Límite izquierdo del área a analizar en longitud.
        longitud_max (float): Límite derecho del área a analizar en longitud.
        precio_maximo (str): Precio máximo que está dispuesto a pagar.
        minimo_reviews (int): Umbral de reviews que debe superar un restaurante para ser considerado en la función.
        rating_minimo (float): Umbral de rating que debe superar un restaurante para ser considerado en la función.

    Retorno:
        dict: Diccionario con la información del primer restaurante que cumpla con las preferencias.
              Si no se encuentra ningún restaurante, retorna None.
    """
    i = 0
    restaurante_preferido = None  # Variable de retorno.
    encontrado = False  # Centinela para controlar si se ha encontrado un restaurante favorito.
    
    restaurantes_en_area = buscar_restaurantes_en_area(estados, latitud_min, latitud_max, longitud_min, longitud_max)

    while i < len(restaurantes_en_area) and not encontrado:
        restaurante = restaurantes_en_area[i]
        if (
            restaurante["price"].count("$") <= precio_maximo.count("$")
            and restaurante["review_count"] >= minimo_reviews
            and restaurante["rating"] >= rating_minimo
        ):
            encontrado = True  # Cambiar centinela si se encuentra un restaurante que cumple las condiciones.
            restaurante_preferido = restaurante
        i += 1

    return restaurante_preferido  # Se usa un solo retorno.