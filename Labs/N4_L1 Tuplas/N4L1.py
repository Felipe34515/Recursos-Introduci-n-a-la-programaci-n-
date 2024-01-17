t = ((1,2), (2,3), (3,4))

# print(len(t))

def sumatupla(tuplas: tuple):
    rta= []
    for tupla in tuplas:
        suma = 0
        for i in range(len(tupla)):
            suma += tupla[i]
        rta.append(suma)
            
    return rta

# print(sumatupla(t))

def inverso(t ):
    longitud = len(t)-1
    rta = ()
    while longitud >= 0:
        rta += (t[longitud],)
        longitud -= 1
    return rta

def inverso2(t):
    pass
        
# print(inverso(t))

t2 = [1,2, 3]

def cubo (lista):
    rta = []
    for i in lista:
        e = i**3
        tupla = (i, e)
        rta.append(tupla)
        
    return rta

# print(cubo(t2))

# def adyacentes (lista):
#     for i in range(len(lista)-1):
        
        
        

