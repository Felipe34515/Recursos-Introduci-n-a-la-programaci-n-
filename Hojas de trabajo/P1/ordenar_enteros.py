#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 07:24:27 2023

@author: mac
"""

def ordenar_enteros( a: int, b: int, c: int) -> str:
    mayor = max(a,b,c);
    menor = min(a,b,c);
    medio = a + b + c - mayor - menor;
    
    return str(mayor) + "," + str(medio) + "," + str(menor);


b = 9
numeros_ordenados = ordenar_enteros( 5, b, 3);
print( numeros_ordenados )