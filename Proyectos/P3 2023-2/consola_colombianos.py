"""
Ejercicio nivel 3: Colombianos en Wikipedia.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""
import colombianos as c


def ejecutar_cargar_datos() -> dict:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de los jugadores.
    Retorno: dict
        El diccionario de ocupaciones con la información de los colombianos en el archivo
    """
    colombianos = None
    archivo = input(
        "Por favor ingrese el nombre del archivo CSV con los colombianos en Wikipedia: ")
    colombianos = c.cargar_datos(archivo)
    if len(colombianos) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los bloques.")
    else:
        print("Se cargaron los siguientes ocupaciones a partir del archivo.")
        for key in colombianos.keys():
            print(key)
    return colombianos


def ejecutar_mayor_lectores(colombianos: dict) -> None:
    """Ejecuta la opción de encontrar el colombiano con mayor número de lectores.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El colombiano con mayor número de lectores en Wikipedia es (nombre del colombiano)'
    """
    a=c.mayor_lectores(colombianos)
    print("El colombiano con mayor número de lectores en Wikipedia es " + str(a))
def ejecutar_hay_3_colombianos(colombianos: dict) -> None:
    """Ejecuta la opción que busca si hay 3 colombianos que superen un número de lectores
       dada una ocupación, un género y un número de lectores a superar.  
    La consola debe mostrar un mensaje con el siguiente mensaje según el caso:
        'Sí existen 3 colombianos de este género y ocupación que superen este tope.'
        'No existen 3 colombianos de este género y ocupación que superen este tope.'
    """
    b=input("Ingrese un genero(Male o Female): ")
    a=input("Ingrese una ocupación dentro de las mostradas en la opción 1: ")
    e=int(input("Ingrese el número de lectores a superar: "))
    d=(c.hay_3_colombianos(colombianos,a,b,e))
    if d==True:
        print("Sí existen 3 colombianos de este género y ocupación que superen este tope.")
    else:
        print("No existen 3 colombianos de este género y ocupación que superen este tope.")


def ejecutar_promedio_lectores(colombianos: dict) -> None:
    """Ejecuta la opción de calcular el promedio de lectores de las personas de una ocupación específica. 
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'El número de lectores promedio de los colombianos con ocupación (ocupacion) es (número de lectores promedio).'
    """
    b=input("Ingrese una ocupación dentro de las mostradas en la opción 1: ")
    d=c.promedio_lectores(colombianos, b)
    print("El número de lectores promedio de los colombianos con ocupación " + str(b) + " es " + str(d) + ".")
def ejecutar_mayor_rating(colombianos: dict) -> None:
    """Ejecuta la opción de encontrar la ocupación con mayor número de lectores promedio
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
        'La ocupación con mayor número de lectores promedio es (ocupación).'
    """
    a=(c.mayor_rating(colombianos))
    print("La ocupación con mayor número de lectores promedio es " + str(a) + ".")

def ejecutar_colombianos_rango(colombianos: dict) -> None:
    """Ejecuta la opción que consulta colombianos con una ocupación específica que hayan nacido en un rango de años
    Se debe mostrar al usuario solo los nombres de los colombianos que cumplen con la condición.
    """
    b=int(input("Ingrese el año de nacimiento minimo: "))
    a=int(input("Ingrese el año de nacimiento maximo: "))
    e=input("Ingrese una ocupación dentro de las mostradas en la opción 1: ")
    d=(c.colombianos_rango(colombianos,e,b,a))
    for x in d:
        for llaves,valores in x.items():
            if llaves=="nombre":
                print(x["nombre"])
def ejecutar_nacionalidades(colombianos: dict) -> None:
    """Ejecuta la opción que cuenta cuantas personas hay de cada nacionalidad. 
    Se debe mostrar al usuario un mensaje que luzca así:
        '(nacionalidad) --> (número de personas con esa nacionalidad)'
    Ejemplo:
        Colombia - Peru --> 2
        Colombia - Mexico --> 7
    """
    d=c.nacionalidades(colombianos)
    for llave,valor in d.items():
        print(str(llave) + " --> " + str(valor))
def ejecutar_calcular_edad(colombianos: dict) -> None:
    """Ejecuta la opción de calcular la edad de cada persona.
    Se debe mostrar al usuario el diccionario de colombianos con la edad incluida
    """
    print(c.calcular_edad(colombianos))

def ejecutar_colombianos_fallecidos(colombianos: dict) -> None:
    """Ejecuta la opción que consulta qué colombianos han fallecido.
    Se debe mostrar al usuario los nombres de los colombianos que han fallecido.
    """
    d=(c.colombianos_fallecidos(colombianos))
    for llaves,valores in d.items():
        for valor in valores:
            for llave,va in valor.items():
                if llave=="nombre":
                    print(va)
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de colombianos.")
    print("2. Encontrar el colombiano con mayor número de lectores.")
    print("3. Encontrar si hay 3 colombianos que superen el tope de lectores.")
    print("4. Calcular el promedio de lectores de las personas de una ocupación específica.")
    print("5. Encontrar qué ocupación es la que tiene mayor número de lectores promedio.")
    print("6. Consultar colombianos con una ocupación específica que hayan nacido en un rango de años.")
    print("7. Contar cuantas personas hay de cada nacionalidad.")
    print("8. Calcular la edad de cada persona. ")
    print("9. Consultar qué colombianos han fallecido.")
    print("10. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    colombianos = {}
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            colombianos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mayor_lectores(colombianos)
        elif opcion_seleccionada == 3:
            ejecutar_hay_3_colombianos(colombianos)
        elif opcion_seleccionada == 4:
            ejecutar_promedio_lectores(colombianos)
        elif opcion_seleccionada == 5:
            ejecutar_mayor_rating(colombianos)
        elif opcion_seleccionada == 6:
            ejecutar_colombianos_rango(colombianos)
        elif opcion_seleccionada == 7:
            ejecutar_nacionalidades(colombianos)
        elif opcion_seleccionada == 8:
            ejecutar_calcular_edad(colombianos)
        elif opcion_seleccionada == 9:
            ejecutar_colombianos_fallecidos(colombianos)
        elif opcion_seleccionada == 10:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
