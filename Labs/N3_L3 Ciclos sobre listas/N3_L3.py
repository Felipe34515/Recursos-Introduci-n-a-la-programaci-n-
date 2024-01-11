
#Actividad 1.1
def Actividad1_1(lista):
    rta = []
    for i in lista:
        if i not in rta:
            rta.append(i)
    return rta



#Actvidad 1.2
def Actividad1_2 (lista):
    lista.sort()
    Actividad1_1(lista)
    rta = lista[1]
    return rta

# diciionarios de dicionarios con llave estudiante
def Actividad2(estudiantes):
    rta = []
    for i, j in estudiantes.items():
        promedioMateria = (estudiantes[i]["Nota_IP"] >= 4.8 or
                           estudiantes[i]["Nota_biofisica"] >= 4.8 or 
                           estudiantes[i]["Nota_ingles"] >= 4.8 or 
                           estudiantes[i]["Nota_bioquimica"]>= 4.8)
        promedio = (estudiantes[i]["Nota_IP"] + 
                    estudiantes[i]["Nota_biofisica"] + 
                    estudiantes[i]["Nota_ingles"] + 
                    estudiantes[i]["Nota_bioquimica"]) /4
        if promedio >= 4 and estudiantes[i]["Proceso_disiplinario"] == False and promedioMateria:
            rta.append({i:j})
    return rta
def Actividad3(frase, tamanio):
    
    rta = 0
    frase = frase.split(" ")
    for palabra in frase:
        if len(palabra) >= tamanio:
            rta += 1
    return rta


#Actividad 4
def Actividad4 (lista, sublista):
    rta = 0
    for i in range(len(lista)-len(sublista)+1):
        igual = True
        for j in range(len(sublista)):
            if lista[i+j] != sublista[j]:
                igual = False
        if igual:
            rta += 1
    return rta


#Actividad 5 
def Actividad5(lista1, lista2):
    lista = lista1 + lista2
    rta = {}
    for i in lista:
        if i not in rta:
            rta[i] = 1
        else:
            rta[i] += 1
    return rta


l = [6,7,1,2,3,4,4]
# print(Actividad1_1(l))
# print(Actividad1_2(l))

# estudiantes = {
#     "estudiante1": {
#         "Nota_biofisica": 4.5,
#         "Nota_ingles": 4.5,
#         "Nota_bioquimica": 3.8,
#         "Nota_IP": 5,
#         "Proceso_disiplinario" : False
        
#     },
#     "estudiante2": {
#         "Nota_biofisica": 4,
#         "Nota_ingles": 3,
#         "Nota_bioquimica": 2,
#         "Nota_IP": 5,
#         "Proceso_disiplinario" : True
#     },
#     "estudiante3": {
#         "Nota_biofisica": 3,
#         "Nota_ingles": 3,
#         "Nota_bioquimica": 2,
#         "Nota_IP": 4,
#         "Proceso_disiplinario" : False
#     },
#     # Agrega más estudiantes según sea necesario
# }
# print(Actividad2(estudiantes))

frase = "hola que tal al"
# print(Actividad3(frase, 2))
# print(Actividad4(frase, "al"))
# print(Actividad5(frase, "wenas  "))

