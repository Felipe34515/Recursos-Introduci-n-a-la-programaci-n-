
import calculadora_indices as mod

def ejecutar_consola_calculo_imc()-> None:
    
    print("\n Porfavor ingrese los siguientes datos para saber su índice de masa corporal")
    peso = float(input("Peso (en kilogramos):"))
    altura = float(input("Altura (en metros):"))
    
    IMC = mod.calcular_IMC (peso, altura)
    print("\n\n El índice de masa corporal es:" , round(IMC,2))
    
def iniciar_aplicación()->None:
    print ( "\n Bienvenido, En esta aplicación vamos a conocer diferentes índices corporales que nos permitiran conocer su estado de salud")
    ejecutar_consola_calculo_imc()
    
iniciar_aplicación()

    





