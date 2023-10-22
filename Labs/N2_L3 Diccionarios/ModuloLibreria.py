# -*- coding: utf-8 -*-
def crear_libro(nom: str, cod: str,autor: int, adp: int, cant: int, pdv: float, cpu: float)->dict:
    dic_libro = { "nombre": nom, 
                       "codigo": cod,  
                       "autor": autor, 
                       "añoPublicacion": adp,
                       "cantidad": cant,
                       "precio": pdv, 
                       "costoProduccion": cpu}
    return dic_libro

#PROGRAMA PRINCIPAL
libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200 , 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100 , 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien",1937, 50 , 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20 , 26000, 13000)

def mayor_ganancia (libro1: dict, libro2: dict, libro3:dict, libro4:dict)->dict:
    
    ganancia1=libro1["precio"]-libro1["costoProduccion"] 
    ganancia2=libro2["precio"]-libro2["costoProduccion"]
    ganancia3=libro3["precio"]-libro3["costoProduccion"]
    ganancia4=libro4["precio"]-libro4["costoProduccion"]
    maximo=max (ganancia1, ganancia2, ganancia3, ganancia4)
    if ganancia1 == maximo :
        ans= libro1
    elif ganancia2 == maximo :
        ans= libro2
    elif ganancia3 == maximo :
        ans= libro3
    elif ganancia4 == maximo :
        ans= libro4

    return ans

def hacer_pedido(libro1: dict, libro2: dict, libro3:dict, libro4:dict, nombre:str)->bool:
    if libro1["nombre"] == nombre and libro1["cantidad"] <= 50:
        ans=True
    if libro2["nombre"] == nombre and libro2["cantidad"] <= 50:
        ans=True 
    if libro3["nombre"] == nombre and libro3["cantidad"] <= 50:
        ans=True
    if libro2["nombre"] == nombre and libro1["cantidad"] <= 50:
        ans=True
        
    return ans 
def publicacion_antes_anio(libro1: dict, libro2: dict, libro3:dict, libro4:dict, anio:int)->dict:
    libros_antes_anio={}
    if libro1["añoPublicacion"] < anio:
        libros_antes_anio[libro1["nombre"]]=libro1["añoPublicacion"]
    if libro2["añoPublicacion"] < anio:
        libros_antes_anio[libro2["nombre"]]=libro2["añoPublicacion"]
    if libro3["añoPublicacion"] < anio:
        libros_antes_anio[libro3["nombre"]]=libro3["añoPublicacion"]
    if libro4["añoPublicacion"] < anio:
        libros_antes_anio[libro4["nombre"]]=libro4["añoPublicacion"]
    return  libros_antes_anio

def ganancias_ventas_libro(libro1: dict, libro2: dict, libro3:dict, libro4:dict, nombre:str, cant:int)->dict:
    d={}
    ganancia1=(libro1["precio"]-libro1["costoProduccion"]) * cant
    ganancia2=(libro2["precio"]-libro2["costoProduccion"]) * cant
    ganancia3=(libro3["precio"]-libro3["costoProduccion"]) * cant
    ganancia4=(libro4["precio"]-libro4["costoProduccion"]) * cant
    if libro1["nombre"]== nombre:
        d[libro1["nombre"]]=ganancia1
    if libro1["nombre"]== nombre:
        d[libro2["nombre"]]=ganancia2
    if libro3["nombre"]== nombre:
        d[libro3["nombre"]]=ganancia3
    if libro4["nombre"]== nombre:
        d[libro4["nombre"]]=ganancia4
    
    return d
def venta_por_mayor (libro1: dict, libro2: dict, libro3:dict, libro4:dict, nombre:str, cant:int)->dict:
    d={}
    if libro1["nombre"].lower() == nombre.lower():
        if libro1["cantidad"] * 0.25 < cant and cant < libro1["cantidad"] * 0.5:
            d[libro1["precio"] * cant * 0.9] = ("10%")
        elif libro1["cantidad"] * 0.5 < cant and cant < libro1["cantidad"] * 0.75:
            d[libro1["precio"] * cant * 0.8] = ("20%")
        elif libro1["cantidad"] * 0.75 < cant and cant < libro1["cantidad"] :
            d[libro1["precio"] * cant * 0.7] = ("30%")
        else:
            d[libro1["precio"] * cant] = ("Sin descuento")
    elif libro2["nombre"].lower() == nombre.lower():
        if libro2["cantidad"] * 0.25 < cant and cant < libro2["cantidad"] * 0.5:
            d[libro2["precio"] * cant * 0.9] = ("10%")
        elif libro2["cantidad"] * 0.5 < cant and cant < libro2["cantidad"] * 0.75:
            d[libro2["precio"] * cant * 0.8] = ("20%")
        elif libro2["cantidad"] * 0.75 < cant and cant < libro2["cantidad"] :
            d[libro2["precio"] * cant * 0.7] = ("30%")
        else:
            d[libro2["precio"] * cant] = ("Sin descuento")
    elif libro3["nombre"].lower() == nombre.lower():
        if libro3["cantidad"] * 0.25 < cant and cant < libro3["cantidad"] * 0.5:
            d[libro3["precio"] * cant * 0.9] = ("10%")
        elif libro3["cantidad"] * 0.5 < cant and cant < libro3["cantidad"] * 0.75:
            d[libro3["precio"] * cant * 0.8] = ("20%")
        elif libro3["cantidad"] * 0.75 < cant and cant < libro3["cantidad"] :
            d[libro3["precio"] * cant * 0.7] = ("30%")
        else:
            d[libro3["precio"] * cant] = ("Sin descuento")
    elif libro4["nombre"].lower() == nombre.lower():
        if libro4["cantidad"] * 0.25 < cant and cant < libro4["cantidad"] * 0.5:
            d[libro4["precio"] * cant * 0.9] = ("10%")
        elif libro4["cantidad"] * 0.5 < cant and cant < libro4["cantidad"] * 0.75:
            d[libro4["precio"] * cant * 0.8] = ("20%")
        elif libro4["cantidad"] * 0.75 < cant and cant < libro4["cantidad"] :
            d[libro4["precio"] * cant * 0.7] = ("30%")
        else:
            d[libro4["precio"] * cant] = ("Sin descuento")
    return d
            
        
print(venta_por_mayor (libro1, libro2, libro3, libro4, "Harry Potter y la piedra filosofal", 180))
    
    
    
    
    
    