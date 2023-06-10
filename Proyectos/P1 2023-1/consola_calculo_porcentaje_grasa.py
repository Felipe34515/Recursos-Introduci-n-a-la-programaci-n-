
import calculadora_indices as mod

def ejecutar_calculo_porcentaje_grasa()-> None:
    
    print("Porfavor ingrese los siguientes datos pra saber su porcentaje de grasa")
    peso = float(input("Peso (en kilogramos):"))
    altura = float(input("Altura (en metros):"))
    edad = int(input("Edad:"))
    valor_genero = float(input("Ingrese el valor 10.8 si usted es hombre y 0 si es mujer:"))
    
    PG= mod.calcular_porcentaje_grasa (peso,altura,edad,valor_genero)
    print(("\n\n Su porcentaje de grasa es: "), round(PG,2), "%")
    
    
def iniciar_aplicación ()->None:
    print("\n Bienvenido, En esta aplicación vamos a conocer diferentes índices corporales que nos permitiran conocer su estado de salud")
    ejecutar_calculo_porcentaje_grasa()
        
iniciar_aplicación()




