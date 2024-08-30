
def calcular_costo_queso_fresco(costo_l: float, cantidad_l: float, costo_ad: float)-> float:
    costo_queso= (costo_l*cantidad_l)+costo_ad
    return round(costo_queso,2)


def calcular_cantidad_queso(cantidad_l: float)-> float:
    cantidad_queso= (1.03*cantidad_l)/10 
    return round(cantidad_queso,2)


def calcular_dia_maduracion( cantidad_l: float, temperatura: float, humedad: float)-> int:
    cantidad_queso= calcular_cantidad_queso(cantidad_l)
    dias_m= 5+0.1*((humedad*cantidad_queso)/temperatura)
    return round(dias_m)


def calcular_costo_queso_madurado( costo_l: float, cantidad_l: float, costo_ad: float,costo_al: float, humedad: float, temperatura: float)-> float:
    queso_f=  calcular_costo_queso_fresco(costo_l, cantidad_l, costo_ad)
    maduracion= calcular_dia_maduracion( cantidad_l, temperatura, humedad)
    queso_m= queso_f+(costo_al *maduracion)
    return round( queso_m,2)


def calcular_tamano(angulo_corte: float)->float:
    tamano= angulo_corte/360
    return round(tamano,2)


def calcular_costo_porcion_madurado( costo_l: float, cantidad_l: float, costo_al: float, costo_ad: float, temperatura: float, humedad: float, angulo_corte: float)-> float:
    queso_m= calcular_costo_queso_madurado(costo_l, cantidad_l, costo_ad,costo_al, humedad, temperatura)
    tamano= calcular_tamano(angulo_corte)
    costo_pm= queso_m*tamano
    return round( costo_pm,2)


    