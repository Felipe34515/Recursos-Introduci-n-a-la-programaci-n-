# -*- coding: utf-8 -*-


import random 


def dar_clase_numero(numero:int)->str:
    """ Esta función permite saber si un numero 
    entero es un rey par, un noble par, guerrero par y rebelde impar. 
    Parámetros:
        numero(int): numero ingresado por el usuario.
    Retorno:
        Str: Informando al usuario con la clase a la cual pertenece el número.
    """
    par = False #Guerrero par
    SumPar =False #Noble par
    sum = 0
    rta = "Rebelde impar"
    if numero % 2 == 0:
        par = True
    contador = 0
    digitos = len(str(numero))
    while contador <= digitos:
        sum += numero%10
        numero = numero//10
        contador += 1
        
    if sum % 2 == 0:
        SumPar = True 
    if SumPar and par:
        rta = ("Rey par")
    elif SumPar and (not par):
        rta = ("Noble par")
    elif (not SumPar) and  par:
        rta = ("Guerrero par")
    return rta

def jugar_PUM(jugadores: int, numero: int)-> None:
    """
    Simula el juego del PUM.
    Parámetros:
        jugadores: cantidad de jugadores
        numero: número escogido para el PUM 
    Retorno:
        No retorna nada ya que imprime por pantalla el desarrollo del juego
    """
    jugador = 1
    while jugador < 10:
        if jugador%jugadores != 0:
            if  jugador%numero == 0:
                print(jugador%jugadores, "Pum...")
            else: 
                print(jugador%jugadores, jugador)
        else:
            if  jugador%numero == 0:
                print(jugadores, "Pum...")
            else: 
                print(jugadores, jugador)
        jugador +=1
        
def adivinar_numero(numero:int)->str:
    """ Esta función permite adivinar un numero entre 1 y 9.
    Parámetros:
        numero(int): numero ingresado por el usuario.
    Retorno:
        Str: Informando al usuario cuando adivino el número.
        Recuerde que el programa continua funcionando hasta el usuario 
        adivina el número escogido por el sistema (este número es 
        dado mendiante la funcion random.randint)
    """
    elegido = random.randint(0,9)
    Busqueda = True
    while Busqueda:
        if elegido == numero:
            Busqueda = False
            print("Felicitaciones, encontró el número " + str(elegido))
        else:
            numero = int(input("No ha encontrado el numero, ingrese otro número del 0 al 9: "))
    