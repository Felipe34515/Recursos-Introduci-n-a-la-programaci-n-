# -------------------------
# Algoritmos iterativos
# Lección 8 (Patrones de recorrido)
# -------------------------
a = [ 34, 12, 6, 64, 3, 2, 1, 8]

# for sin range
def forIn(lista):
    for i in lista:
        print(i)   
# for Con range
def forInRange(lista):
    for i in range(0, len(lista)):
        print(i)
        
# While que simula un for in 
def whileSinRange(lista):
    i = 0
    while i <= len(lista):
        print(i)

# While que simula un for in range
def whileConRange(lista):
    i = 0
    while i <= len(lista):
        print(a[i])
        

# print(forIn(a))
# print(whileSinRange(a))
print(forInRange(a))
# print(whileConRange(a))

# -------------------------
# Algoritmos iterativos
# Lección 9 (recorrido en diccionarios)
# -------------------------

d = {"Juan": 4.1, "Pepe": 3.8, "Cristiana": 4.2, "Saldra": 3.5}


def sacarLlaves(diccionario):
    for i in diccionario:
        print(i)
        
def sacarValores(diccionario):
    for i in diccionario:
        print(diccionario[i])
        
def sacarTodo(diccionario):
    for i in diccionario:
        print(i, diccionario[i])
        
# print(sacarLlaves(d))
# print(sacarValores(d))
# print(sacarTodo(d))


# -------------------------
# Manejo de archivos
# Lección 10 (manejo archivos)
# -------------------------


n = "C:/Users/felip/Documents/Semestres/2023-1/Monitoria IP/Monitoría N3/personas.txt"
# n = "../atletas.csv"
def leerArchivo(nombre):
    file = open( nombre, 'r')
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
    file.close()

# leerArchivo(n)

# import os
# print(os.getcwd())
          
 
# -------------------------
# Estructuras de datos compuestas
# Lección 11 (Estructuras de datos compuestas)
# ------------------------- 

def cargarDatos(nombre):
    file = open( nombre, 'r')
    line = file.readline()
    line = file.readline()
    personas ={}
    
    while len(line) > 0:
        lista = line.split(",")
        datos ={}
        datos["correo"] = lista[1]
        datos["telefono"] = lista[2]
        personas[lista[0]] = datos
        line = file.readline()
        
    print(personas)
           
        
# cargarDatos(n)



# alfa = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
# # print(alfa[4])
    
# def impresionNums():
#     for i in range(1,17):
#         rta = []
#         div = i//27
#         mod = i%27
#         rta.insert(0,alfa[mod])
#         while (div > 26):
#             div = div//26
#             rta.insert(0,alfa[div%26])
#         print(i , rta)
            
# impresionNums()

# z = 702%26
# print(z)
        
atletas = [    {'nombre': 'Usain Bolt', 'genero': 'm', 'edad': 30, 'pais': 'Jamaica', 'anio': 2016, 'evento': '100m', 'medalla': 'gold'},
           {'nombre': 'Simone Biles', 'genero': 'f', 'edad': 19, 'pais': 'Estados Unidos', 'anio': 2016, 'evento': 'gimnasia', 'medalla': 'gold'},
           {'nombre': 'Michael Phelps', 'genero': 'm', 'edad': 31, 'pais': 'Estados Unidos', 'anio': 2016, 'evento': 'natación', 'medalla': 'silver'},
           {'nombre': 'Katie Ledecky', 'genero': 'f', 'edad': 19, 'pais': 'Estados Unidos', 'anio': 2016, 'evento': 'natación', 'medalla': 'gold'},
           {'nombre': 'Mo Farah', 'genero': 'm', 'edad': 33, 'pais': 'Gran Bretaña', 'anio': 2016, 'evento': '5,000m', 'medalla': 'gold'},
           {'nombre': 'Laura Trott', 'genero': 'f', 'edad': 24, 'pais': 'Gran Bretaña', 'anio': 2016, 'evento': 'ciclismo', 'medalla': 'gold'},
           {'nombre': 'Rafael Nadal', 'genero': 'm', 'edad': 30, 'pais': 'España', 'anio': 2016, 'evento': 'tenis', 'medalla': 'na'},
           {'nombre': 'Serena Williams', 'genero': 'f', 'edad': 34, 'pais': 'Estados Unidos', 'anio': 2016, 'evento': 'tenis', 'medalla': 'na'}]


evento = "gimnasia"

def p6 (lista, evento):
    visitados =[]
    rta = {}
    for dicc in lista:
        if (dicc["evento"] not in visitados):
            visitados.append(dicc["nombre"])
            rta[dicc["evento"]] = [dicc["nombre"]]
        else:
            a = rta[dicc["evento"]]
            a.append(dicc["nombre"])
            rta[dicc["nombre"]] = a
    return rta


# print(p6(atletas, evento))

def mas_medallistas(atletas:list) ->dict:
    dicc={}
    
    for cada_elemento in atletas:
        if cada_elemento["pais"] != "na":
            if cada_elemento["pais"] in dicc:
                dicc[cada_elemento["pais"]] += 1
            else:
                dicc[cada_elemento["pais"]]=1
                
    return dicc

def cuantas_medallas_cada_atleta(olimpicos:list)->dict:
    # nuevo_dict = {}
    # for atleta in olimpicos:
    #     atleta = atleta["nombre"]
    #     if atleta["medalla"] != "na":
    #         if atleta not in nuevo_dict:
    #             nuevo_dict[atleta]=0
    #         nuevo_dict[atleta] += 1
    return olimpicos


def producto_mas_costoso(carrito_compras: dict)->str:
    if len(carrito_compras) == 0:
        rta = "No hay productos en el carrito"
    max = -1
    for producto in carrito_compras:
        if max < carrito_compras[producto]:
            max = carrito_compras[producto]

    for producto in carrito_compras:
        if max == carrito_compras[producto] and encontrado == False:
            encontrado = True
            rta = producto

    return rta
