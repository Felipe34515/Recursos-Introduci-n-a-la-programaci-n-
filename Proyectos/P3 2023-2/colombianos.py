import datetime



def cargar_datos(ruta_archivo: str)->dict:
     ocupaciones={}
     archivo=open(ruta_archivo)          
     titulos =archivo.readline().split(",")
     linea=archivo.readline()
     while len(linea) > 0:         
           datos = linea.split(",")         
           colombiano={} 
           colombiano["nombre"] = datos[0]         
           colombiano["genero"] = datos[1]         
           colombiano["anio_nacimiento"] = int(datos[2])        
           colombiano["anio_muerte"] = int(datos[3])         
           colombiano["ciudadania"] = datos[5]         
           colombiano["numero_lectores"] = int(datos[6])     
           if datos[4] not in ocupaciones:
               ocupaciones[datos[4]] = []
           ocupaciones[datos[4]].append(colombiano)
           linea =archivo.readline()     
     archivo.close()     
     return ocupaciones 
 
 
cargar_datos("colombianos.csv")


def mayor_lectores(diccionario:dict)->str:
    mayor=0
    maxi=""
    for deporte in diccionario.keys():
        for atleta in diccionario[deporte]:
            if atleta["numero_lectores"] >=mayor:
                mayor=atleta["numero_lectores"]
                maxi=atleta["nombre"]
    return maxi


def hay_3_colombianos(diccionario:dict, ocupacion:str, genero:str, lectores:int)->bool:
    numero=0
    centinela=False
    for colombiano in diccionario[ocupacion]:
        if (colombiano["genero"]==genero) and (colombiano["numero_lectores"]>lectores):
            numero+=1
    if numero>=3:
        centinela=True
    return centinela


def promedio_lectores(diccionario:dict, ocupacion:str)->float:
    promedio=0
    suma=0
    contador=0
    for llave,valor in diccionario.items():
        if llave==ocupacion:
            for x in valor:
                suma+=x["numero_lectores"]
                contador+=1
    promedio=suma/contador
    return round(promedio,2)    



def mayor_rating(diccionario:dict)->int:
    mayor=0
    maxi=""
    for llave,valor in diccionario.items():
       a=promedio_lectores(diccionario, llave)
       if a>mayor:
           mayor=a
           maxi=llave
    return maxi
          
def colombianos_rango(diccionario:dict, ocupacion:str, inferior:int, superior:int)->list:
    lista=[]
    for llave,valor in diccionario.items():
            for y in valor:
                if (y["anio_nacimiento"]<=superior) and (y["anio_nacimiento"]>=inferior) and (llave==ocupacion):
                    lista.append(y)
    return lista
def nacionalidades(diccionario:dict)->dict:
    nacion={}
    for llave,valor in diccionario.items():
        for y in valor:
            if (y["ciudadania"]) not in nacion:
                nacion[y["ciudadania"]]=0
            nacion[y["ciudadania"]]+=1
    return nacion      
def calcular_edad(diccionario:dict)->dict:
    currentDateTime=datetime.datetime.now()
    date=currentDateTime.date()
    year=int(date.strftime("%Y"))
    for llave,valor in diccionario.items():
            for y in valor:
                if y["anio_muerte"]==0:
                    edad=year-y["anio_nacimiento"]
                else:
                    edad=y["anio_muerte"]-y["anio_nacimiento"]
                y["edad"]=edad
    return diccionario


def colombianos_fallecidos(diccionario:dict)->dict:
    lista=[]
    ocupaciones={}
    for llave,valor in diccionario.items():
            for y in valor:
                if y["anio_muerte"]!=0:
                    lista.append(y)
                    if llave not in ocupaciones:
                       ocupaciones[llave] = []
                    ocupaciones[llave].append(y)
    return ocupaciones 

