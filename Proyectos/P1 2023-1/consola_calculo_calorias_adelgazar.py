

import calculadora_indices as mod

def consumo_calorias_recomendadas_para_adelgazar()-> None:
    print("\n Porfavor ingrese los siguientes datos su tasa metabólica basal")
    peso = float(input("Peso (en kilogramos):"))
    altura = float(input("Altura (en centimetros):"))
    edad= int(input("Edad:"))
    valor_genero = float(input("Ingrese 5 en caso de ser hombre y -161 si es mujer: "))
    
    TMB= mod.consumo_calorias_recomendadas_para_adelgazar (peso,altura,edad,valor_genero)
    CAC_minimo= float(TMB* 0.80)
    CAC_máxima= float(TMB*0.85)
    
    print("\n\n Lo recomendable es que usted consuma entre", round(CAC_minimo,2), "a", round(CAC_máxima,2), "calorias para adelegazar")
    
def iniciar_aplicación ()->None:
    print("\n Bienvenido, En esta aplicación vamos a conocer diferentes índices corporales que nos permitiran conocer su estado de salud")
    consumo_calorias_recomendadas_para_adelgazar()
    
iniciar_aplicación()
    
    
    
    