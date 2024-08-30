import cupy_quesos as c   
def dia_maduracion():
    costo_l= float(input("ingrese costo de leche:  "))
    cantidad_l= float(input("ingrese cantidad de leche:  "))
    costo_ad= float(input("ingrese costos extra:  "))
    costo_al= float(input("ingrese costo de almacenamiento:  "))
    temperatura= float(input("ingrese temperatura de almacenamiento leche:  "))
    humedad= float(input("ingrese humedad que debe estar la leche:  "))
    costo_m= c.calcular_costo_queso_madurado( costo_l, cantidad_l, costo_ad,costo_al, humedad, temperatura)
    print("costo de producir queso madurado es de:  "+ str(costo_m))

dia_maduracion()
    
    