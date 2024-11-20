# -*- coding: utf-8 -*-
"""
Aplicación de Restaurantes

@author: Cupi2
"""

import restaurantes as r


# Funciones para facilitar la impresión (ver ejemplo de uso en la función: ejecutar_estandarizar_direcciones())
def mostrar_restaurante(restaurante: dict) -> None:
    """
    Muestra toda la información de un restaurante.
    
    Parámetros:
        restaurante (dict): Información del restaurante.
    """
    delivery = "No"
    if restaurante["delivery"] == True:
        delivery = "Sí"
    
    print((
        "Nombre: {}\n"
        "Categoría: {}\n"
        "Dirección: {}\n"
        "Ciudad: {}\n"
        "Estado: {}\n"
        "Rating: {} ({} reseñas)\n"
        "Costo: {}\n"
        "Servicio a domicilio: {}\n"
        "Latitud: {}\n"
        "Longitud: {}\n"
    ).format(
        restaurante["name"], restaurante["category"], restaurante["address"],
        restaurante["city"], restaurante["state"], restaurante["rating"],
        restaurante["review_count"], restaurante["price"], delivery,
        restaurante["latitude"], restaurante["longitude"]
    ))

def mostrar_restaurantes(restaurantes: list) -> None:
    """
    Muestra la lista de restaurantes.
    
    Parámetros:
        restaurantes (list): Lista de restaurantes.
    """
    for restaurante in restaurantes:
        mostrar_restaurante(restaurante)
####

        
#Funciones a implementar:
def ejecutar_buscar_restaurantes_en_area(estados: dict) -> None:
    """
    Ejecuta la opción de buscar restaurantes dentro de un área definida por el usuario.

    Parámetros:
        estados (dict): Diccionario de estados.

    Si no se encuentran restaurantes en el área definida, se debe mostrar el siguiente mensaje:
    "No se encontraron restaurantes en el área definida."

    En cualquier otro caso, se muestran los restaurantes encontrados (usando la función: mostrar_restaurantes(...))
    y la cantidad total en el siguiente formato:
    "Se encontraron {número} restaurantes en el área definida."

    """
    # TODO1 - Solución:
    latitud_min = float(input("Ingrese la latitud mínima: "))
    latitud_max = float(input("Ingrese la latitud máxima: "))
    longitud_min = float(input("Ingrese la longitud mínima: "))
    longitud_max = float(input("Ingrese la longitud máxima: "))

    restaurantes_encontrados = r.buscar_restaurantes_en_area(estados, latitud_min, latitud_max, longitud_min, longitud_max)
    
    if restaurantes_encontrados != []:
        mostrar_restaurantes(restaurantes_encontrados)
        print("Se encontraron {} restaurantes en el área definida.".format(len(restaurantes_encontrados)))
    else:
        print("No se encontraron restaurantes en el área definida.")


def ejecutar_buscar_restaurante_mas_sucursales(estados: dict) -> None:
    """
    Ejecuta la opción de buscar el restaurante con más sucursales en un estado específico.

    Parámetros:
        estados (dict): Diccionario de estados.

    Si no se encuentran restaurantes en el estado, se debe mostrar el siguiente mensaje:
    "No se encontraron restaurantes en el estado {estado}."

    En cualquier otro caso, se muestra el nombre del restaurante con más sucursales y la cantidad de sucursales en el siguiente formato:
    "El restaurante con más sucursales en {estado} es '{nombre_restaurante}' con {numero_sucursales} sucursales."
    """
    # TODO2 - Solución:
    estado = input("Ingrese el estado donde desea buscar: ")
    resultado = r.buscar_restaurante_mas_sucursales(estados, estado)
    if resultado["nombre_restaurante"] != "":
        print("El restaurante con más sucursales en {} es '{}' con {} sucursales.".format(estado, resultado["nombre_restaurante"], resultado["numero_sucursales"]))
    else:
        print("No se encontraron restaurantes en el estado {}.".format(estado))

        
def ejecutar_estandarizar_direcciones(estados: dict) -> None:
    """
    Ejecuta la opción de estandarizar las direcciones de los restaurantes.

    Parámetros:
        estados (dict): Diccionario de estados.

    A modo de ejemplo, se muestra el primer restaurante de California (usando la función: mostrar_restaurante(...)) 
    antes y después de estandarizar las direcciones.
    """
    if "California" in estados and estados["California"] != []:
        print("Primer restaurante de California antes de estandarizar su dirección:")
        mostrar_restaurante(estados["California"][0])

        print("\nEstandarizando direcciones...")
        r.estandarizar_direcciones(estados)

        print("\nPrimer restaurante de California después de estandarizar su dirección:")
        mostrar_restaurante(estados["California"][0])


def ejecutar_buscar_restaurantes_palindromos(estados: dict) -> None:
    """
    Ejecuta la opción de buscar todos los restaurantes cuyos nombres son palíndromos.

    Parámetros:
        estados (dict): Diccionario de estados.
    
    Si no se encuentran restaurantes con nombres palíndromos, se debe mostrar el siguiente mensaje:
    "No se encontraron restaurantes cuyos nombres sean palíndromos."

    En cualquier otro caso, imprime todos los restaurantes (usando la función: mostrar_restaurantes(...)) con nombres palíndromos encontrados.
    """
    # TODO3 - Solución:
    restaurantes_palindromos = r.buscar_restaurantes_palindromos(estados)
    
    if restaurantes_palindromos != []:
        print("Restaurantes cuyos nombres son palíndromos:")
        mostrar_restaurantes(restaurantes_palindromos)
    else:
        print("No se encontraron restaurantes cuyos nombres sean palíndromos.")


def ejecutar_buscar_restaurante_cercano(estados: dict) -> None:
    """
    Ejecuta la opción de buscar el restaurante más cercano.

    Parámetros:
        estados (dict): Diccionario de estados.

    Imprime el restaurante que es más cercano al punto de referencia (usando la función: mostrar_restaurante(...)).
    """
    # TODO4 - Solución:
    latitud_ref = float(input("Ingrese la latitud del punto de referencia: "))
    longitud_ref = float(input("Ingrese la longitud del punto de referencia: "))

    restaurante_cercano = r.buscar_restaurante_cercano(estados, latitud_ref, longitud_ref)
    mostrar_restaurante(restaurante_cercano)


def ejecutar_buscar_restaurante_preferido(estados: dict) -> None:
    """
    Ejecuta la opción de buscar el primer restaurante en un área determinada que cumpla con preferencias de precio, número de reviews y rating.

    Parámetros:
        estados (dict): Diccionario de estados.
    
    Si no se encuentra un restaurante que cumpla con las preferencias del usuario, se debe mostrar el siguiente mensaje:
    "No se encontró un restaurante que cumpla con las preferencias."

    En cualquier otro caso, imprime el restaurante preferido encontrado (usando la función: mostrar_restaurante(...)).
    """
    # TODO5 - Solución:
    latitud_min = float(input("Ingrese la latitud mínima: "))
    latitud_max = float(input("Ingrese la latitud máxima: "))
    longitud_min = float(input("Ingrese la longitud mínima: "))
    longitud_max = float(input("Ingrese la longitud máxima: "))
    precio_maximo = str(input("Ingrese el precio máximo que está dispuesto a pagar ($, $$, $$$ o $$$$): "))
    minimo_reviews = int(input("Ingrese el número mínimo de reviews que debe tener el restaurante: "))
    rating_minimo = float(input("Ingrese el rating mínimo que debe tener el restaurante: "))

    resultado = r.buscar_restaurante_preferido(estados, latitud_min, latitud_max, longitud_min, longitud_max, precio_maximo, minimo_reviews, rating_minimo)
    
    if resultado is not None:
        mostrar_restaurante(resultado)
    else:
        print("No se encontró un restaurante que cumpla con las preferencias.")


# Función principal:
def iniciar_aplicacion() -> None:
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si su archivo se llama restaurantes.csv: ")
    if archivo == "":
        archivo = "restaurantes.csv"
    estados = r.cargar_restaurantes(archivo)
    print("\nDatos cargados exitosamente.\n")
    ejecutando = True
    print("#" * 50)
    print("¡Bienvenido a la aplicación de restaurantes!")
    print("#" * 50)
    while ejecutando == True:
        ejecutando = mostrar_menu_aplicacion(estados)
        if ejecutando == True:
            input("Presione Enter para continuar...")


# Función para mostrar el menú de la aplicación:
def mostrar_menu_aplicacion(estados: dict) -> bool:
    print("\nMenú de opciones:")
    print("1. Buscar restaurantes en un área.")
    print("2. Buscar restaurante con más sucursales en un estado.")
    print("3. Estandarizar direcciones.")
    print("4. Buscar restaurantes con nombres palíndromos.")
    print("5. Buscar restaurante más cercano.")
    print("6. Buscar restaurante preferido.")
    print("7. Salir")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_restaurantes_en_area(estados)
    elif opcion_elegida == "2":
        ejecutar_buscar_restaurante_mas_sucursales(estados)
    elif opcion_elegida == "3":
        ejecutar_estandarizar_direcciones(estados)
    elif opcion_elegida == "4":
        ejecutar_buscar_restaurantes_palindromos(estados)
    elif opcion_elegida == "5":
        ejecutar_buscar_restaurante_cercano(estados)
    elif opcion_elegida == "6":
        ejecutar_buscar_restaurante_preferido(estados)
    elif opcion_elegida == "7":
        print("¡Gracias por usar la aplicación de restaurantes!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Inténtelo de nuevo.")

    return continuar_ejecutando


# Punto de entrada de la aplicación
if __name__ == "__main__":
    iniciar_aplicacion()