import calculadora_empanadas as emp

def star():
    print("Bienvido a Cupiempanadas, digite los siguientes datos para conocer el tiempo e cocción de varias empanadas")
    
    tiempo_por_empanada = int(input("Tiempo en segundos que tarda en cocinarse una empanada: "))
    cantidad_empanadas = int(input("Cantidad de empanadas: "))
    
    rta = emp.calcular_tiempo_coccion_lote_empanadas(tiempo_por_empanada, cantidad_empanadas)
    
    rta_usuario = "La respuesta es " + str(rta) + " segundos que tardarían todas las empanadas en estar listas"
    print(rta_usuario)
    
star()
    
    