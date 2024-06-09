import calculadora_quimica as cal

def ejecutar_calcular_particulas () -> None:
    masa_sustancia = float(input("Ingrese la masa de la sustacia: "))
    masa_molar = float(input ("Ingrese la masa molar de la sustancia: "))
    particulas_fin = cal.calcular_particulas (masa_sustancia, masa_molar)
    return particulas_fin

print("El número de particulas es:", ejecutar_calcular_particulas())