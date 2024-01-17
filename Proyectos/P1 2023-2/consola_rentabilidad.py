import calculadora_empanadas as emp

def star():
    print("Bienvido a Cupiempanadas, digite los siguientes datos para conocer su rentabilidad")
    
    precio_venta = float(input("Precio de venta de una empanada: "))
    precio_carne = int(input("Precio de la carne por kilogramo: "))
    precio_papa = int(input("Precio de la papa por libra: "))
    precio_aceite = int(input("Precio del aceite por litro: "))
    
    rta = emp.calcular_rentabilidad(precio_venta, precio_carne, precio_papa, precio_aceite)
    
    rta_usuario = "La respuesta es " + str(rta) + " y significa la ganancia neta de una única empanada"
    print(rta_usuario)

star()