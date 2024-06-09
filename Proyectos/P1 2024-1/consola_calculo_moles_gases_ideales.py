import calculadora_quimica as cal

def ejecutar_calcular_moles_gases_ideales () -> None:
    presion = float(input("Ingrese la presión: "))
    volumen = float(input ("Ingrese el volumen: "))
    temperatura = float(input ("Ingrese la temperatura: "))
    moles_gases_ideales_fin = cal.calcular_moles_gases_ideales(presion, volumen, temperatura)
    return moles_gases_ideales_fin

print("El número de moles es:", ejecutar_calcular_moles_gases_ideales())

