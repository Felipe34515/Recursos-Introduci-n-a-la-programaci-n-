"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
 
    pelicula = {
        'nombre': nombre,
        'genero': genero,
        'duracion': duracion,
        'anio': anio,
        'clasificacion': clasificacion,
        'hora': hora,
        'dia': dia
    }
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """

    if(nombre_pelicula == p1["nombre"]):
        return p1
   
    if(nombre_pelicula == p2["nombre"]):
        return p2
   
    if(nombre_pelicula == p3["nombre"]):
        return p3
  
    if(nombre_pelicula == p4["nombre"]):
        return p4
  
    if(nombre_pelicula == p5["nombre"]):
        return p5
    else:
        return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    dic = {}
    temp = p1["duracion"]
    if(p2["duracion"] > temp ):
        temp = p2["duracion"]
        dic = p2
    if(p3["duracion"] > temp ):
        temp = p3["duracion"]
        dic = p3
    if(p4["duracion"] > temp ):
        temp =  p4["duracion"]
        dic = p4
    if(p5["duracion"] > temp ):
        temp = p5["duracion"]
        dic = p5
    if(temp == p1["duracion"]):
        dic = p1

    return dic

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """

    Total = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    respuesta = float(Total / 5) 
    return str(int(respuesta//60))+ "h" +str(int(respuesta%60))

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    estrenos = ""
    if(p1["anio"] > anio):
        if estrenos != "":
            estrenos += ", "
        estrenos =  estrenos + str(p1["anio"]) + " "+ p1["nombre"]
    
    if(p2["anio"] > anio):
        if estrenos != "":
            estrenos += ", "
        estrenos = estrenos + str(p2["anio"]) + " "+ p2["nombre"] 
    
    if(p3["anio"] > anio):
        if estrenos != "":
            estrenos += ", "
        estrenos = estrenos + str(p3["anio"]) + " "+p3["nombre"] 
    
    if(p4["anio"] > anio):
        if estrenos != "":
            estrenos += ", "
        estrenos =  estrenos + str(p4["anio"]) + " "+ p4["nombre"] 
    
    if(p5["anio"] > anio):
        if estrenos != "":
            estrenos += ", "
        estrenos = estrenos + str(p5["anio"]) + " " +p5["nombre"]

    if(estrenos == ""):
        estrenos = "Ninguna"

    return str(estrenos)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    temp = 0
    if(p1["clasificacion"] == "18+"):
        temp += 1

    if(p2["clasificacion"] == "18+"):
        temp += 1
    
    if(p3["clasificacion"] == "18+"):
        temp += 1
    
    if(p4["clasificacion"] == "18+"):
        temp += 1
    
    if(p5["clasificacion"] == "18+"):
        temp += 1
    
    return temp

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """

    respuesta=True 

    minutos1=p1["duracion"]%60
    minutos2=p2["duracion"]%60
    minutos3=p3["duracion"]%60
    minutos4=p4["duracion"]%60
    minutos5=p5["duracion"]%60
    
    hora1= (p1["duracion"]//60) *100
    hora2= (p2["duracion"]//60) *100
    hora3= (p3["duracion"]//60) *100
    hora4= (p4["duracion"]//60) *100
    hora5= (p5["duracion"]//60) *100
    
    hora_dura1= hora1+minutos1
    hora_dura2= hora2+minutos2
    hora_dura3= hora3+minutos3
    hora_dura4= hora4+minutos4
    hora_dura5= hora5+minutos5
    
    
    if p1["dia"]==nuevo_dia and (nueva_hora>=p1["hora"] and nueva_hora<=hora_dura1+p1["hora"]):
        respuesta=False
    if p2["dia"]==nuevo_dia and (nueva_hora>=p2["hora"] and nueva_hora<=hora_dura2+p2["hora"]):
        respuesta=False
    if p3["dia"]==nuevo_dia and (nueva_hora>=p3["hora"] and nueva_hora<=hora_dura3+p3["hora"]):
        respuesta=False
    if p4["dia"]==nuevo_dia and (nueva_hora>=p4["hora"] and nueva_hora<=hora_dura4+p4["hora"]):
        respuesta=False
    if p5["dia"]==nuevo_dia and (nueva_hora>=p5["hora"] and nueva_hora<=hora_dura5+p5["hora"]):
        respuesta=False
    else:
        if control_horario:
            if peli is not None and "Documental" in peli["genero"] and nueva_hora>2200:
                respuesta=False
            if peli is not None and "Drama" in peli["genero"] and nuevo_dia=="Viernes":
                respuesta=False
            if nuevo_dia=="Lunes" or nuevo_dia=="Martes" or nuevo_dia=="Miércoles" or nuevo_dia=="Jueves" or nuevo_dia=="Viernes":
                if nueva_hora>=2300 or nueva_hora<=600:
                    respuesta=False
        
                    
    if peli is not None and respuesta==True:
        peli["dia"]=nuevo_dia
        peli["hora"]=nueva_hora
        
    if peli==None:
        respuesta=False
        
    
    return respuesta
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    if(edad_invitado >=18):
        return True
    else:
        if(peli["genero"] == "Suspenso, Terror"  and edad_invitado < 15):
            return False
        if((peli["genero"] == "Familiar, Ciencia-Ficción"or peli["genero"] == "Familiar, Comedia") and edad_invitado <= 10):
            return True
        if(autorizacion_padres == True or peli["genero"] == "Documental, Suspenso"):
            return True
        else:
            return False








