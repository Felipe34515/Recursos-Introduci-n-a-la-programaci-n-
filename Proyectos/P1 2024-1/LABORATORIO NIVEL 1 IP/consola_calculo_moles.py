import calculadora_quimica as cal

def ejecutar_calcular_moles () -> None:
    masa_sustancia = float(input("Ingrese la masa de la sustacia: "))
    masa_molar = float(input ("Ingrese la masa molar de la sustancia: "))
    moles_fin = cal.calcular_moles_sustancia(masa_sustancia, masa_molar)
    return moles_fin

print("El número de moles es:", ejecutar_calcular_moles())

