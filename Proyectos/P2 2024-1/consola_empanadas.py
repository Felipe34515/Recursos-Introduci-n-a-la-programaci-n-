"""
Ejercicio nivel 2: empanadas
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

import empanadas as em


def mostrar_empanada(empanada: dict) -> None:

    nombre = empanada["nombre"] 
    precio = empanada["precio"]
    vegana = empanada["vegana"]
    ingredientes = empanada["ingredientes"]
    toppings = empanada["toppings"]
    rating = empanada["rating"]
    unidades_vendidas = empanada["unidades_vendidas"]
    proxima_fecha_entrega = empanada["proxima_fecha_entrega"]

    print("Nombre: " + nombre +
            "\nPrecio: " + str(precio) +
            "\n¿Es Vegana?: " + str(vegana) +
            "\nIngredientes: " + str(ingredientes) +
            "\nToppings recomendados: " + str(toppings) +
            "\nRating: " + str(rating) +
            "\nUnidades vendidas: " + str(unidades_vendidas) +
            "\nProxima fecha entrega: " + str(proxima_fecha_entrega))
    

def ejecutar_buscar_empanada_por_nombre(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar un empanada por su nombre.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar: "X cuesta Y y tiene Z", donde X es el nombre de la empanada, Y es el precio y Z son los ingredientes
    
    Si no se encuentra la empanada debe mostrar: "No se encontró la empanada"


    """
    nombre = input("Ingrese el nombre de la empanada: ")
    respuesta = em.buscar_empanada_por_nombre(e1, e2, e3, e4, nombre)
    print(respuesta["nombre"] + " cuesta " + str(respuesta["precio"]) + " y tiene " + respuesta["ingredientes"])
    
    

def ejecutar_buscar_empanada_mas_ganancias(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar el empanada con más ganancias.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar un mensaje de la forma: "La empanada con más ganancias es X con ganancias de Y", donde X es el nombre de la empanada y Y es el valor de las ganancias.

    """
    dicc = em.buscar_empanada_mas_ganancias(e1, e2, e3, e4)
    respuesta = dicc["precio"] * dicc["unidades_vendidas"]
    print("La empanada con mas ganancias es " + dicc["nombre"] + " con ganancias de: " + str(respuesta))
    
    


def ejecutar_buscar_empanadas_por_ingrediente(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar empanadas por ingrediente.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar un mensaje de la forma "Las empanadas que contienen X son Y", donde X es el ingrediente y Y son los nombres de las empanadas que contienen el ingrediente. 
    Si no se encuentra ninguna empanada debe mostrar: "No se encontró ninguna empanada con X", donde X es el ingrediente.

    """
    ingrediente = input(str("Ingrese un ingrediente especifico que contenga la empanada: "))
    respuesta = em.buscar_empanadas_por_ingrediente(e1, e2, e3, e4, ingrediente)
    print("Las empanadas que contienen " + ingrediente + " son: "+ respuesta )
    

def ejecutar_buscar_empanada_con_mejor_rating_por_topping(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar empanada con mejor rating por topping.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar un mensaje de la forma "La empanada con mejor rating con X es Y con Z de rating", donde X es el topping, Y es el nombre de la empanada y Z es el rating de la empanada.
    Si no se encuentra ninguna empanada debe mostrar: "No se encontró ninguna empanada con X", donde X es el topping recomendado.

    """
    topping = input(str("Ingrese el topping: "))
    respuesta = em.buscar_empanada_con_mejor_rating_por_topping(e1, e2, e3, e4, topping)
    print("La empanada con " + topping + " es " +  str(respuesta["nombre"]) + " con " + str(respuesta["rating"]) + " de rating.")
    
    
    
    
def ejecutar_calcular_promedio_rating_empanadas(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular el promedio de rating de las empanadas veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada
    es_vegana : bool
        Booleano que indica si se calculará el rating de las empanadas veganas o no veganas 

    El programa debe mostrar el promedio de rating de las empanadas con el formato 
    "El promedio de rating de las empanadas es X", donde X es el promedio de rating de las empanadas redondeado a 2 decimales.

    """
    boleano = None
    usuario = input("Ingrese 1, si desea calcular el rating de las empanadas veganas, y 2 en caso de las emmpanadas no veganas: ")
    if usuario == "1":
        boleano = True
        
    if usuario == "2":
        boleano = False
    
    respuesta = em.calcular_promedio_rating_empanadas(e1, e2, e3, e4, boleano)
    print(respuesta)

    
    
    

def ejecutar_comparar_rating_empanadas_veganas_y_no_veganas(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de comparar el promedio de rating de las empanadas veganas y no veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar el mensaje 
    "El promedio de rating de las empanadas veganas es mayor que el de las no veganas" si el promedio de rating de las empanadas veganas es mayor que el promedio de rating de las empanadas no veganas.
    "El promedio de rating de las empanadas no veganas es mayor que el de las veganas" si el promedio de rating de las empanadas no veganas es mayor que el promedio de rating de las empanadas veganas.
    "El promedio de rating de las empanadas veganas y no veganas es el mismo" si el promedio de rating de las empanadas veganas es igual al promedio de rating de las empanadas no veganas.

    """
    respuesta = em.comparar_promedio_rating_empanadas_veganas_no_veganas(e1, e2, e3, e4)
    print(respuesta)
    
    


def ejecutar_modificar_rating_y_toppings(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de modificar el rating y los toppings de una empanada.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar un mensaje de la forma: "Se ha modificado exitosamente la empanada"

    Si no se encuentra la empanada debe mostrar: "No se encontró la empanada"
    """
    nombre = input("Ingrese el nombre de la empanada: ")
    empanada = em.buscar_empanada_por_nombre(e1, e2, e3, e4, nombre)
    if empanada != "No se encontro la empanada":
        nuevo_rating = float(input("Ingrese el nuevo rating (números entre 0 y 5): " ))
        if 0 <= nuevo_rating <= 5:
            nuevos_toppings = input("Ingrese los nuevos toppings: ")
            funcion = em.modificar_rating_y_toppings(empanada, nuevo_rating, nuevos_toppings)
            print("Se ha modificado exitosamente la empanada")
            return funcion
        else:
            print("El rating no está dentro del rango que se pide.")
    else:
        print(empanada)

        
        
        
    


def ejecutar_calcular_tiempo_proxima_fecha_entrega(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular los años, meses y dias para la proxima fecha de entrega de una empanada.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información de la primera empanada
    e2 : dict
        Diccionario con la información de la segunda empanada
    e3 : dict
        Diccionario con la información de la tercera empanada
    e4 : dict
        Diccionario con la información de la cuarta empanada

    El programa debe mostrar los años, meses y dias para la proxima fecha de entrega de una empanada con el formato
    "Faltan X años, Y meses y Z días entre la fecha A y la próxima fecha de entrega de B", donde X, Y y Z son los años, meses y dias para la proxima fecha de entrega, A es la fecha ingresada por el usuario y B es la proxima fecha de entrega de la empanada.
    
    Si la fecha ingresada por el usuario es mayor a la proxima fecha de entrega de la empanada debe mostrar: "La entrega de X ya pasó", donde X es el nombre de la empanada.

    Si no se encuentra la empanada debe mostrar: "No se encontró la empanada"
    """
    nombre = input("Ingrese el nombre de la empanada: ")
    busqueda = em.buscar_empanada_por_nombre(e1, e2, e3, e4, nombre)
    if busqueda != "No se encontró la empanada":
        fecha = input("Ingrese la fecha en formato YYYYMMDD: ")
        respuesta = em.calcular_tiempo_proxima_fecha_entrega(fecha, busqueda)
        print(respuesta)
    else:
        print( busqueda)


def iniciar_aplicacion() -> None:
    empanada1 = em.crear_empanada(
        nombre="Empanada Carnívora Multicarne",
        precio=2700, 
        vegana=False,
        ingredientes="Carne de res, Carne de cerdo, Pollo desmenuzado, Huevo Cebolla, Pimiento",
        toppings="Salsa de chimichurri, Ají",
        rating=4.6,
        unidades_vendidas=160,
        proxima_fecha_entrega=20240306
    )

    empanada2 = em.crear_empanada(
        nombre="Empanada de los Sabores del Huerto",
        precio=3000,
        vegana=True,
        ingredientes="Champiñones, Cebolla, Pimiento, Tomate, Aceitunas",
        toppings="Salsa de ajo, Salsa de mostaza",
        rating=4.3,
        unidades_vendidas=120,
        proxima_fecha_entrega=20240309
    )
    empanada3 = em.crear_empanada(
        nombre="Empanada de Pollo",
        precio=2550,
        vegana=False,
        ingredientes="Pollo desmenuzado, Cebolla, Pimiento, Tomate",
        toppings="Ají, Salsa de ajo",
        rating=4.5,
        unidades_vendidas=200,
        proxima_fecha_entrega=20240208
    )

    empanada4 = em.crear_empanada(
        nombre="Empanada Vegana de Lentejas",
        precio=3200,
        vegana=True,
        ingredientes="Lentejas, Cebolla, Pimiento, Tomate",
        toppings="Guacamole, Salsa de mostaza",
        rating=4.2,
        unidades_vendidas=100,
        proxima_fecha_entrega=20240518
    )
    ejecutando = True
    while ejecutando:
        print("\nEmpanadas existentes\n" + ("-"*50))
        print("Empanada 1\n")
        mostrar_empanada(empanada1)
        print("-"*50)

        print("Empanada 2\n")
        mostrar_empanada(empanada2)
        print("-"*50)

        print("Empanada 3\n")
        mostrar_empanada(empanada3)
        print("-"*50)

        print("Empanada 4\n")
        mostrar_empanada(empanada4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            empanada1, empanada2, empanada3, empanada4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar empanada por nombre")
    print(" 2 - Buscar empanada con más ganancias")
    print(" 3 - Buscar empanadas por ingrediente")
    print(" 4 - Buscar empanada con mejor rating por topping")
    print(" 5 - Calcular promedio de rating de las empanadas (veganas o no veganas)")
    print(" 6 - Comparar promedio de rating de las empanadas veganas y no veganas")
    print(" 7 - Modificar rating y toppings de una empanada")
    print(" 8 - Calcular los años, meses y dias para la proxima fecha de entrega de una empanada")
    print(" 9 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_empanada_por_nombre(
            e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_buscar_empanada_mas_ganancias(
            e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_buscar_empanadas_por_ingrediente(
            e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_buscar_empanada_con_mejor_rating_por_topping(
            e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_calcular_promedio_rating_empanadas(
            e1, e2, e3, e4)
    elif opcion_elegida == "6":
        ejecutar_comparar_rating_empanadas_veganas_y_no_veganas(
            e1, e2, e3, e4)
    elif opcion_elegida == "7":
        ejecutar_modificar_rating_y_toppings(
            e1, e2, e3, e4)
    elif opcion_elegida == "8":
        ejecutar_calcular_tiempo_proxima_fecha_entrega(
            e1, e2, e3, e4)
    elif opcion_elegida == "9":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    return continuar_ejecutando


iniciar_aplicacion()
