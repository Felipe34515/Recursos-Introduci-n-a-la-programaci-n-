import cupy_quesos as c   
def dias():
    cantidad_l= float(input("ingrese cantidad de leche:  "))
    temperatura= float(input("ingrese la temperatura de la leche:  "))
    humedad= float(input("ingrese humedad a la cual debeb estar la leche:  "))
    tamano= c.calcular_dia_maduracion(cantidad_l,temperatura, humedad)
    print("los dias de maduracion del queso son:  "+ str(tamano))
dias()