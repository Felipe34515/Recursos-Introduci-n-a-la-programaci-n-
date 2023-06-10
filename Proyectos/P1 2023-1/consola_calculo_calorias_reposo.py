
import calculadora_indices as mod

def ejecutar_calculo_calorias_reposo()-> None:
    
    print("\n Porfavor ingrese los siguientes datos su tasa metabólica basal")
    peso = float(input("Peso (en kilogramos):"))
    altura = float(input("Altura (en centimetros):"))
    edad= int(input("Edad:"))
    valor_genero = float(input("Ingrese 5 en caso de ser hombre y -161 si es mujer: "))
    
    TMB= mod.calcular_calorias_en_reposo (peso,altura,edad,valor_genero)
    print("\n\n Su tasa de metabolica basal es", float(round(TMB,2)), "cal")
    
def iniciar_aplicación()->None:
    print("\n Bienvenido, En esta aplicación vamos a conocer diferentes índices corporales que nos permitiran conocer su estado de salud")
    ejecutar_calculo_calorias_reposo()
    
iniciar_aplicación()

