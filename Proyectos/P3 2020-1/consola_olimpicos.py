# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Atletas Olímpicos.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: Cupi2
"""

import modulo_olimpicos

def ejecutar_cargar_atletas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    los atletas y los carga.
    Retorno: list
        La lista de atletas con la información del archivo.
    """
    atletas = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con los atletas: ")
    atletas = modulo_olimpicos.atletas(archivo)
    if len(atletas) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar los atletas olímpicos")
    else:
        print("Se cargaron", len(atletas), "atletas a partir del archivo.")
    return atletas

def ejecutar_funcion_2(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas de un año dado
    """
    
    anio_in = int(input("Ingrese el año de su interés: "))
    print(modulo_olimpicos.funcion_2(atletas,anio_in))
    
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_3(atletas: list) -> None:
    """ Ejecuta la opción de buscar las medallas de un atleta
    en un rango específico de años 
    """ 
    
    nom_interes = input("Ingrese el nombre del atleta de su interés: ")
    anio_inicio = int(input("Ingrese el límite inferior del rango: "))
    anio_final = int(input("Ingrese el límite superior del rango: "))
    print(modulo_olimpicos.funcion_3(atletas,anio_inicio,anio_final,nom_interes))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_4(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas de un país específico
    """
    
    pais_interes = input("Ingrese el nombre del país de su interés: ")
    print(modulo_olimpicos.funcion_4(atletas,pais_interes))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_5(atletas: list) -> None:
    """ Ejecuta la opción de buscar el país con más atletas
    """
    print(modulo_olimpicos.funcion_5(atletas))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_6(atletas: list) -> None:
    """ Ejecuta la opción de buscar los medallistas de un evento dado
    """
    
    evento_in = input("Ingrese el evento de su interés: ")
    print(modulo_olimpicos.funcion_6(atletas,evento_in))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_7(atletas: list) -> None:
    """ Ejecuta la opción de buscar los atletas que han obtenido 
    una cantidad de medallas superior a un número dado
    """
    
    minimo = int(input("Ingrese el mínimo de medallas: "))
    print(modulo_olimpicos.funcion_7(atletas,minimo))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado)

def ejecutar_funcion_8(atletas: list) -> None:
    """ Ejecuta la opción de buscar el atleta con
    más medallas de todos los tiempos
    """
    print(modulo_olimpicos.funcion_8(atletas))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
    
def ejecutar_funcion_9(atletas: list) -> None:
    """ Ejecuta la opción de buscar el país con mejor
    desempeño en un evento en específico
    """
    
    evento = input("Ingrese el evento de su interés: ")
    print(modulo_olimpicos.funcion_9(atletas,evento))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
    
def ejecutar_funcion_10 (atletas: list) -> None:
    """ Ejecuta la opción de buscar el atleta más todoterreno
    de todos los tiempos
    """
    print(modulo_olimpicos.funcion_10(atletas))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
    
def ejecutar_funcion_11(atletas: list) -> None:
    """ Ejecuta la opción de buscar los medallistas de un país
    y género específicos
    """
    
    pais = input("Ingrese el país de su interés: ")
    genero = input("Ingrese el género de su interés (m o f): ")
    print(modulo_olimpicos.funcion_11(atletas,pais,genero))
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_funcion_12(atletas: list) -> None:
    """ Ejecuta la opción de calcular el porcentaje de medallistas 
    """
    rta = float(modulo_olimpicos.funcion_12(atletas))
    print(rta)

def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de atletas")
    print("2. Consultar los atletas de un año dado")
    print("3. Consultar las medallas de un atleta en un periodo")
    print("4. Consultar los atletas de un país dado")
    print("5. Consultar el país con más medallistas")
    print("6. Consultar todos los medallistas de un evento dado")
    print("7. Consultar los atletas más populares")
    print("8. Consultar el atleta estrella de todos los tiempos")
    print("9. Consultar el mejor país en un evento")
    print("10. Consultar el atleta Todoterreno")
    print("11. Consultar los medallistas por nación y género")
    print("12. Consultar el porcentaje de atletas que son medallistas")
    print("13. Salir de la aplicación")
	
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    atletas = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            atletas=ejecutar_cargar_atletas()
        elif opcion_seleccionada == 2:
            ejecutar_funcion_2(atletas)
        elif opcion_seleccionada == 3:
            ejecutar_funcion_3(atletas)
        elif opcion_seleccionada == 4:
            ejecutar_funcion_4(atletas)
        elif opcion_seleccionada == 5:
            ejecutar_funcion_5(atletas)
        elif opcion_seleccionada == 6:
            ejecutar_funcion_6(atletas)
        elif opcion_seleccionada == 7:
            ejecutar_funcion_7(atletas)
        elif opcion_seleccionada == 8:
            ejecutar_funcion_8(atletas)
        elif opcion_seleccionada == 9:
            ejecutar_funcion_9(atletas)
        elif opcion_seleccionada == 10:
            ejecutar_funcion_10(atletas)
        elif opcion_seleccionada == 11:
            ejecutar_funcion_11(atletas)
        elif opcion_seleccionada == 12:
            ejecutar_funcion_12(atletas)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()