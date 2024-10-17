# -*- coding: utf-8 -*-

def es_palindroma(cadena: str)->bool:
    """
    Indica si la cadena recibida por parámetro es palíndroma
    Parámetros:
        cadena: cadena a analizar
    Retorno:
        True si la cadena es palíndroma, false de lo contrario
    """
    rta = True
    for i in range(len(cadena)//2):
        if cadena[i] != cadena[len(cadena)-i-1]:
            rta = False
            
    return rta

def letra_mas_comun(cadena: str)->str:
    """
    Retorna la letra más común en la cadena recibida por parámetro.
    Parámetros:
        cadena: cadena a analizar
    Retorno:
        letra encontrada más veces en la cadena
    """
    diccionario = {}  
    maximo = 0
    letra = ""  
    for i in cadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
        if diccionario[i] > maximo:
            maximo = diccionario[i]
            letra = i
            
    return letra
    

def invertir_cadena(cadena: str)->str:

    """
    Invierte la cadena recibida por parámetro
    Parámetros:
        cadena: cadena a invertir
    Retorno:
        cadena invertida
    """
    inversa = ""
    recorrido = len(cadena)-1
    while recorrido >= 0:
        inversa += cadena[cadena[recorrido]]
         
        recorrido -= 1
    return inversa

