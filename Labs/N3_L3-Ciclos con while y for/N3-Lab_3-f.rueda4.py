# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 06:36:27 2020

@author: felip
"""
listo = [ 1,2,3,1,2,4,3]
listo2 = [1,2,3]
def buscar_elementos_iguales_seguidos(lista:list)-> int:
    b = 0
    rta = -1
    for i in lista:
        if b < len(lista)-1:
            b += 1
            if lista.count (i) <= 2 and lista[lista.index(i)] == lista[lista.index(i)+1]:
                rta = i
            
    return rta 

def contar_apariciones (lista1:list,lista2:list)->int:
    rta= 0
    c = 0
    for i in lista1:
        while c < len(lista2)-1:
            c += 1
            if i in lista2:
                if lista1[0]==lista2[0] and lista1[1]==lista2[1] and lista1[2]==lista2[2]:
                    rta += 1
                    lista1.remove([lista2])
                else:
                    lista1.remove([lista2])
                    
    return rta 

def viables(ciudades: dict, minimo : int):
    rta = {"viables": [], "inviables": []}

    for ciudad in ciudades:
        if ciudad["poblacion"] < minimo:
            rta["inviables"].append(ciudad)
        else: 
            rta["viables"].append(ciudad)
            
    return rta