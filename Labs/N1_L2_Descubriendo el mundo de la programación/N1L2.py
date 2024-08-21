# Autor: Felipe Rueda


def actividad1 ():
    """ 
    Para obtener el perfil anterior, usted debe construir un programa que le solicite al usuario 
    los nombres de 3 estudiantes, junto con sus respectivos años de nacimiento y que imprima 
    en pantalla la información del perfil.
    """
    estudiante1= input("Ingrese el nombre del estudiante 1: ")
    anioNacimiento = input("Ingrese el año de nacimiento del estudiante 1: ")
    estudiante2= input("Ingrese el nombre del estudiante 2: ")
    anioNacimiento2 = input("Ingrese el año de nacimiento del estudiante 2: ")
    estudiante3= input("Ingrese el nombre del estudiante 3: ")
    anioNacimiento3 = input("Ingrese el año de nacimiento del estudiante 3: ")

    edad1 = 2021 - int(anioNacimiento)
    edad2 = 2021 - int(anioNacimiento2)
    edad3 = 2021 - int(anioNacimiento3)

    mayor = max(edad1, edad2, edad3)
    menor = min(edad1, edad2, edad3)

    print(estudiante1 + " este año cumple " + str(edad1) + " años.")
    print(estudiante2 + " este año cumple " + str(edad2) + " años.")
    print(estudiante3 + " este año cumple " + str(edad3) + " años.")
    print("el promedio de edad de los estudiantes es: " + str(round((edad1 + edad2 + edad3) / 3),2))
    print("La diferencia de edad entre el mayor y el menor es: " + str(mayor - menor) + " años.")
    
# actividad1()

def actividad2(segundos):
    """
    Escriba un programa que convierta una medida en tiempo en segundos a días, horas, 
    minutos y segundos. Para esto debe solicitar al usuario un valor entero que va a 
    representar la medida de tiempo en segundos.
    Su programa debe informar el resultado de la conversión con un mensaje de la forma: “El 
    tiempo ingresado corresponde a 11 días, 10 horas, 17 minutos y 36 segundos”
    """
    segundos = int(input("Ingrese la cantidad de segundos: "))
    minutos = segundos // 60
    segundos = segundos % 60
    horas = minutos // 60
    días = horas // 24
    horas = horas % 24
    print("Días: " + str(días) + " Horas: " + str(horas) + " Minutos: " + str(minutos) + " Segundos: " + str(segundos))
    
# actividad2(100000)
    
def actividad3():
    """
    En esta actividad usted deberá escribir un programa que calcule la fuerza de gravedad 
    universal entre dos cuerpos celestes dadas sus masas y la distancia entre ellos. Para esto, 
    debe solicitar al usuario la masa de cada uno de los planetas y la distancia que los separa, 
    y una vez realizada la operación deberá informar al usuario el resultado con el siguiente 
    mensaje: “La fuerza gravitacional es: 3.55e22 N
    """
    masa1 = float(input("Ingrese la masa del primer cuerpo celeste (kilogramos): "))
    masa2 = float(input("Ingrese la masa del segundo cuerpo celeste (kilogramos): "))
    distancia = float(input("Ingrese la distancia entre los cuerpos celestes (metros): "))
    G = 6.674e-11
    fuerza = G * ((masa1 * masa2) / distancia**2)
    print("La fuerza gravitacional es: " + str(fuerza) + " N")
    
# actividad3()
    


