#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 04:31:55 2023

@author: mac
"""

def saludar_repetidas_veces(nombre: str, veces:int ) -> str:
    """
    

    Parameters
    ----------
    nombre : str
        DESCRIPTION.
    veces : int
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.

    """
    cantidad_o = veces;
    cantidad_a = veces//2;
    
    return "H" + ( "o" * cantidad_o ) + "l" + ( "a" * cantidad_a ) + " " + nombre;


nombre = input("Como se llama la persona que se debe saludar: ");
veces = int( input("Escriba la cantidad de veces que se va repetir la 'o': ") );
print( saludar_repetidas_veces(nombre, veces) );