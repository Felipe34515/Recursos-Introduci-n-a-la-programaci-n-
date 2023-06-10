# -*- coding: utf-8 -*-


import libreria_juego as lib_juego


def ejecutar_cargar_tablero()->list:
    archivo = input("Por favor ingrese el nombre del archivo con el tablero de juego que desea cargar: ")
    tablero = lib_juego.cargar_tablero(archivo)
    return tablero

def ejecutar_jugada(tablero:list)->list:
    tablero = lib_juego.realizar_jugada(tablero)
    pintar_tablero(tablero)
    return tablero

def pintar_tablero(tablero:list)->None:
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            if tablero[i][j] == 0:
                print(".",end="")
            else:
                print("*",end="")
        print()
                
def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Cargar tablero")
    print("2. Imprimir tablero")
    print("3. Jugar")
    print("4. Salir")


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
    continuar = True
    tablero = []
    while continuar:
        mostrar_menu()
        opcion = int(input("Por favor seleccione una opción del menú: "))
        if opcion == 1:
            tablero = ejecutar_cargar_tablero()
        elif opcion == 2:
            pintar_tablero(tablero)
        elif opcion == 3:
            tablero = ejecutar_jugada(tablero)
        elif opcion == 4:
            continuar = False
        else:
            print("Por favor seleccione una de las opciones del menú.")


#PROGRAMA PRINCIPAL
iniciar_aplicacion()