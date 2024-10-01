# -*- coding: utf-8 -*-
"""
CupiTikTok:

@author: Cupi2
"""


def construir_creador(
    nombre: str,
    pais: str,
    categorias: str,
    likes: int,
    vistas: int,
    seguidores: int,
    fecha_ultima_publicacion: int,
) -> dict:
    """
    Crea un diccionario con la información de un creador de contenido.

    Parámetros:
    nombre (str): Nombre del creador de contenido.
    pais (str): País de origen del creador de contenido.
    categorias (str): Categoría de los videos del creador de contenido.
    likes (int): Cantidad de likes que ha recibido el creador de contenido.
    vistas (int): Cantidad de vistas que ha recibido el creador de contenido.
    seguidores (int): Cantidad de seguidores que tiene el creador de contenido.
    fecha_ultima_publicacion (int): Fecha de la última publicación del creador
        de contenido en formato YYYYMMDD.

    Retorno:
    dict: Diccionario con la información del creador de contenido.
    """
    creador = {
        "nombre": nombre,
        "pais": pais,
        "categorias": categorias,
        "likes": likes,
        "vistas": vistas,
        "seguidores": seguidores,
        "fecha_ultima_publicacion": fecha_ultima_publicacion,
    }

    return creador


def buscar_creador_por_nombre(nombre: str, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca si entre los creadores de contenido dados, hay uno con el nombre ingresado.

    Parámetros:
        nombre (str): Nombre del creador de contenido a buscar.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario del creador de contenido con el nombre ingresado por el usuario.
            Retorna None si no hay ningún creador con ese nombre. Si dos creadores
            o más tienen el mismo nombre, retorna el primero encontrado.
    """
    # TODO1 - Solución
    tiktoker_encontrado = None  # Variable de retorno

    if c1["nombre"] == nombre:
        tiktoker_encontrado = c1
    elif c2["nombre"] == nombre:
        tiktoker_encontrado = c2
    elif c3["nombre"] == nombre:
        tiktoker_encontrado = c3
    elif c4["nombre"] == nombre:
        tiktoker_encontrado = c4

    return tiktoker_encontrado  # Se usa un solo retorno


def filtrar_creadores_por_categoria(categoria: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados según la categoría ingresada.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores que hacen contenido de la categoría dada,
            separados por comas. Retorna None si no hay ningún creador que haga
            parte de la categoría de interés ingresada.
    """
    # TODO2 - Solución
    creadores = ""  # Variable de retorno

    if categoria in c1["categorias"]:
        creadores = c1["nombre"]
    if categoria in c2["categorias"]:
        if creadores != "":
            creadores += ", "
        creadores += c2["nombre"]
    if categoria in c3["categorias"]:
        if creadores != "":
            creadores += ", "
        creadores += c3["nombre"]
    if categoria in c4["categorias"]:
        if creadores != "":
            creadores += ", "
        creadores += c4["nombre"]
    if creadores == "":
        creadores = None

    return creadores  # Se usa un solo retorno


def calcular_promedio_vistas(c1: dict, c2: dict, c3: dict, c4: dict) -> float:
    """
    Calcula el promedio de vistas de todos los creadores de contenido dados.

    Parámetros:
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        float: Promedio de vistas de todos los creadores de contenido dados,
            redondeado a dos cifras decimales.
    """
    # TODO3 - Solución
    suma_vistas = c1["vistas"] + c2["vistas"] + c3["vistas"] + c4["vistas"]
    promedio = suma_vistas / 4

    return round(promedio, 2)


def filtrar_creadores_por_vistas(minimo_vistas: int, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados que superen un mínimo de vistas (umbral).

    Parámetros:
        minimo_vistas (int): Umbral de vistas.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores de contenido dados que superan el mínimo
            de vistas ingresado, separados por comas. Retorna el mensaje "Ninguno"
            si ningún creador de contenido supera el umbral.
    """
    # TODO4 - Solución
    creadores = ""  # Variable de retorno

    if c1["vistas"] > minimo_vistas:
        creadores = c1["nombre"]
    if c2["vistas"] > minimo_vistas:
        if creadores != "":
            creadores += ", "
        creadores += c2["nombre"]
    if c3["vistas"] > minimo_vistas:
        if creadores != "":
            creadores += ", "
        creadores += c3["nombre"]
    if c4["vistas"] > minimo_vistas:
        if creadores != "":
            creadores += ", "
        creadores += c4["nombre"]
    if creadores == "":
        creadores = "Ninguno"

    return creadores  # Se usa un solo retorno


def calcular_rating_creador(creador: dict) -> float:
    """
    Calcula el rating de un creador de contenido con base en su número de
    seguidores, likes y vistas usando la fórmula F1.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.

    Retorno:
        float: El rating del creador de contenido, redondeado a dos cifras
            decimales. Este valor se encuentra entre 0 y 100.
    """
    # TODO5 - Solución
    S_MAX = 600_000
    L_MAX = 100_000_000
    V_MAX = 100_000_000
    rating = (
        (creador["seguidores"] / S_MAX) * 0.5
        + (creador["likes"] / L_MAX) * 0.3
        + (creador["vistas"] / V_MAX) * 0.2
    )

    return round(rating, 2)


def calcular_puntaje_afinidad(creador: dict, categoria: str, minimo_rating: float, pais: str) -> float:
    """
    Calcula el puntaje de afinidad entre un creador de contenido y un
    usuario basándose en una categoría, un país y un rating mínimo dados.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.
        categoria (str): Categoría de interés para el usuario.
        minimo_rating (float): Rating mínimo que debe tener el creador de contenido.
            Este valor se encuentra entre 0 y 100.
        pais (str): Nombre del país de interés para el usuario.

    Retorno:
        float: El puntaje de afinidad que tiene un creador con un usuario,
            redondeado a dos cifras decimales.
    """
    # TODO6 - Solución
    afinidad = 0

    puntaje = calcular_rating_creador(creador)
    if creador["pais"] == pais:
        afinidad += 2
    else:
        afinidad -= 1
    if categoria in creador["categorias"]:
        afinidad += 3
    if puntaje < minimo_rating:
        afinidad -= 5
    else:
        afinidad += 2

    return afinidad  # Se usa un solo retorno


def buscar_creador_favorito(categoria: str, rating: float, pais: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Busca el creador de contenido con el mayor puntaje de afinidad, teniendo
        en cuenta la categoría, el país y un rating mínimo especificados.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        rating (float): Rating mínimo que debe tener el creador de contenido.
        pais (str): Nombre del país de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: El nombre del creador de contenido con mayor puntaje de afinidad
            y su puntaje obtenido como sigue: "{nombre} con puntaje {puntaje_afinidad}",
            por ejemplo: "Code_Destroyer2002 con puntaje 100".
            Si dos creadores resultan con el mismo puntaje de afinidad, se retorna la
            información del que tenga el nombre alfabéticamente anterior/menor 
            (considerando el orden de sus caracteres en el abecedario). 
    """
    # TODO7 - Solución
    puntaje_c1 = calcular_puntaje_afinidad(c1, categoria, rating, pais)
    puntaje_c2 = calcular_puntaje_afinidad(c2, categoria, rating, pais)
    puntaje_c3 = calcular_puntaje_afinidad(c3, categoria, rating, pais)
    puntaje_c4 = calcular_puntaje_afinidad(c4, categoria, rating, pais)

    mayor_puntaje = puntaje_c1
    creador_favorito = c1["nombre"]

    if puntaje_c2 > mayor_puntaje or (
        puntaje_c2 == mayor_puntaje and c2["nombre"] < creador_favorito
    ):
        mayor_puntaje = puntaje_c2
        creador_favorito = c2["nombre"]

    if puntaje_c3 > mayor_puntaje or (
        puntaje_c3 == mayor_puntaje and c3["nombre"] < creador_favorito
    ):
        mayor_puntaje = puntaje_c3
        creador_favorito = c3["nombre"]

    if puntaje_c4 > mayor_puntaje or (
        puntaje_c4 == mayor_puntaje and c4["nombre"] < creador_favorito
    ):
        mayor_puntaje = puntaje_c4
        creador_favorito = c4["nombre"]

    respuesta = str(creador_favorito) + " con puntaje " + str(mayor_puntaje)

    return respuesta  # Se usa un solo retorno


def buscar_creador_inactivo(fecha_de_referencia: int, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca al creador de contenido que lleva el mayor tiempo sin publicar
        con base en una fecha ingresada por parámetro y la llave
        fecha_ultima_publicacion.

    Parámetros:
        fecha_de_referencia (int): Fecha con la que se busca hacer el análisis
            de actividad en formato YYYYMMDD.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario con las llaves: "nombre", "dias", "meses" y "anios",
            cuyos valores son respectivamente el nombre del creador más inactivo y 
            el tiempo de inactividad en años, meses y días.
            Si dos creadores tienen el mismo tiempo sin publicar, retorna el
            que tenga menos seguidores.
            Si la fecha ingresada es anterior a todas las fechas de última publicación,
            retorna None.
    """
    # TODO8 - Solución - con función auxiliar
    dias_c1 = calcular_dias(fecha_de_referencia, c1["fecha_ultima_publicacion"])
    dias_c2 = calcular_dias(fecha_de_referencia, c2["fecha_ultima_publicacion"])
    dias_c3 = calcular_dias(fecha_de_referencia, c3["fecha_ultima_publicacion"])
    dias_c4 = calcular_dias(fecha_de_referencia, c4["fecha_ultima_publicacion"])

    mayor_dias = dias_c1
    creador_menos_activo = c1

    if dias_c2 > mayor_dias or (
        dias_c2 == mayor_dias and c2["seguidores"] < creador_menos_activo["seguidores"]
    ):
        mayor_dias = dias_c2
        creador_menos_activo = c2

    if dias_c3 > mayor_dias or (
        dias_c3 == mayor_dias and c3["seguidores"] < creador_menos_activo["seguidores"]
    ):
        mayor_dias = dias_c3
        creador_menos_activo = c3

    if dias_c4 > mayor_dias or (
        dias_c4 == mayor_dias and c4["seguidores"] < creador_menos_activo["seguidores"]
    ):
        mayor_dias = dias_c4
        creador_menos_activo = c4

    if mayor_dias < 0:
        creador_inactivo = None
    else:
        creador_inactivo = {
            "nombre": creador_menos_activo["nombre"],
            "dias": (mayor_dias % 360) % 30,
            "meses": (mayor_dias % 360) // 30,
            "anios": mayor_dias // 360,
        }

    return creador_inactivo  # Se usa un solo retorno


# Función opcional para TODO8
def calcular_dias(fecha_de_referencia: int, fecha_ultima_publicacion: int) -> int:
    """
    Calcula la cantidad de días que han pasado entre dos fechas.

    Parámetros:
    fecha_de_referencia (int): Fecha con la que se busca hacer el análisis de
        actividad en formato YYYYMMDD.
    fecha_ultima_publicacion (int): Fecha de la última publicación del creador
        de contenido en formato YYYYMMDD.

    Retorno:
    int: Cantidad de días que han pasado entre las dos fechas.
    """
    anio_referencia = fecha_de_referencia // 10000
    mes_referencia = (fecha_de_referencia % 10000) // 100
    dia_referencia = fecha_de_referencia % 100

    anio_publicacion = fecha_ultima_publicacion // 10000
    mes_publicacion = (fecha_ultima_publicacion % 10000) // 100
    dia_publicacion = fecha_ultima_publicacion % 100

    dias = (anio_referencia - anio_publicacion) * 360
    dias += (mes_referencia - mes_publicacion) * 30
    dias += dia_referencia - dia_publicacion

    return dias  # Se usa un solo retorno
