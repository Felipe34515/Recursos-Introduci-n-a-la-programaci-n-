import modulo as mod

def ejecutar_bisiesto()->None:
    print("Vamos a decidir si un año es bisiesto o no")
    x = int(input("Ingrese el año: "))
    rta = mod.bisesto1(x)

def ejecutar_clasificar()->None:
    print("Vamos a determinar de qué tipo es un triángulo dados sus ángulos")
    a1 = float(input("Ingrese el primer ángulo: "))
    a2 = float(input("Ingrese el segundo ángulo: "))
    a3 = float(input("Ingrese el tercer ángulo: "))
    rta = mod.clasificar(a1, a2, a3)

def ejecutar_solucionar()->None:
    print("Vamos a tratar de hallar las soluciones de una ecuación cuadrática")
    a = float(input("Ingrese el coeficiente cuadrático: "))
    b = float(input("Ingrese el coeficiente lineal: "))
    c = float(input("Ingrese el término independiente: "))
    rta = mod.solucinar(a, b, c)

def mostrar_menu()->None:
    print ("Menu principal")
    print ("(1) Año bisiesto")
    print ("(2) Tipo de triángulo")
    print ("(3) Solución ecuación cuadrática")

    x = input("Seleccione su opción: ")

    if x == "1":
        ejecutar_bisiesto()
    elif x == "2":
        ejecutar_clasificar()
    elif x == "3":
        ejecutar_solucionar()
    else:
        print("Opción inválida")


def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

    