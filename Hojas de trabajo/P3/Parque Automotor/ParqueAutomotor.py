
def cargar_datos(nombre_archivo):
    archivo = open( nombre_archivo, "r", encoding='utf8' );
    linea = archivo.readline();
    linea = archivo.readline();
    departamentos = {}
    while linea != "":
        linea = linea.split(",")
        carro = {}
        carro["anio_registro"] = int(linea[0])
        carro["antiguo_clasico"] = linea[1]
        carro ["clase"] = linea[2]
        carro ["departamento"] = linea[3]
        carro ["marca"] = linea[4]
        carro ["servicio"] = linea[5]
        
        if linea[3] not in departamentos:
            departamentos[linea[3]] = []
        departamentos[linea[3]].append(carro)
        linea = archivo.readline();
        
    archivo.close()
    return departamentos

ED = cargar_datos("parque_automotor_2017_v2.csv")
# print(ED["Meta"][0])


def cargar_datos_v2(nombre_archivo):
    archivo = open( nombre_archivo, "r", encoding='utf8' );
    linea = archivo.readline();
    linea = archivo.readline();
    departamentos = []
    i = 0
    while linea != "":
        linea = linea.split(",")
        carro = {}
        carro["anio_registro"] = int(linea[0])
        carro["antiguo_clasico"] = linea[1]
        carro ["clase"] = linea[2]
        carro ["departamento"] = linea[3]
        carro ["marca"] = linea[4]
        carro ["servicio"] = linea[5]
        departamentos.append(carro)
        linea = archivo.readline();
        
    archivo.close()
    return departamentos

# ED = cargar_datos_v2("parque_automotor_2017_v2.csv")
# print(ED)

def clase_mas_comun(departamentos):
    rta = {}
    for departamento in departamentos.keys():
        clases = {}
        for carro in departamentos[departamento]:
            if carro ["clase"] not in clases:
                clases[carro["clase"]] = 0
            clases[carro["clase"]] += 1   
        max = 0
        clase = ""
        for llave, valor in clases.items():
            if valor > max:
                max = valor
                clase = llave
        rta[departamento] = clase
        
    return rta
print(clase_mas_comun(ED))

def deptos_al_menos_uno_diplomatico(departamentos):
    rta = []
    for departamento in departamentos.keys():
        for carro in departamentos[departamento]:
            if "Diplomatico" in carro ["servicio"] and carro ["servicio"] not in rta:
                rta.append(departamento)
                
    return rta
print(deptos_al_menos_uno_diplomatico(ED))

def marcas_por_clase(departamentos):
    rta = {}
    for departamento in departamentos.keys():
        for carro in departamentos[departamento]:
            if carro ["marca"] not in rta:
                rta[carro ["marca"]] = []
            if carro ["clase"] not in rta[carro ["marca"]]:
                rta[carro ["marca"]].append(carro ["clase"])
            
    return rta
# print(marcas_por_clase(ED))

def departamentos_condiciones_v0(departamentos):
    rta = []
    for departamento in departamentos.keys():
        for carro in departamentos[departamento]:
            if carro["anio_registro"] > 2014 and "JMC" in carro ["marca"] and departamento not in rta:
                rta.append(departamento)
    return rta
# print(departamentos_condiciones_v0(ED))

def departamentos_condiciones(departamentos):
    doc = open("departamentos_condiciones.txt", "w")
    for departamento in departamentos.keys():
        rta = False
        for carro in departamentos[departamento]:
            if carro["anio_registro"] > 2014 and "JMC" in carro ["marca"] :
                rta = True
        if rta:
            doc.write(departamento + "\n")
departamentos_condiciones(ED)


def clase_mas_comun_V2(departamentos):
    rta = {}
    for departamento in departamentos.keys():
        clases = {}
        for carro in departamentos[departamento]:
            if carro ["clase"] not in clases:
                clases[carro["clase"]] = 0
            clases[carro["clase"]] += 1   
        max = 0
        clase = 0
        for llave, valor in clases.items():
            if valor > max:
                max = valor
                clase = valor
        rta[departamento] = clase
        
    return rta

# print("")
# print(clase_mas_comun(ED))
# print("")
# print(clase_mas_comun_V2(ED))

# profesiones = ["Médico", "Ingeniero", "Profesor", "Abogado", "Diseñador", "Programador", "Enfermero", "Arquitecto", "Artista", "Científico", "Chef", "Policía", "Bombero", "Periodista", "Electricista"]

# for i in range(len(profesiones)):
#         print(profesiones[i], i)
    
    

# numeros = [7, 2, 5, 1, 9, 3]
# numeros.sort()
# print(numeros)

# palabras = ["manzana", "banana", "naranja", "uva", "pera"]
# palabras.sort()
# print(palabras)

# palabras = ["manzana", "banana", "naranja", "uva", "pera"]
# palabras_ordenadas = sorted(palabras)
# print(palabras_ordenadas)





