"""
Ejercicio nivel 2: Videojuegos
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: Cupi2

"""


def crear_videojuego(titulo: str, anio_de_lanzamiento: int, generos: str, rating: float,
                     es_multijugador: bool, clasificacion_edad: str, duracion: int) -> dict:
    """
    Función para crear un videojuego en la plataforma.

    Parámetros
    ----------

    titulo : str
        Título del videojuego.
    anio_de_lanzamiento : int
        Año de lanzamiento del videojuego.
    generos : str
        Géneros del videojuego separados por coma
    rating : float
        Rating IGN del videojuego, en el rango [0.0, 10.0].
    es_multijugador : bool
        Indica si el videojuego tiene algún modo multijugador.
    clasificacion_edad : str
        Clasificación de edad del videojuego según la ESRB.
    duracion : int
        Duración del videojuego según el sitio HowLongToBeat.
        El formato es XY, con X como las horas y Y como los minutos, ejemplo: 3221.

    Retorno
    -------
    dict
        Diccionario del videojuego con su información.

    """
    rta = {}
    rta["titulo"] = titulo
    rta["anio_de_lanzamiento"] = anio_de_lanzamiento
    rta["generos"] = generos
    rta["rating"] = rating
    rta["es_multijugador"] = es_multijugador
    rta["clasificacion_edad"] = clasificacion_edad
    rta["duracion"] = duracion
    return rta


def buscar_videojuego_por_titulo(j1: dict, j2: dict, j3: dict, j4: dict, titulo: str) -> dict:
    """
    Busca un videojuego en particular por su título.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    titulo : str
        Título del videojuego que se desea buscar.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego encontrado. Si no se encuentra el videojuego,
        retorna None.

    """
    if j1["titulo"] == titulo:
        rta = j1
    elif j2["titulo"] == titulo:
        rta = j2
    elif j3["titulo"] == titulo:
        rta = j3
    elif j4["titulo"] == titulo:
        rta = j4
    else:
        rta = None
    return rta


def buscar_videojuego_mas_corto(j1: dict, j2: dict, j3: dict, j4: dict) -> dict:
    """
    Busca el videojuego más corto de una lista de videojuegos.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego más corto.

    """
    durMin = min(j1["duracion"], j2["duracion"], j3["duracion"], j4["duracion"])
    
    if j1["duracion"] == durMin:
        rta = j1
    elif j2["duracion"] == durMin:
        rta = j2
    elif j3["duracion"] == durMin:
        rta = j3
    elif j4["duracion"] == durMin:
        rta = j4
    
    return rta


def calcular_dias_necesarios_para_terminar_videojuego(juego: dict, horas_disponibilidad: int) -> int:
    """
    Calcula los días necesarios para terminar un videojuego.

    Parámetros
    ----------
    juego : dict
        Diccionario que contiene la información del videojuego.
    horas_disponibilidad : int
        Horas disponibles por día para jugar.

    Retorno
    -------
    int
        Número de días necesarios para terminar el videojuego.

    """
    duracion = juego["duracion"]
    rta = duracion//100
    if (duracion% 24 != 0):
        rta += 1
    return rta


def mostrar_videojuegos_aptos_para_cierta_edad(j1: dict, j2: dict, j3: dict, j4: dict, edad: int) -> str:
    """
    Retorna una cadena con los títulos de los videojuegos aptos para una cierta edad.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    edad : int
        Edad a la que se desea verificar la aptitud de los videojuegos.

    Retorno
    -------
    str
        Cadena con los títulos de los videojuegos aptos para la edad especificada. Si no hay juegos aptos,
        retorna un mensaje indicando que no hay juegos aptos para la edad especificada.

    """
    rta= ""
    if (j1["clasificacion_edad"]=="E" ) or (j1["clasificacion_edad"]=="E10+" and edad > 10) or (j1["clasificacion_edad"]=="T" and edad > 13) or (j1["clasificacion_edad"]=="M" and edad > 17):
        rta += j1["titulo"]
    if (j2["clasificacion_edad"]=="E" ) or (j2["clasificacion_edad"]=="E10+" and edad > 10) or (j2["clasificacion_edad"]=="T" and edad > 13) or (j2["clasificacion_edad"]=="M" and edad > 17):
        rta += j2["titulo"]
    if (j3["clasificacion_edad"]=="E" ) or (j3["clasificacion_edad"]=="E10+" and edad > 10) or (j3["clasificacion_edad"]=="T" and edad > 13) or (j3["clasificacion_edad"]=="M" and edad > 17):
        rta += j3["titulo"]
    if (j4["clasificacion_edad"]=="E" ) or (j4["clasificacion_edad"]=="E10+" and edad > 10) or (j4["clasificacion_edad"]=="T" and edad > 13) or (j4["clasificacion_edad"]=="M" and edad > 17):
        rta += j4["titulo"]
        
    return rta
    

def aux_mostrar_videojuegos_aptos_para_cierta_edad(rta: str, j: dict, edad: int) -> str:
    """Agrega a la lista un video juego con respecto a cierta edad

    Args:
        rta (str): _description_
        j (dict): _description_
        edad (int): _description_

    Returns:
        str: _description_
    """
#     if j["clasificacion_edad"] == "E":
#         rta += j["nombre"] + str(", ")
#     elif j["clasificacion_edad"] == "E10+" and edad >= 10:
#         rta += j["nombre"] + str(", ")
#     elif j["clasificacion_edad"] == "T" and edad >= 13:
#         rta += j["nombre"] + str(", ")
#     elif j["clasificacion_edad"] == "M" and edad >= 17:
#         rta += j["nombre"] + str(", ")
#     return rta


def determinar_puntaje_de_un_videojuego(juego: dict) -> float:
#     """
#     Calcula el puntaje de un videojuego en base a su rating y duración.

#     Parámetros:
#     - juego (dict): Diccionario que contiene la información del videojuego.

#     Retorna:
#     - float: Puntaje del videojuego.

#     puntos por:

#     anio_de_lanzamiento -> mas reciente es mejor | 2020s -> 4 | 2010s -> 3 | 2000s -> 2 | 1990s -> 1 | 1980s -> 0
#     generos -> mas generos mejor | carreras o deportes -> 4 | accion o aventura -> 3 | estrategia o simulacion -> 2 | rol o plataformas -> 1
#     rating -> mas rating mejor | divida el rating en 2 y restarle 1
#     es_multijugador -> si es multijugador sume 5 puntos
#     clasificacion_edad -> mas inclusivo mejor | E -> 4 | E10+ -> 3 | T -> 2 | M -> 1
#     duracion -> quiero que dure lo justo | entre 1 y 3 hr -> 2 | entre 3 y 10 hr -> 4 | mas de 10 hr -> 2

#     """
#     puntaje = 0
#     if juego["anio_de_lanzamiento"] >= 2020 and juego["anio_de_lanzamiento"] < 2029:
#         puntaje += 4
#     elif juego["anio_de_lanzamiento"] >= 2010 and juego["anio_de_lanzamiento"] < 2019:
#         puntaje += 3
#     elif juego["anio_de_lanzamiento"] >= 2000 and juego["anio_de_lanzamiento"] < 2009:
#         puntaje += 2
#     elif juego["anio_de_lanzamiento"] >= 1990 and juego["anio_de_lanzamiento"] < 1999:
#         puntaje += 1
        
#     if ("carreras" in juego["generos"]) or ("deportes" in juego["generos"]):
#         puntaje += 4
#     elif "accion" in juego["generos"] or ("aventura" in juego["generos"]):
#         puntaje += 3
#     elif "estrategia" in juego["generos"] or ("simulacion" in juego["generos"]):
#         puntaje += 2
#     elif "rol" in juego["generos"] or ("plataformas" in juego["generos"]):
#         puntaje += 1
        
#     puntaje += (juego["rating"]/2)-1
    
#     if juego["es_multijugador"] == True:
#         puntaje += 5
        
#     if juego["clasificacion_edad"] == "E":
#         puntaje += 4
#     elif juego["clasificacion_edad"] == "E10+":
#         puntaje += 3
#     elif juego["clasificacion_edad"] == "T":
#         puntaje += 2
#     elif juego["clasificacion_edad"] == "M":
#         puntaje += 1
    
#     if juego["duracion"] > 1030 and juego["duracion"] <= 3000:
#         puntaje += 2
#     elif juego["duracion"] > 3000 and juego["duracion"] <= 10000:
#         puntaje += 4
#     elif juego["duracion"] > 10000:
#         puntaje += 2
    
#     return puntaje

    puntaje=0
    anio_lanzamiento=juego["anio_de_lanzamiento"]
    genero=juego["generos"]
    clasificacion_edad=juego["clasificacion_edad"]
    duracion=juego["duracion"]//100
   
    puntaje+= (juego["rating"]/2)-1
    if anio_lanzamiento >= 2020:
        puntaje+=4
    elif anio_lanzamiento >=2010:
        puntaje+=3
    elif anio_lanzamiento >=2000:
        puntaje+=2
    elif anio_lanzamiento >=1990:
        puntaje+=1
    elif anio_lanzamiento >=1980:
        puntaje+=3
       

    if genero in "carreras" or  genero in "simulacion":
        puntaje+=4
    elif genero in "deportes":
        puntaje+=3
    # a = genero in "acción"
    # b = genero in "aventura"
    elif ("acción" in genero ) or ("aventura" in genero ) or (genero in "plataformas"):
        puntaje+=2
    elif genero in "rol" or "estrategia":
        puntaje+=1
        #solo está esta mal
       
    if juego["es_multijugador"] == True:
        puntaje+=5
       
    if clasificacion_edad == "E":
        puntaje+=4
    elif clasificacion_edad == "E10+":
        puntaje+=3
    elif clasificacion_edad == "T":
        puntaje+=2
    elif clasificacion_edad == "M":
        puntaje+=1
       
    if (duracion>=1 and duracion<=3) or (duracion>=10):
        puntaje+=2
    if duracion>3 and duracion<=10:
        puntaje+=4

    return round(puntaje,2)


def contar_cantidad_de_juegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> int:
    """
    Cuenta la cantidad de juegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - int: Cantidad de videojuegos del género especificado.

    """
    rta = 0
    if genero in j1["genero1"]:
        rta += 1
    if genero in j2["genero1"]:
        rta += 1
    if genero in j3["genero1"]:
        rta += 1
    if genero in j4["genero1"]:
        rta += 1
    return rta


def calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> float:
    """
    Calcula el promedio de rating de los videojuegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - float: Promedio de rating de los videojuegos del género especificado. Si no hay videojuegos del género,
    retorna -1.

    """
    num_juegos, rating_T = 0, 0
    num_juegos, rating_T = aux_calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j1, genero, num_juegos, rating_T)
    num_juegos, rating_T = aux_calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j2, genero, num_juegos, rating_T)
    num_juegos, rating_T = aux_calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j3, genero, num_juegos, rating_T)
    num_juegos, rating_T = aux_calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j4, genero, num_juegos, rating_T)
    if (rating_T != 0):
        rta = rating_T/num_juegos
    else: 
        rta = -1
    return rta

def aux_calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(juego: dict, genero: str, num_juegos: int, rating_T: int)-> (int, int):
    if (genero in juego["generos"]):
        num_juegos += 1
        rating_T += juego["rating"]
    
    return num_juegos, rating_T
