import cupy_quesos as c    
def queso_f():
    costo_l= float( input("ingrese costo leche:  "))
    cantidad_l= float(input("ingrese cantidad leche:  "))
    costo_ad=float(input("ingrese costos extra:  "))
    costo= c.calcular_costo_queso_fresco( costo_l, cantidad_l, costo_ad)
    print(" costo de producir queso es: "+ str(costo))
    
    
queso_f()

  