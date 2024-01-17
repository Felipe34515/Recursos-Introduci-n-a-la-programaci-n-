import calculadora_empanadas as emp

def star():
    print("Bienvido a Cupiempanadas, digite los siguientes datos para conocer el costo de varias empanadas")
    
    precio_carne = int(input("Precio de la carne por kilogramo: "))
    precio_papa = int(input("Precio de la papa por libra: "))
    precio_aceite = int(input("Precio del aceite por litro: "))
    
    rta = emp.calcular_costo_empanada(precio_carne, precio_papa, precio_aceite)
    
    rta_usuario = "La respuesta es " + str(rta) + " pesos por todas esas empanadas"
    print(rta_usuario)
    
star()