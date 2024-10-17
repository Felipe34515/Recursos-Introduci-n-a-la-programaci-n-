

def jugar_PUM(jugadores: int, numero: int)-> None:
    """
    Simula el juego del PUM.
    Parámetros:
        jugadores: cantidad de jugadores
        numero: número escogido para el PUM 
    Retorno:
        No retorna nada ya que imprime por pantalla el desarrollo del juego
    """
    jugador = 1
    while jugador < 10:
        if jugador%jugadores != 0:
            if  jugador%numero == 0:
                print(jugador%jugadores, "Pum...")
            else: 
                print(jugador%jugadores, jugador)
        else:
            if  jugador%numero == 0:
                print(jugadores, "Pum...")
            else: 
                print(jugadores, jugador)
        jugador +=1
        
        
def fibonacci (n:int)->int:
    """
    Calcula el n-ésimo término de la sucesión de Fibonacci.
    Parámetros:
        n: número de términos de la sucesión
    Retorno:
        int: n-ésimo término de la sucesión
    """
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

