import cupy_quesos as c   
def porcion_m():
    costo_l= float(input("ingrese costo de leche:  "))
    cantidad_l= float(input("ingrese cantidad de leche:  "))
    costo_al= float(input("ingrese costo de almacenamiento:  "))
    costo_ad= float(input("ingrese costos extra:  "))
    temperatura= float(input("ingrese temperatura de almacenamiento leche:  "))
    humedad= float(input("ingrese humedad que debe estar la leche:  "))
    angulo_corte= float(input("ingrese angulo de corte:  "))
    costo_pm= c.calcular_costo_porcion_madurado( costo_l, cantidad_l, costo_al, costo_ad, temperatura, humedad, angulo_corte)
    print("el costo de la porcion de queso madurado es de:  "+str(costo_pm))
porcion_m()
    