"""
Ejercicio nivel 2: videojuegos
Modulo de interacción por consola.

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

import videojuegos as vd


def mostrar_videojuego(videojuego: dict) -> None:

    titulo = videojuego["titulo"]  # string
    anio_de_lanzamiento = videojuego["anio_de_lanzamiento"]  # int
    generos = videojuego["generos"]  # string
    rating = videojuego["rating"]  # float
    es_multijugador = videojuego["es_multijugador"]  # bool
    clasificacion_edad = videojuego["clasificacion_edad"]  # string
    # string (formato Xh Ym, con X horas y Y minutos)
    duracion = videojuego["duracion"]

    print("Título: " + titulo +
          "\n\nAño de lanzamiento: " + str(anio_de_lanzamiento) +
          "\n\nGéneros del videojuego: " + generos +
          "\n\nRating del videojuego: " + str(rating) +
          "\n\n¿Es multijugador?: " + str(es_multijugador) +
          "\n\nClasificación de edad: " + clasificacion_edad +
          "\n\nDuración del videojuego: " + str(duracion) + " horas"
          )


def ejecutar_buscar_videojuego_por_nombre(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar un videojuego por su nombre.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar: "X (Y)" En el cual X es el nombre del videojuego y Y el año de lanzamiento.

    Si no se encuentra el videojuego debe mostrar: "No se encontró ningún juego"

    """
    titulo = "Minecraft"
    rta = vd.buscar_videojuego_por_titulo(e1, e2, e2, e3, e4, titulo)
    print("el juego se lanzó ")


def ejecutar_buscar_videojuego_mas_corto(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar el videojuego más corto.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar:
    "El juego más corto es X y tarda Y horas con Z minutos en completarse"
    En el cual X es el nombre del videojuego, Y las horas y Z los minutos.

    """
    # TODO: Implementar


def ejecutar_calcular_dias_necesarios_para_terminar_videojuego(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular cuántos días se necesitan para terminar un videojuego, dada una disponibilidad temporal diaria.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar: "Terminar X tardaría Y días" En el cual X es el número de horas. En caso
    de que no se ingrese un nombre válido de videojuego debe
    mostrar un mensaje que lo notifique.

    """
    # TODO: Implementar


def ejecutar_mostrar_videojuegos_aptos_para_cierta_edad(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de mostrar cuáles videojuegos
    son aptos para cierta edad.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    """
    # TODO: Implementar


def ejecutar_determinar_puntaje_de_un_videojuego(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular el puntaje de un
    videojuego de acuerdo con el sistema de puntuación.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar el siguiente mensaje:
    "El videojuego X tiene un puntaje de Y", donde X es el nombre del videojuego 
    y Y es el puntaje calculado redondeado a 2 decimales.

    """
    titulo = "Minecraft"
    juego = vd.buscar_videojuego_por_titulo(e1,e2,e3,e4,titulo)
    rta = vd.determinar_puntaje_de_un_videojuego(juego)
    print(rta)
    # TODO: Implementar


def ejecutar_contar_cantidad_de_juegos_de_un_genero(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de contar cuántos videojuegos
    son de un género en particular.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar: "Hay X juego(s) de Y".
    En el cual X es la cantidad de videojuegos y Y el género.

    En caso de que no se ingrese un nombre válido de videojuego debe
    mostrar el mensaje "Ningún juego es de Y", siendo Y el género.

    """
    # TODO: Implementar


def ejecutar_mostrar_promedio_de_rating_de_los_videojuegos_de_un_genero(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de mostrar el promedio de rating
    de los videojuegos de un género en particular.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer videojuego.
    e2 : dict
        Diccionario con la información del segundo videojuego.
    e3 : dict
        Diccionario con la información del tercer videojuego.
    e4 : dict
        Diccionario con la información del cuarto videojuego.

    El programa debe mostrar: "El rating medio de los juegos de X es Y".
    En el cual X es el género y Y el rating medio. En caso de que no
    se ingrese un nombre válido de videojuego debe mostrar el mensaje
    "Ningún juego es de Y", siendo Y el género.

    """
    # TODO: Implementar


def iniciar_aplicacion() -> None:

    videojuego1 = vd.crear_videojuego(
        titulo="Minecraft",
        anio_de_lanzamiento=2011,
        generos="acción, aventura, sandbox",
        rating=9.0,
        es_multijugador=True,
        clasificacion_edad="E10+",
        duracion=9021
    )
    videojuego2 = vd.crear_videojuego(
        titulo="Forza Horizon 5",
        anio_de_lanzamiento=2021,
        generos="carreras, deportes, simulación, vuelo",
        rating=10.0,
        es_multijugador=True,
        clasificacion_edad="E",
        duracion=2047
    )
    videojuego3 = vd.crear_videojuego(
        titulo="Cyberpunk 2077",
        anio_de_lanzamiento=2020,
        generos="fps, rol, ciencia ficción, sandbox",
        rating=9.0,
        es_multijugador=False,
        clasificacion_edad="M",
        duracion=2518
    )
    videojuego4 = vd.crear_videojuego(
        titulo="The Legand of Zelda: Tears of the Kingdon",
        anio_de_lanzamiento=2023,
        generos="tercera persona, acción, aventura, rol, sandbox",
        rating=10.0,
        es_multijugador=False,
        clasificacion_edad="",
        duracion=5753
    )
    ejecutando = True
    while ejecutando:
        print("\nVideojuegos existentes\n" + ("-"*50))
        print("Videojuego 1\n")
        mostrar_videojuego(videojuego1)
        print("-"*50)

        print("Videojuego 2\n")
        mostrar_videojuego(videojuego2)
        print("-"*50)

        print("Videojuego 3\n")
        mostrar_videojuego(videojuego3)
        print("-"*50)

        print("Videojuego 4\n")
        mostrar_videojuego(videojuego4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            videojuego1, videojuego2, videojuego3, videojuego4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar videojuego por nombre")
    print(" 2 - Buscar videojuego más corto")
    print(" 3 - Calcular días necesarios para terminar un videojuego")
    print(" 4 - Mostrar videojuegos aptos para cierta edad")
    print(" 5 - Determinar el puntaje de un videojuego")
    print(" 6 - Contar la cantidad de videojuegos de un género")
    print(" 7 - Mostrar promedio de rating de los videojuegos de un género")
    print(" 8 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_videojuego_por_nombre(
            e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_buscar_videojuego_mas_corto(
            e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_calcular_dias_necesarios_para_terminar_videojuego(
            e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_mostrar_videojuegos_aptos_para_cierta_edad(
            e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_determinar_puntaje_de_un_videojuego(
            e1, e2, e3, e4)
    elif opcion_elegida == "6":
        ejecutar_contar_cantidad_de_juegos_de_un_genero(
            e1, e2, e3, e4)
    elif opcion_elegida == "7":
        ejecutar_mostrar_promedio_de_rating_de_los_videojuegos_de_un_genero(
            e1, e2, e3, e4)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    return continuar_ejecutando


iniciar_aplicacion()


def fibonacci_iterativo(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

n = int(input("Ingrese la cantidad de términos de la secuencia de Fibonacci que desea calcular: "))
fibonacci_sequence = fibonacci_iterativo(n)
print("Secuencia de Fibonacci:", fibonacci_sequence)


