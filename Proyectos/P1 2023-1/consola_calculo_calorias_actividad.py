
import calculadora_indices as mod


def ejecutar_calculo_calorias_actividad()->None:
    
    print("\n Porfavor ingrese los siguientes datos para saber su tasa metabólica basal según su actividad")
    peso = float(input("Peso(en kilogramos): "))
    altura = float(input("Altura (en centimetros):"))
    edad= int(input("Edad:"))
    valor_genero= float(input("Ingrese 5 en caso de ser hombre y -161 si es mujer: "))
    valor_actividad = float(input("Ingrese el valor correspondiente según la cantidad de actividad que hace en el transcurso de la semana:\n \n 1.2 si hace poco o ningún ejercicio a la semana\
                                   \n 1.375 si hace ejercicio de 1 a 2 días a la semana \n 1.55 si hace ejercicio de 4 a 5 días a la semana \n 1.725 si hace ejercicio de 6 a 7 días a la semana \n 1.9 si entrena dos veces al día todos los días \n \n ¿Cual es su valor? "))
    
    TMBA = mod.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print ("\n\n Su tasa metobolica basal según su activiad física es: ", float(round(TMBA,2)), "cal")
    
def iniciar_aplicación()->None:
    print("\n Bienvenido, En esta aplicación vamos a conocer diferentes índices corporales que nos permitiran conocer su estado de salud")
    ejecutar_calculo_calorias_actividad()
    
iniciar_aplicación()
    
    