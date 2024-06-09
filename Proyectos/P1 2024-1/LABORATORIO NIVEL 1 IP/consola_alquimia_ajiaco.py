import calculadora_quimica as cal

def ejecutar_calcular_alquimia_ajiaco () -> None:
    presion = float(input("Ingrese la presión: "))
    volumen = float(input ("Ingrese el volumen: "))
    temperatura = float(input ("Ingrese la temperatura: "))
    botella = int(input ("Ingrese el volumen de las botellas: "))
    alquimia_ajiaco_fin = cal.alquimia_ajiaco(presion, volumen, temperatura, botella)
    return alquimia_ajiaco_fin

print("La cantidad de botellas obtenidas será:", ejecutar_calcular_alquimia_ajiaco())

