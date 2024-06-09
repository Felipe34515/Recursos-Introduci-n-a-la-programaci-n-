
# Calcular moles en la sustancia

def calcular_moles_sustancia(masa_sustancia: float, masa_molar:float) -> float:
    """ Calcula la cantidad de moles de una sustancia dada su masa y masa molar
    Parametros:
        Masa sustancia(float)
        Masa molar (float)
    Retorna:
        Float: moles de la sustancia
    """
    moles_de_la_sustancia = masa_sustancia / masa_molar
    return round(moles_de_la_sustancia,3)

# Calcular cantidad de partículas en la sustancia

def calcular_particulas(masa_sustancia: float, masa_molar: float) -> float:
    """ Calcula la cantidad de partículas de una sustancia dada la masa
        de la sustancia y la masa molar presentes, utilizando la
        constante de Avogadro.
    Parametros:
        Masa sustancia(float)
        Masa molar (float)
    Retorna:
        Float: Cantidad de particulas de la sustancia
    """
    particulas_en_sustancia = calcular_moles_sustancia(masa_sustancia, masa_molar) * float(6.023e23)
    return round(particulas_en_sustancia,3)

# Calcular molaridad en la sustancia

def calcular_molaridad (masa_sustancia: float, masa_molar: float, volumen_solucion: float) -> str:
    """ Calcula la molaridad de una sustancia en una solución, dada la
        masa de la sustancia en gramos, la masa molar de la sustancia
        y el volumen de la solución en litros.

    Parametros:
        Masa sustancia(float)
        Masa molar (float)
        Volumen solución (float)
    Retorna:
        String: “Estos XX gramos diluidos en YY litros de
                solución, nos dan una molaridad de: ZZ”. Donde XX es la masa
                de la sustancia, YY el número de litros de la solución y ZZ el
                cálculo de la molaridad."

    """
    molaridad_sustancia = calcular_moles_sustancia(masa_sustancia, masa_molar)/volumen_solucion
    return str("Estos "+ str(masa_sustancia) + " gramos diluidos en " + str(volumen_solucion) +  " litros de solución, nos dan una molaridad de: "+ str(molaridad_sustancia))

# Calcular moles gases ideales

def calcular_moles_gases_ideales (presion: float, volumen: float, temperatura: float) -> float:
    """ Calcula la cantidad de moles de un gas utilizando la ecuación de
        los gases ideales. 
    Parametros:
        Presión (float)
        Volumen (float)
        Temperatura (float)
    Retorna:
        Float: Moles del gas en las condiciones dadas.
    """
    r = 0.0821
    moles_de_gas_condiciones = (presion * volumen)/(r * temperatura)
    return round(moles_de_gas_condiciones,3)

#Calcular alquimia ajiaco

def alquimia_ajiaco (presion: float, volumen: float, temperatura: float, botella: int) -> int:
    """ Calcula la cantidad estricta de botellas que es posible llenar a
        partir de la información del vapor de agua capturado.
    Parametros:
        Presión (float)
        Volumen (float)
        Temperatura (float)
        botella (int)
    Retorna:
        int: El número de botellas del volumen dado que es posible llenar a
        partir de los moles de agua capturados en el proceso de
        alquimia.
    """
    masa_molar = 18.015
    numero_de_botellas = (calcular_moles_gases_ideales(presion, volumen, temperatura)*masa_molar)//botella
    return numero_de_botellas

