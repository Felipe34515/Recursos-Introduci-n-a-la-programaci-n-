import calculadora_empanadas as emp

def star()-> None:
    print("Bienvido a Cupiempanadas, digite los siguientes datos para conocer la meta de la empresa")
    
    arriendo = float(input("Valor diario del arriendo: "))
    numero_empleados = int(input("Número de empleados en turno: "))
    precio_venta = float(input("Precio de venta de una empanada: "))
    precio_carne = int(input("Precio de la carne por kilogramo: "))
    precio_papa = int(input("Precio de la papa por libra: "))
    precio_aceite = int(input("Precio del aceite por litro: "))
    
    rta = emp.calcular_cantidad_empanadas_meta(arriendo, numero_empleados, precio_venta, precio_carne, precio_papa, precio_aceite)
    
    rta_usuario = "La respuesta es " + str(rta) + " empanadas necesarias para cumplir la meta"
    print(rta_usuario)
    
star()