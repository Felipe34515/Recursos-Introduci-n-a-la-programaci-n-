def calcular_costo_empanada (precio_carne: int, precio_papa: int, precio_aceite: int)-> float:
    #Calcula cuánto costaría hacer una empanada a partir del costo de 
    # cada uno de sus ingredientes
    rta = ((2.5*precio_carne) + (3 * precio_papa) + (precio_aceite))/50
    return rta

def calcular_tiempo_coccion_lote_empanadas (tiempo_por_empanada: int, cantidad_empanadas: int)-> int:
    # Calcula cuánto tiempo tardarían en cocinarse una cantidad 
    # determinada de empanadas a partir del tiempo que tarda una única 
    # empanada.
    rta = tiempo_por_empanada * cantidad_empanadas
    return rta

def calcular_rentabilidad(precio_venta: float, precio_carne: int, precio_papa: int, precio_aceite: int)->float:
    # Calcula cuánto se está ganando por cada empanada vendida a partir 
    # de su costo de fabricación y su precio de venta.
    costo_empanada = calcular_costo_empanada(precio_carne, precio_papa, precio_aceite)
    rta = precio_venta  - costo_empanada
    return rta

def calcular_cantidad_empanadas_meta (arriendo: float, numero_empleados: int, precio_venta: float, 
                                      precio_carne: int, precio_papa: int, precio_aceite: int)->int:
    # Calcula cuántas empanadas se deben hacer para lograr la meta 
    # establecida, esto según el precio de venta de las empanadas y 
    # teniendo en cuenta el costo de fabricación
    rentabilidad = calcular_rentabilidad(precio_venta, precio_carne, precio_papa, precio_aceite)
    rta = ( arriendo + (numero_empleados * 45000) ) / rentabilidad
    return int(rta)

def calcular_precio_venta_promocion (precio_venta_unidad : float, cantidad_empanadas : int)-> str:
    # Dar un mensaje con el precio de venta total en promoción de una 
    # cantidad de empanadas suponiendo que la promoción es “pague 3 y 
    # lleve 5”.
    rta = ((cantidad_empanadas//5)* 3 +(cantidad_empanadas%5)) * precio_venta_unidad
    rta = "El precio de venta en promoción de " + str(cantidad_empanadas) + " empanadas sería de " + str(rta) 
    return rta

