"""
Ejercicio nivel 2: Empanadas
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: Cupi2

"""

def crear_empanada(nombre: str, precio: int, vegana: bool, ingredientes: str, toppings: str, rating: float, unidades_vendidas: int, proxima_fecha_entrega: int) -> dict:
    """
    Función para crear una empanada en la plataforma.

    Parámetros
    ----------
    nombre : str
        Nombre de la empanada.
    precio : int
        Precio de la empanada.
    vegana : bool
        Indica si la empanada es vegana.
    ingredientes : str
        Cadena de caracteres separados por comas de los ingredientes de la empanada.
    toppings : str
        Cadena de caracteres separados por comas de los toppings sugeridos para la empanada.
    rating : float
        Rating de la empanada.
    unidades_vendidas : int
        Unidades vendidas de la empanada.
    proxima_fecha_entrega : int
        Próxima fecha de entrega de la empanada en formato YYYYMMDD.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada.

    """
    diccionario ={
        "nombre":nombre,
        "precio":precio,
        "vegana": vegana,
        "ingredientes":ingredientes,
        "toppings": toppings,
        "rating": rating,
        "unidades_vendidas":unidades_vendidas,
        "proxima_fecha_entrega": proxima_fecha_entrega
        }
    return diccionario


def buscar_empanada_por_nombre(e1: dict, e2: dict, e3: dict, e4: dict, nombre: str) -> dict:
    """
    Busca una empanada en la plataforma por su nombre.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    nombre : str
        Nombre de la empanada a buscar.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada buscada. Si no se encuentra la empanada, retorna None.

    """
    respuesta = "No se encontro la empanada"
    if e1["nombre"]==nombre:
        respuesta = e1
    if e2["nombre"]==nombre:
        respuesta = e2
    if e3["nombre"]==nombre:
        respuesta = e3
    if e4["nombre"]==nombre:
        respuesta =  e4
    
    return respuesta


      
  

def buscar_empanada_mas_ganancias(e1: dict, e2: dict, e3: dict, e4: dict) -> dict:
    """
    Busca la empanada que ha generado más ganancias.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada que ha generado más ganancias.

    """
    comparacion = e1["unidades_vendidas"]
    respuesta = e1
    if e2["unidades_vendidas"]> comparacion:
         comparacion = e2["unidades_vendidas"]
         respuesta = e2
    if e3["unidades_vendidas"]> comparacion:
         comparacion = e3["unidades_vendidas"]
         respuesta = e3
    if e4["unidades_vendidas"]> comparacion:
         comparacion = e4["unidades_vendidas"]
         respuesta = e4
    
    return respuesta
        
        
    

def buscar_empanadas_por_ingrediente(e1: dict, e2: dict, e3: dict, e4: dict, ingrediente: str) -> str:
    """
    Busca las empanadas que contengan un ingrediente específico.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    ingrediente : str
        Ingrediente a buscar.

    Retorno
    -------
    str
        Cadena con el nombre de las empanadas que contienen el ingrediente especificado. Si no se encuentra ninguna empanada, retorna None.

    """
    respuesta = ""
    
    if ingrediente in e1["ingredientes"]:
        respuesta += e1["nombre"]
        respuesta += ", "
    if ingrediente in e2["ingredientes"]:
        respuesta += e2["nombre"]
        respuesta+= ", "
    if ingrediente in e3["ingredientes"]:
        respuesta += e3["nombre"]
        respuesta += ", "
    if ingrediente in e4["ingredientes"]:
        respuesta += e4["nombre"]
        respuesta+= ", "
    else:
        return "No se encontró ninguna empanada con " + ingrediente
        
    formato = respuesta[:-2]
    
    return formato
       
    

def buscar_empanada_con_mejor_rating_por_topping(e1: dict, e2: dict, e3: dict, e4: dict, topping: str) -> dict:
    """
    Busca la empanada con mejor rating que contenga un topping específico.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    topping : str
        Topping a buscar.

    Retorno
    -------
    dict
        Diccionario con la información de la empanada con mejor rating que contenga el topping especificado. Si no se encuentra ninguna empanada, retorna None.

    """
    respuesta = None 
    rate = 0
    
    if topping in e1["toppings"] and e1["rating"] > rate:
        respuesta= e1
        rate = e1["rating"]
    if topping in e2["toppings"] and e2["rating"] > rate:
        respuesta= e2
        rate = e2["rating"]
    if topping in e3["toppings"] and e3["rating"] > rate:
        respuesta= e3
        rate = e3["rating"]
    if topping in e4["toppings"] and e4["rating"] > rate:
        respuesta= e4
        rate = e4["rating"]
        
    return respuesta

def calcular_promedio_rating_empanadas(e1: dict, e2: dict, e3: dict, e4: dict, es_vegana: bool) -> float:
    """
    Calcula el promedio de rating de las empanadas veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    es_vegana : bool
        Booleano que representa si se va a calcular el promedio de rating de empanadas veganas o no veganas. (True para veganas, False de lo contrario)

    Retorno
    -------
    float
        Promedio de rating de las empanadas.

    """
    suma = 0
    division = 0
    
    if e1["vegana"] == es_vegana:
        suma += e1["rating"]
        division += 1
    if e2["vegana"] == es_vegana:
        suma += e2["rating"]
        division += 1
    if e3["vegana"] == es_vegana:
        suma += e3["rating"]
        division += 1
    if e4["vegana"] == es_vegana:
        suma += e4["rating"]
        division += 1
    
    if division == 0:
        return 0  
    
    respuesta = suma / division
    return round(respuesta, 2)
    
        
    
def comparar_promedio_rating_empanadas_veganas_no_veganas(e1: dict, e2: dict, e3: dict, e4: dict) -> str:
    """
    Compara el promedio de rating de las empanadas veganas y no veganas.

    Parámetros
    ----------
    e1 : dict
        Diccionario que contiene la información de la primera empanada.
    e2 : dict
        Diccionario que contiene la información de la segunda empanada.
    e3 : dict
        Diccionario que contiene la información de la tercera empanada.
    e4 : dict
        Diccionario que contiene la información de la cuarta empanada.
    
    Retorno
    -------
    str
        Cadena con el mensaje de comparación entre el promedio de rating de las empanadas veganas y no veganas.

    """
    
    vegana = calcular_promedio_rating_empanadas(e1,e2,e3,e4,True)
    no_vegana = calcular_promedio_rating_empanadas(e1, e2, e3, e4, False)
    
    if vegana == no_vegana:
        return "El promedio de rating de las empanadas veganas y no veganas es el mismo"
    elif vegana > no_vegana:
        return "El promedio de rating de las empanadas veganas es mayor que el de las no veganas"
    elif no_vegana > vegana:
        return "El promedio de rating de las empanadas no veganas es mayor que el de las veganas"
        
    
    

def modificar_rating_y_toppings(empanada: dict, nuevo_rating: float, nuevos_toppings: str) -> dict:
    """
    Modifica el rating y los toppings de una empanada

    Parámetros
    ----------
    empanada : dict
        Diccionario de la empanada a modificar
    nuevo_rating : float
        Nuevo rating de la empanada.
    nuevos_toppings : str
        Nuevos toppings de la empanada

    Retorno
    -------
    dict
        El diccionario modificado de la empanada.
    """
    empanada["rating"] = nuevo_rating
    empanada["toppings"] = nuevos_toppings
    return empanada
    


def calcular_tiempo_proxima_fecha_entrega(fecha: int, empanada: dict) -> str:
    """
    Calcula los años, meses y días que faltan entre una fecha y la próxima fecha de entrega de una empanada.

    Parámetros
    ----------
    fecha : int
        Fecha en formato YYYYMMDD.
    empanada : dict
        Diccionario de la empanada.

    Retorno
    -------
    str
        Cadena con el mensaje de los años, meses y días que faltan entre una fecha y la próxima fecha de entrega de una empanada.
    """
    anio_usuario = int(fecha[:4])
    mes_usuario = int(fecha[4:6])
    dia_usuario = int(fecha[6:])

    proxima_fecha_entrega = str(empanada["proxima_fecha_entrega"])
    anio_empanada = int(proxima_fecha_entrega[:4])
    mes_empanada = int(proxima_fecha_entrega[4:6])
    dia_empanada = int(proxima_fecha_entrega[6:])

    if anio_usuario >= anio_empanada:
        if mes_usuario >= mes_empanada:
            if dia_usuario >= dia_empanada:
                return "La entrega de " + str(empanada["nombre"]) +  " ya pasó"
            else:
                r_dia = dia_empanada - dia_usuario
                r_mes = mes_empanada - mes_usuario
                r_anio = anio_empanada - anio_usuario
        else:
            r_dia = dia_empanada - dia_usuario
            r_mes = mes_empanada - mes_usuario
            r_anio = anio_empanada - anio_usuario
    else:
        r_dia = dia_empanada - dia_usuario
        r_mes = mes_empanada - mes_usuario
        r_anio = anio_empanada - anio_usuario

    if r_dia < 0:
        r_mes -= 1
        if r_mes < 0:
            r_anio -= 1
            r_mes += 12
        r_dia += 30  

    return "Faltan " + str(r_anio) + " años, " + str(r_mes) + " meses y " + str(r_dia) + " días entre la fecha " + fecha + " y la próxima fecha de entrega de " + empanada['nombre']

