# -*- coding: utf-8 -*-

#TODO: importar el módulo

from random import randint
import modulo as mod


def ejecutar_dar_clase_numero(num: int )->None:
    print(mod.dar_clase_numero(num))
    
def ejecutar_PUM(jugadores:int, X: int)->None:
    mod.jugar_PUM(jugadores, X)
    
def ejecutar_adivinar_numero()->None: 
    """Esta funcion permite ejecutar la función que haya programado para adivinar un numero de 1 a 9. """
    numero = int(input("Ingrese un número del 0 al 9: "))
    print(mod.adivinar_numero(numero))
    

def mostrar_menu()->bool:
    print("1. Dar clase de un número")
    print("2. Jugar PUM")
    print("3. Adivinar un número de 1 a 10")
    print("4. Salir")
    continuar = True
    eleccion  = int(input("Ingrese una opción: "))
    if eleccion == 1:
        num = int(input("Ingrese un número: "))
        ejecutar_dar_clase_numero(num)
    elif eleccion == 2:
        jugadores = int(input("Ingrese el número de jugadores: "))
        X = int(input("Ingrese el número PUM: "))
        ejecutar_PUM(jugadores, X)
    elif eleccion == 3:
        ejecutar_adivinar_numero()
    else:
        continuar = False
    return continuar

def iniciar_aplicacion()->None:
    """
    Esta función mantiene el programa funcionando hasta que el usuario seleccione la opción para salir.
    La función primero debe mostrar el menú de opciones usando la función mostrar_menu().
    A continuación, debe solicitarle al usuario una opción.
    Según lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccionó la opción de Salir, la función debe terminar su ejecución para que el programa pueda terminar.
    Si el usuario seleccionó cualquier otra opción, después de ejecutar la opción seleccionada se debe volver
    a mostrar el menú de opciones y se debe repetir el proceso.
    """
    ejecutando = True
    while ejecutando:
        ejecutando = mostrar_menu()
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

    #TODO: implementar la función 

iniciar_aplicacion()

