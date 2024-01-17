import calculadora_empanadas as emp

def star():
    print("Bienvido a Cupiempanadas, digite los siguientes datos para conocer el precio de venta de una promocion")
    
    precio_venta_unidad = float(input("Precio de venta de una empanada individual: "))
    cantidad_empanadas = int(input("Cantidad de empanadas"))
    
    rta = emp.calcular_precio_venta_promocion (precio_venta_unidad, cantidad_empanadas)
    
    rta_usuario = rta
    print(rta_usuario)
    
star()