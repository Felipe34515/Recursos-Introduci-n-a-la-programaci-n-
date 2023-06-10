# -*- coding: utf-8 -*-

def cargar_tablero(ruta_archivo: str)->list:
    """
    Esta función carga la información un tablero del juego de la vida 
    a partir de un archivo CSV.
    La primera fila del archivo contiene las dimensiones del tablero filas, columnas.
    Parámetros:
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con el tablero de juego
    """
    archivo = open(ruta_archivo)
    dimensiones = archivo.readline().split(",")
    filas = int(dimensiones[0])
    columnas = int(dimensiones[1])
    print("Filas:", filas)
    print("Columnas:", columnas)
    
    tablero = []
    for i in range(0,filas):
        tablero.append([0] * columnas)

    linea = archivo.readline()
    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,columnas):
            tablero[i][j] = int(datos[j])
        i += 1 
        linea = archivo.readline()

    archivo.close()
    return tablero

def cuantas_vecinas_vivas(tablero:list, fila:int, columna:int)->int:
    """
    Esta función cuenta cuántas células vivas vecinas tiene la célula de 
    la casilla ubicada en la posición fil, col del tablero recibido por parámetro.
    Parámetros:
        tablero (list): la matriz que contiene el tablero de juego
        fil (int): fila de la casilla que se va a explorar
        col (int): columna de la casilla que se va a explorar
    Retorno: int
        La cantidad de casillas vecinas de la casilla fil,col que contienen células vivas.
    """
    #TODO: Completar la función según la documentación                

    cel_vivas= 0
    n=len(tablero)
    m=len(tablero[0])
    for i in range(max(0,fila-1),min(n,fila+2)):
        for j in range(max(0,columna),min(m,columna+2)):
            if i!=fila or j!=columna:
                cel_vivas+=tablero[i][j]
    
    return cel_vivas

def regla_nacimiento(tablero:list, fila:int, columna:int)->bool:
    """
    Esta función verifica si la célula de la casilla ubicada en la posición 
    fil, col del tablero recibido por parámetro cumple con la regla de nacimiento.
    Parámetros:
        tablero (list): la matriz que contiene el tablero de juego
        fil (int): fila de la casilla que se va a explorar
        col (int): columna de la casilla que se va a explorar
    Retorno: bool
        True si la casilla cumple con la regla de nacimiento. False de lo contrario.
    """
    #TODO: Completar la función según la documentación          
    return cuantas_vecinas_vivas(tablero, fila, columna)==3

def regla_supervivencia(tablero:list, fil:int, col:int)->bool:
    """
    Esta función verifica si la célula de la casilla ubicada en la posición 
    fil, col del tablero recibido por parámetro cumple con la regla de supervivencia.
    Parámetros:
        tablero (list): la matriz que contiene el tablero de juego
        fil (int): fila de la casilla que se va a explorar
        col (int): columna de la casilla que se va a explorar
    Retorno: bool
        True si la casilla cumple con la regla de supervivencia. False de lo contrario.
    """
    n = cuantas_vecinas_vivas(tablero, fil, col)
    if (tablero[fil][col] == 1 and (n == 2 or n == 3)):
        return True
    else:
        return False

def realizar_jugada(tablero:list)-> list:
    """
    Esta función simula una jugada (aplicando las reglas del juego de la vida sobre 
    cada casilla del tablero) y retorna el tablero de juego modificado tras la jugada
    Parámetros:
        tablero (list): la matriz que contiene el tablero de juego
    Retorno: list
        El tablero de juego modificado desupués de realizar la jugada.
    """
    filas = len(tablero)
    columnas = len(tablero[0])

    nuevo_tablero = []

    for i in range(0,filas):
        nuevo_tablero.append([0] * columnas)

    #TODO: Completar la función según la documentación        
    n=len(tablero)
    m=len(tablero[0])
    for i in range(0,n):
        for j in range(0,m):
            if tablero[i][j]==1 and regla_supervivencia(tablero, i, j):
                nuevo_tablero[i][j]=1
            if tablero[i][j]==0 and regla_nacimiento(tablero, i, j):
                nuevo_tablero[i][j]=1
    return nuevo_tablero


            
    
