

def bisesto1(anio:int)-> bool:
    if (anio%4 != 0):
        rta = False
    elif (anio%100 != 0):
        rta = True
    elif (anio%400 != 0):
        rta = False
    else:
        rta = True
    return rta
        
def bisesto2(anio:int)-> bool:
    rta = True
    if((anio%4 != 0 and anio%100 != 0 and anio%400 != 0) or (anio%4 != 0 and anio%100 == 0)):
        rta = False
    return rta

anio = 1984
# print(bisesto1(anio))
# print(bisesto2(anio))



def solucinar(a,b,c):
    i = ((b**2)- 4*a*c)
    if (i<0):
        rta = "No se puede hacer esa operación"
    else:
        p = (-b + i**(1/2))/ (2*a)
        n = (-b - i**(1/2))/ (2*a)
        if (p != n):
            rta = "Las dos respuestas son " + str(round(p, 2)) + " y " + str(round(n, 2))
        else:
            rta = "La respuesta es " + str(n)
    return rta

# Sin solución
# a = 2
# b = 4
# c = 9

# Con solo una solución
# a = 1
# b = -6
# c = 9

#Con dos soluciones
a = 1
b = -5
c = 6


print(solucinar(a,b,c))


