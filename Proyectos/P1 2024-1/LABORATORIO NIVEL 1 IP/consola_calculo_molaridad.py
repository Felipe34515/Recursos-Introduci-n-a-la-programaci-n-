import calculadora_quimica as cal

def ejecutar_calcular_molaridad () -> None:
    masa_sustancia = float(input("Ingrese la masa de la sustacia: "))
    masa_molar = float(input ("Ingrese la masa molar de la sustancia: "))
    volumen_solucion = float(input ("Ingrese el volumen de la sustancia: "))
    molaridad_fin = cal.calcular_molaridad(masa_sustancia, masa_molar, volumen_solucion)
    return molaridad_fin

print("El número de molaridad es:", ejecutar_calcular_molaridad())

