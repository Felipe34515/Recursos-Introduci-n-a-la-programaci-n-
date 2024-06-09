"""
Proyecto nivel 3: Partidos de fútbol.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import futbol as f


def ejecutar_cargar_datos() -> dict:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de los partidos de fútbol y carga los datos en un diccionario.
    Retorno: dict
        El diccionario cuyas llaves son los países y los valores son listas de diccionarios con los datos de los partidos.
    """
    paises = None
    
    archivo = str(input(
        "Por favor ingrese el nombre del archivo CSV con los partidos de fútbol: "))
    
    paises = f.carga_de_datos(archivo)
    if len(paises) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los datos.")
    else:
        print("Se cargaron los siguientes paises en donde se disputaron partidos a partir del archivo.")
        for pais in paises.keys():
            print(pais)
    return paises

def ejecutar_buscar_partido(paises: dict):
    """Función que ejecuta la opción de buscar un partido.
    Se debe imprimir el diccionario de datos del partido. En caso de que no se encuentre el partido se debe 
    imprimir el mensaje "No se encontró el partido."
    
    """
    pais_sede = input("Ingrese el pais sede del partido a buscar: ")
    ciudad = input("Ingrese la ciudad del partido a buscar: ")
    fecha = input("Ingrese la fecha del partido a buscar: ")
    buscar_partido = f.buscar_partido(paises, pais_sede, ciudad, fecha)
    if buscar_partido == None:
        print("No se encontr� el partido.")
    else:
        print(buscar_partido)

def ejecutar_buscar_mayor_goleada(paises: dict):
    """Funci�n que ejecuta la opci�n de buscar el partido con la mayor diferencia de goles.
    Se debe imprimir resultado con el formato: "El partido con la mayor diferencia de goles fue: {equipo_local} vs {equipo_visitante} que qued� {goles_local} - {goles_visitante}"
    En caso de que no se encuentre el partido se debe imprimir el mensaje "No se encontr� el partido."
    """
    partido = f.buscar_mayor_goleada(paises)
    if partido:
        print(f"El partido con la mayor diferencia de goles fue: {partido['equipo_local']} vs {partido['equipo_visitante']} que qued� {partido['goles_local']} - {partido['goles_visitante']}")
    else:
        print("No se encontr� el partido.")


def ejecutar_buscar_primera_goleada(paises: dict):
    """Función que ejecuta la opción de buscar la goleada.
    Se debe imprimir el resultado con el formato: "La primera goleada en {pais} fue un partido que quedó {goles_local}-{goles_visitante} entre {equipo_local} y {equipo_visitante} en {fecha}"
    En caso de que no se encuentre el partido se debe imprimir el mensaje "En el {pais} no han habido goleadas"
    """
    sede = str(input("Digite el pa�s en el cual quiere buscar la primera goleada: "))
    resultado = f.buscar_primera_goleada(paises, sede)
    if resultado:
        print(f"La primera goleada en {sede} fue un partido que qued� {resultado['goles_local']}-{resultado['goles_visitante']} entre {resultado['equipo_local']} y {resultado['equipo_visitante']} en {resultado['fecha']}")
    else:
        print(f"En el {sede} no han habido goleadas")  

def ejecutar_calcular_desempeno(paises: dict):
    """Función que ejecuta la opción de calcular el desempeño de un país.
    Se debe imprimir el diccionario que retorna la función del módulo que implementa la funcionalidad.
    En caso de que no se encuentre el país se debe imprimir el mensaje "No se encontró el país."
    """
    sede = input("Digite el nombre del pa�s sede: ")
    pais = input ("Ingrese el nombre la selecci�n del pa�s a buscar: ")
    resultado = f.calcular_desempeno(paises, sede, pais)
    if resultado:
        print(resultado)
    else:
        print("No se encontr� el pa�s")

def ejecutar_buscar_pais_de_la_suerte(paises: dict):
    """Función que ejecuta la opción de buscar el país de la suerte.
    Se debe imprimir el resultado con el formato: "El país de la suerte de {pais} fue {pais_suerte}"
    En caso de que no se encuentre el país se debe imprimir el mensaje "No se encontró el país."
    """
    seleccion = input("Ingrese el nombre de la selecci�n a analizar: ")
    resultado = f.buscar_pais_de_la_suerte(paises, seleccion)
    if resultado:
        print(f"El pa�s de la suerte de {seleccion} fue {resultado}")
    else:
        print ("No se encontr� el pa�s.")

def ejecutar_buscar_partidos_por_torneo_y_decada(paises: dict):
    """Función que ejecuta la opción de buscar los partidos de un torneo en una década.
    Se deben imprimir los partidos del torneo con el formato 'Los partidos del torneo {torneo} en la década de {decada} fueron: ' y luego cada partido en una línea.
    """
    torneo = input("Ingrese el nombre del torneo a buscar: ")
    anio = int(input("Ingrese el anio en el que comienza la d�cada a buscar: "))
    resultado = f.buscar_partidos_por_torneo_y_decada(paises, torneo, anio)
    
    if resultado:
        print(f"Los partidos del torneo {torneo} en la d�cada de {anio} a {anio+10} fueron:")
        for partido in resultado:
            print(partido)
    else:
        print("No se encontraron partidos en esa d�cada o torneo.")

def ejecutar_buscar_partido_mas_jugado(paises: dict):
    """Función que ejecuta la opción de buscar el partido más jugado.
    Se debe imprimir el resultado con el formato: "El partido más jugado fue {partido} que se jugó {cantidad} veces"
    """
    resultado = f.buscar_partido_mas_jugado(paises)
    partido = resultado["partido"]
    cantidad = resultado["cantidad"]
    print(f"El partido m�s jugado fue {partido} que se jug� {cantidad} veces")
    
def ejecutar_buscar_paises_sin_jugar(paises: dict):
    """Función que ejecuta la opción de buscar los países que no jugaron.
    Se debe imprimir los países con el formato 'Los países en los que se jugaron partidos pero cuyas selecciones no jugaron fueron: ' y luego cada país en una línea.
    """
    resultado = f.buscar_paises_sin_jugar(paises)
    if resultado:
        print("Los pa�ses en los que se jugaron partidos pero cuyas selecciones no jugaron fueron: ")
        for pais in resultado.split(","):
            print(pais)
    else:
        print("No se encontraron pa�ses con esa condici�n.")
    
def ejecutar_buscar_ganador_por_puntos(paises: dict):
    """Función que ejecuta la opción de buscar el ganador de un torneo por puntos.
    Se debe imprimir el resultado con el formato: "El ganador del torneo {torneo} en el año {anio} fue {ganador}"
    """
    torneo = input("Digfite el nombre del torneo a buscar: ")
    anio = input("Digite el anio en el que desea buscar: ")
    resultado = f.buscar_ganador_por_puntos(paises, torneo, anio)
    if resultado:
        print(f"El ganador del torneo {torneo} en el anio {anio} fue {resultado}.")
    else:
        print("No se encontr� el torneo o el torneo no se jug� en el anio ingresado.")

def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de partidos de fútbol.")
    print("2. Buscar un partido dado un país, una ciudad y una fecha.")
    print("3. Buscar el partido con la mayor goleada")
    print("4. Buscar la primera goleada en un país")
    print("5. Calcular el desempeño de un país en otro")
    print("6. Buscar el país de la suerte de otro")
    print("7. Buscar los partidos de un torneo en una década.")
    print("8. Buscar el partido que se ha jugado más veces.")
    print("9. Buscar los países en los que se han jugado partidos pero el país no ha jugado.")
    print("10. Buscar el ganador de un torneo por puntos.")
    print("11. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    paises = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            paises = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_partido(paises)
        elif opcion_seleccionada == 3:
            ejecutar_buscar_mayor_goleada(paises)
        elif opcion_seleccionada == 4:
            ejecutar_buscar_primera_goleada(paises)
        elif opcion_seleccionada == 5:
            ejecutar_calcular_desempeno(paises)
        elif opcion_seleccionada == 6:
            ejecutar_buscar_pais_de_la_suerte(paises)
        elif opcion_seleccionada == 7:
            ejecutar_buscar_partidos_por_torneo_y_decada(paises)
        elif opcion_seleccionada == 8:
            ejecutar_buscar_partido_mas_jugado(paises)
        elif opcion_seleccionada == 9:
            ejecutar_buscar_paises_sin_jugar(paises)
        elif opcion_seleccionada == 10:
            ejecutar_buscar_ganador_por_puntos(paises)
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
