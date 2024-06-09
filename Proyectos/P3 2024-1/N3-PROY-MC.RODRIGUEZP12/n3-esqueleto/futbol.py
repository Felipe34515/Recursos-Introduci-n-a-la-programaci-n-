def carga_de_datos(archivo: str) -> dict:
    """
    esta función carga los datos del archivo CSV que llega por parámetro y los convierte en un diccionario
    Parameters
    ----------
    archivo : str
        nombre del archivo ingresado por el usuario.

    Returns
    -------
    dict
        diccionario en el cual las llaves son los paises sede y los valores 
        son una lista de diccionarios con la infortmación de los partidos jugados en ese país.

    """
    
    paises = {}
    archivo = open(archivo, "r",encoding="utf-8")
    archivo.readline()
    for linea in archivo:
        info = linea.strip().split(",")
        nombre_pais = info[7]
        partido = {
            "fecha": info[0],
            "equipo_local": info[1],
            "equipo_visitante": info[2],
            "goles_local": int(info[3]),
            "goles_visitante": int(info[4]),
            "torneo": info[5],
            "ciudad": info[6]
        }
        if nombre_pais not in paises:
            paises[nombre_pais] = []
        paises[nombre_pais].append(partido)
    archivo.close()
    return paises


def buscar_partido (paises:dict, pais_sede:str, ciudad:str, fecha:str)-> dict:
    """
    Esta función con un fecha, sede y ciudad que entran por parámetro
    busca el partidoq ue cumpla con esas condiciones

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él.
    pais_sede : str
        nombre del pais sede en el cual se va a buscar el partido.
    ciudad : str
        ciudad en el pais sede en dpnde se jugó el partido.
    fecha : str
        fecha en la cual se jugó el partido a buscar.

    Returns
    -------
    dict
        la funcion devuelve el diccionario del partido buscado.

    """
    partidos = paises[pais_sede]
    i = 0
    n = len(partidos)
    comprobante = True
    respuesta = None
    while i < n and comprobante:
        partido = partidos [i]
        if partido ["ciudad"] == ciudad and partido["fecha"]==fecha:
            respuesta = partido
            comprobante = False
        i+=1
    return respuesta

def buscar_mayor_goleada(paises: dict) -> dict:
    """
    esta funcion compara la mayor diferencia en cantidad de goles de todos los partidos del diccionario

    Parameters
    ----------
    paises : diccionario con los datos de los paises y partidos jugados en él.
    
    Returns
    -------
    dict
        diccionario del partido con la mayor goleada.

    """
    partido_goleada = None
    for llaves in paises.keys():
        mayor_diferencia = 0
        partidos = paises[llaves]
        for partidos in paises.values():
            for partido in partidos:
                diferencia = abs(partido["goles_local"] - partido["goles_visitante"])
                if diferencia >= 3 and diferencia > mayor_diferencia:
                    mayor_diferencia = diferencia
                    partido_goleada = partido
    return partido_goleada

def buscar_primera_goleada(paises: dict, sede: str) -> dict:
    """
    esta función busca la primera goleada en un partido jugado en el pais sede

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..
    sede : str
        nombre del país sede en el cual se va a buscar la primera goleada.

    Returns
    -------
    dict
        diccionario del partido con la priera goleada.

    """
    if sede in paises:
        pais = paises[sede]
    else:
        pais = []

    goleada = None
    i = 0
    while i < len(pais) and not goleada:
        partido = pais[i]
        diferencia = abs(partido["goles_local"] - partido["goles_visitante"])
        if diferencia >= 3:
            goleada = partido
        i += 1
    return goleada

def calcular_desempeno(paises: dict, sede: str, pais: str) -> dict:
    """
    

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..
    sede : str
        pais sede en el cual se va a calcular el desempeñp.
    pais : str
        nombre de la selección de la cual se va a calcular el desempeño en el pais sede.

    Returns
    -------
    dict
        diccionario con los elementos del desempeño calculado, partidos ganados, jugados,
        perdidos, empatados, goles a favor y en contra.

    """
    desempeno = {}
    partidos = paises[sede]
    partidos_jugados = 0
    partidos_ganados = 0
    partidos_perdidos = 0
    partidos_empatados = 0
    goles_favor = 0
    goles_contra = 0

    for partido in partidos:
        if pais == partido["equipo_local"]:
            partidos_jugados += 1
            goles_favor += partido["goles_local"]
            goles_contra += partido["goles_visitante"]
            if partido["goles_local"] > partido["goles_visitante"]:
                partidos_ganados += 1
            elif partido["goles_local"] < partido["goles_visitante"]:
                partidos_perdidos += 1
            else:
                partidos_empatados += 1
        elif pais == partido["equipo_visitante"]:
            partidos_jugados += 1
            goles_favor += partido["goles_visitante"]
            goles_contra += partido["goles_local"]
            if partido["goles_visitante"] > partido["goles_local"]:
                partidos_ganados += 1
            elif partido["goles_visitante"] < partido["goles_local"]:
                partidos_perdidos += 1
            else:
                partidos_empatados += 1

    desempeno = {
        "partidos_jugados": partidos_jugados,
        "partidos_ganados": partidos_ganados,
        "partidos_perdidos": partidos_perdidos,
        "partidos_empatados": partidos_empatados,
        "goles_favor": goles_favor,
        "goles_contra": goles_contra
    }

    return desempeno

                
def buscar_pais_de_la_suerte (paises:dict, seleccion:str)-> str:
    """
    esta funcion revisa el desempeño de la selección dada y analiza
    en qué país sede ha teniso un mejor desempeño

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..
    seleccion : str
        nombre de la selección en al cual se va a buscar el pais de la suerte.

    Returns
    -------
    str
        nombre del pais de la suerte de la selección dada.

    """
    max_partidos_ganados=0
    pais_suerte = None
    for sede in paises.keys():
        partidos = paises[sede]
        partidos_ganados = 0
        goles_favor = 0
        goles_contra=0
        for partido in partidos:
            if seleccion == partido["equipo_local"]:
                goles_favor += partido["goles_local"]
                goles_contra += partido["goles_visitante"]
                if partido["goles_local"] > partido["goles_visitante"]:
                    partidos_ganados += 1
            elif seleccion == partido["equipo_visitante"]:
                goles_favor += partido["goles_visitante"]
                goles_contra += partido["goles_local"]
                if partido["goles_visitante"] > partido["goles_local"]:
                    partidos_ganados += 1
        if partidos_ganados > max_partidos_ganados:
            max_partidos_ganados = partidos_ganados
            pais_suerte = sede

    return pais_suerte

def buscar_partidos_por_torneo_y_decada(paises: dict, torneo: str, año: int)->list:
    """
    esta función busca los partidos que se jugaron de cierto torneo dado
    en la década tomando como inicio el año dado

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él.
    torneo : str
        nombre del torneo en el cual se van a buscar los partidos.
    año : int
        año inicio de la década a buscar partidos.

    Returns
    -------
    list
        lista de los diccionarios de los partidos jugados del torneo y década dada.

    """
    año_base = año
    año_decada = año +10
    salida=[]
    respuesta = None
    for sede in paises.keys():
        partidos = paises[sede]
        for partido in partidos:
            año_partido = int(partido["fecha"][:4])
            if partido["torneo"] == torneo and año_base <= año_partido <= año_decada:
                salida.append(partido)
    if salida:
        respuesta= salida
    return respuesta

def buscar_partido_mas_jugado(paises: dict) -> dict:
    """
    esta funcion busca el partido que más se ha jugado,
    o sea el partido que más se repita en el que los contrincantes sean el mismo

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..

    Returns
    -------
    dict
        diccionario con el nombre de los contrincantes y la cantidad de veces que se ha jugado ese partido.

    """
    partidos_cantidad = {}
    for partidos in paises.values():
        for partido in partidos:
            paises_en_contra = [partido["equipo_visitante"], partido["equipo_local"]]
            paises_en_contra.sort()
            partido_vs = paises_en_contra[0] + " vs " + paises_en_contra[1]
            if partido_vs in partidos_cantidad:
                partidos_cantidad[partido_vs] += 1
            else:
                partidos_cantidad[partido_vs] = 1
    cantidad_partidos = 0
    for partido in partidos_cantidad:
        cantidad = partidos_cantidad[partido]
        if cantidad > cantidad_partidos:
            partido_mas_jugado = partido
            cantidad_partidos = cantidad
    salida = {"partido": partido_mas_jugado, "cantidad": cantidad_partidos}

    return salida

def buscar_paises_sin_jugar (paises:dict)-> str:
    """
    esta funcion busca las selecciones que nunca han jugado en su pais

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..

    Returns
    -------
    str
        cadena de texto separada por comad con el nombre de las selecciones
        que jamás han u¿jugado en su país.

    """
    paises_sin_jugar = ""
    respuesta = None
    for sede in paises.keys():
        jugado = False
        partidos = paises[sede]
        for partido in partidos: 
            if sede == partido["equipo_local"] or sede == partido ["equipo_visitante"]:
                jugado = True
        if not jugado: 
            paises_sin_jugar += sede + ","
    if paises_sin_jugar != "":
        respuesta = paises_sin_jugar
    return respuesta
                
def buscar_ganador_por_puntos(paises: dict, torneo: str, año: str) -> str:
    """
    esta funcion calcula los puntos y con ello busca el ganador
    de un torneo dado en el año dado.

    Parameters
    ----------
    paises : dict
        diccionario con los datos de los paises y partidos jugados en él..
    torneo : str
        nombre del torneo en el que se va a buscar un ganador.
    año : str
        año en el que se va a buscar el torneo.

    Returns
    -------
    str
        nombre de la selección ganadora del torneo 
        (cuando hay empate en puntos da cualquiera de los ganadores).

    """
    puntos= {}
    for sede in paises.keys():
        partidos= paises[sede]
        for partido in partidos:
            if partido["torneo"]==torneo and partido["fecha"][:4] == año:
                equipo_local =partido["equipo_local"]
                if equipo_local not in puntos:
                    puntos[equipo_local] = 0
                if partido["goles_local"] > partido["goles_visitante"]:
                    puntos[equipo_local]+= 3
                elif partido["goles_local"]== partido["goles_visitante"]:
                    puntos[equipo_local] += 1
                    
                equipo_visitante =partido["equipo_visitante"]
                if equipo_visitante not in puntos:
                    puntos[equipo_visitante]= 0
                if partido["goles_visitante"]> partido["goles_local"]:
                    puntos[equipo_visitante] += 3
                elif partido["goles_visitante"] ==partido["goles_local"]:
                    puntos[equipo_visitante] += 1
            
    puntaje_mas_alto = -1
    for puntoss in puntos.values():
        if puntoss > puntaje_mas_alto:
            puntaje_mas_alto = puntoss

    ganador = None
    for pais in puntos:
        puntaje = puntos[pais]
        if puntaje == puntaje_mas_alto:
            ganador = pais

    return ganador
  
    
        
                 
             
    
        