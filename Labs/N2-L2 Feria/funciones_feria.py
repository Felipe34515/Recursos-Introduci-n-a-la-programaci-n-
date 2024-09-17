# -*- coding: utf-8 -*-
import math as math
import random as rand

# Juego 1: Buscar la bolita

def buscar_bolita(posicion_inicial: int, posicion_apuesta: int)->bool:
    """ Esta función ubica la bolita en la posición inicial indicada, hace 3 intercambios aleatorios y
        finalmente informa si la bolita quedó en la posición por la que apostó el jugador.
    Parámetros:
        posicion_inicial (int): es el número del vaso en el que va a quedar la bolita inicialmente (1, 2 o 3)
        posicion_apuesta (int): es el número del vaso en el que el jugador supone que va a quedar la bolita (1, 2 o 3)    
    Retorno:
        Retorna True si la bolita quedó en la posición apostada y False en caso contrario.
    """
    
    #TODO:completar la función para simular los 3 movimientos aleatorios entre los vasos
    #Use las variables booleanas vaso1, vaso2 y vaso3 para indicar respectivamente si el vaso 1 contiene la bolita (True) o
    #no la contiene (False), si el vaso 2 contiene la bolita (True) o no la contiene (False) y si el vaso 3 contiene 
    #la bolita (True) o no la contiene (False)
    
    mov1, mov2, mov3 = rand.randint(1,3), rand.randint(1,3), rand.randint(1,3)


    #TODO: Inicialización de las variables vaso1, vaso2 y vaso3 de acuerdo a la posición inicial de la bolita dada por el usuario
    if posicion_apuesta == 1:
        vaso1, vaso2, vaso3 = True, False, False
    elif posicion_apuesta == 2:
        vaso1, vaso2, vaso3 = False, True, False
    elif posicion_apuesta == 1:
        vaso1, vaso2, vaso3 = False, False, True

    #TODO simular el primer intercambio aleatorio de vasos
    if mov1 == 1:
        if vaso1 == True:
            vaso1 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso1 = True
    elif mov1 == 2:
        if vaso3 == True:
            vaso3 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso3 = True
    elif mov1 == 3:
        if vaso3 == True:
            vaso3 = False
            vaso1 = True
        elif vaso1 == False:
            vaso1 = False
            vaso3 = True        

    #TODO: simular el segundo y tercer intercambio aleatorio
    
    if mov2 == 1:
        if vaso1 == True:
            vaso1 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso1 = True
    elif mov2 == 2:
        if vaso3 == True:
            vaso3 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso3 = True
    elif mov2 == 3:
        if vaso3 == True:
            vaso3 = False
            vaso1 = True
        elif vaso1 == False:
            vaso1 = False
            vaso3 = True  
            
    if mov3 == 1:
        if vaso1 == True:
            vaso1 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso1 = True
    elif mov3 == 2:
        if vaso3 == True:
            vaso3 = False
            vaso2 = True
        elif vaso2 == False:
            vaso2 = False
            vaso3 = True
    elif mov3 == 3:
        if vaso3 == True:
            vaso3 = False
            vaso1 = True
        elif vaso1 == False:
            vaso1 = False
            vaso3 = True  
            

    #TODO Llamar a la función es_ganador para determinar si el jugador ganó o perdió y dejar el resultado en la variable gano
    gano = es_ganador(posicion_apuesta, vaso1, vaso2, vaso3)

    return gano


def es_ganador(posicion_apuesta, vaso1: bool, vaso2: bool, vaso3: bool)->bool:
    """ Esta función indica si el jugador ganó dependiendo de su apuesta y dependiendo del contenido de los vasos.
    Parámetros:
        posicion_apuesta (int): es la posición en la que el jugador supone que va a estar la bolita (1, 2 o 3)
        vaso1 (bool): es True si la bolita se encuentra en el vaso 1 y False de lo contrario.
        vaso2 (bool): es True si la bolita se encuentra en el vaso 2 y False de lo contrario.
        vaso3 (bool): es True si la bolita se encuentra en el vaso 3 y False de lo contrario.
    Retorno:
        Retorna True si el jugador ganó su apuesta y False en caso contrario.
    """
    # TODO: completar la implementación de la función. 
    if (posicion_apuesta == vaso1 or posicion_apuesta == vaso2 or posicion_apuesta == vaso3):
        return True
    else:
        return False


# Juego 2: Tiro al blanco

def tiro_al_blanco(velocidad_inicial: float, angulo_alfa: float, angulo_beta: float)->int:
    """ Esta función calcula los puntos obtenidos por un jugador dados los datos de su lanzamiento.
    La mesa se encuentra ubicada a 7 metros del lugar de lanzamiento.
    El blanco tiene 4 zonas de 10, 20, 30 y 40 cms de diámetro, que dan 50, 20, 10 y 5 puntos respectivamente.
    Parámetros:
        velocidad_inicial (float): la velocidad inicial en kilómetros/horaa la que sale la bola lanzada.
        angulo_alfa (float): el ángulo en grados al que sale la bola con respecto a la horizontal.
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.
    Retorno:
        La cantidad de puntos obtenidos por el jugador
    """
    # TODO: completar la implementación de la función. 
    velocidad_inicial = velocidad_inicial * (1 + (rand.randint(1,10) /100))
    angulo_alfa = angulo_alfa * (1 + (rand.randint(1,5) /100))
    angulo_beta = angulo_beta * (1 + (rand.randint(1,5) /100))
    distancia_tiro = calcular_distancia_tiro(velocidad_inicial, angulo_alfa, angulo_beta)
    x = calcular_x_tiro(distancia_tiro, 7, angulo_beta)
    y = calcular_y_tiro(distancia_tiro, 7, angulo_beta)
    puntos = calcular_puntos(x, y, 10, 20, 30, 40)
    return puntos


def calcular_distancia_tiro(velocidad_inicial: float, angulo_alfa: float, angulo_beta: float)->float:
    """ Calcula la distancia horizontal recorrida por la bola desde el lanzamiento hasta que caiga sobre la mesa.
    Parámetros:
        velocidad_inicial (float): la velocidad inicial en metros/segundo a la que sale la bola lanzada.
        angulo_alfa (float): el ángulo en grados al que sale la bola con respecto a la horizontal.
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.
    Retorno:
        La distancia en metros del lanzamiento
    """
    # TODO: completar la implementación de la función. 

    Vx = velocidad_inicial * math.cos(math.radians(angulo_alfa))
    t = calcular_tiempo_tiro(velocidad_inicial)
    pos_inicial = 0
    rta = pos_inicial + Vx * t
    
    return rta


def calcular_tiempo_tiro(velocidad_vertical_inicial: float)->float:
    """ Calcula el tiempo que le toma a la bola caer sobre la mesa.
    Parámetros:
        velocidad_vertical_inicial (float): la componente vertical de la velocidad inicial en metros/segundo 
        a la que sale la bola lanzada.
    Retorno:
        La cantidad de segundos que le toma a la bola llegar a la mesa
    """
    # TODO: completar la implementación de la función. 
    Vy = velocidad_vertical_inicial * math.sin(math.radians(0.5)) 
    t = Vy / 9.8
    return t


def calcular_x_tiro(distancia_tiro: float, distancia_mesa: int, angulo_beta: float)->float:
    """ Calcula la coordenada X del lugar donde cayó la bola, teniendo el centro de la mesa como la coordenada 0,0.
    Parámetros:
        distancia_tiro (float): la distancia en metros recorrida por la bola durante el lanzamiento
        distancia_mesa (float): la distancia en metros entre el lugar del lanzamiento y el centro de la mesa
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.        
    Retorno:
        La coordenada x del lanzamiento, en centímetros
    """
    # TODO: completar la implementación de la función. 
	# Cuando haya completado la función con su verdadero valor de retorno, borre la siguiente línea.
    rta = distancia_tiro * math.cos(math.radians(angulo_beta))
    return rta


def calcular_y_tiro(distancia_tiro: float, distancia_mesa: int, angulo_beta: float)->float:
    """ Calcula la coordenada Y del lugar donde cayó la bola, teniendo el centro de la mesa como la coordenada 0,0.
    Parámetros:
        distancia_tiro (float): la distancia en metros recorrida por la bola durante el lanzamiento
        distancia_mesa (float): la distancia en metros entre el lugar del lanzamiento y el centro de la mesa
        angulo_beta (float): el ángulo en grados al que sale la bola con respecto a la línea recta entre el punto de lanzamiento y el centro del blanco.        
    Retorno:
        La coordenada y del lanzamiento, en centímetros
    """
    # TODO: completar la implementación de la función. 
    rta = distancia_tiro * math.sin(math.radians(angulo_beta))
    return rta


def calcular_puntos(x: float, y: float, radio1: int, radio2: int, radio3: int, radio4: int)->int:
    """ Calcula la cantidad de puntos que ganó el usuario dada la posición donde cayó la bola.
    La coordenada 0,0 corresponde al centro de la mesa.
    Parametros:
        x (float): la coordenada x del lanzamiento, en centímetros
        y (float): la coordenada y del lanzamiento, en centímetros
        radio1 (int): el radio en centímetros de la zona 1 de la mesa (la zona más interna) que da 50 puntos
        radio2 (int): el radio en centímetros de la zona 2 de la mesa que da 20 puntos
        radio3 (int): el radio en centímetros de la zona 3 de la mesa que da 10 puntos
        radio4 (int): el radio en centímetros de la zona 4 de la mesa (la zona más externa) que da 5 puntos
    Retorno:
        La cantidad de puntos obtenidos por el jugador
    """
    # TODO: completar la implementación de la función. 
    rta = 0
    if -radio1 <= x and x <= radio1 and -radio1 <= y and y <= radio1:
        rta = 50
    elif -radio2 <= x and x <= radio2 and -radio2 <= y and y <= radio2:
        rta = 20
    elif -radio3 <= x and x <= radio3 and -radio3 <= y and y <= radio3:
        rta = 10
    elif -radio4 <= x and x <= radio4 and -radio4 <= y and y <= radio4:
        rta = 5
     
    return rta

