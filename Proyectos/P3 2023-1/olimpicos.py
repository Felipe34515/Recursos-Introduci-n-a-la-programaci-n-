# -*- coding: utf-8 -*-
"""

@author: Felipe Rueda
"""
def cargar_atletas(ruta_archivo: str) ->list:
    atletas=[]
    archivo=open(ruta_archivo)
    titulos=archivo.readline()
    #print (titulos)
    
    linea=archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        atleta = {}
        atleta["nombre"] = datos[0]
        atleta["genero"] = datos[1]
        atleta["edad"] = datos[2]
        atleta["pais"] = datos[3]
        atleta["anio"] = datos[4]
        atleta["evento"] = datos[5]
        atleta["medalla"] = datos[6]
        atletas.append(atleta)
        linea = archivo.readline()
        
    archivo.close()
    return atletas

def atletas_por_anio(atletas:list, anio:int) ->dict:
    dicc={}
    print (dicc)
            
    
    for cada_elemento in atletas:
        #print (cada_elemento)
        if int(cada_elemento["anio"]) == int(anio):
            if cada_elemento["evento"] not in dicc:
                #print(cada_elemento["nombre"])
                dicc[cada_elemento["evento"]]=[cada_elemento["nombre"]]
            else:
                dicc[cada_elemento["evento"]].append(cada_elemento["nombre"])

                
    return dicc

#print (atletas_por_anio(cargar_atletas("atletas.csv"), 2016))     
#print (x)

def medallas_en_rango (atletas:list, anio_inicial:int, anio_final:int, nombre: str)->list:
    lista=[]

    
    for cada_elemento in atletas:
        dic_f={}
        if  cada_elemento["nombre"]==nombre:
            if anio_inicial<int(cada_elemento["anio"]) and anio_final>int(cada_elemento["anio"]):
                dic_f["evento"]=cada_elemento["evento"]
                dic_f["anio"]=cada_elemento["anio"]
                dic_f["medalla"]=cada_elemento["medalla"]
                lista.append(dic_f)

            #print(dic_f)        
    return lista

#print (medallas_en_rango(cargar_atletas("atletas.csv"), 2006,2016,"elvan abeylegesse"))

def atletas_por_pais (atletas: list, pais: str) ->list:
    
    lista=[]
    for cada_elemento in atletas:
        dicc={}
        
        if cada_elemento["pais"]==pais:
            dicc["nombre"]=cada_elemento["nombre"]
            dicc["evento"]=cada_elemento["evento"]
            dicc["anio"]=cada_elemento["anio"]
            lista.append(dicc)
            
    return lista

#print (atletas_por_pais(cargar_atletas("atletas.csv"), "canada"))


def pais_con_mas_atletas(atletas:list) ->dict:
    
    
    
    dicc={}
    for atleta in atletas:
        pais = str(atleta["pais"])
        medalla = str(atleta["medalla"])
        nombre= str(atleta["nombre"])
        if medalla != "na" and medalla != "na\n":
            if pais not in dicc:
                dicc[pais]= [nombre]
            elif nombre not in dicc[pais]:
                dicc[pais].append(nombre)
                
                
    for cada_elemento in dicc:
           dicc[cada_elemento] = len(dicc[cada_elemento])   
           
    print(dicc)
    mayor=-1
    ganador=""
    dicc_f={}
    
    for cada_elemento in dicc:
        if dicc[cada_elemento]>mayor:
            mayor=dicc[cada_elemento]
            ganador=cada_elemento
            
    dicc_f[ganador]=mayor
            
            
            
    return dicc_f
            
#print (pais_con_mas_atletas(cargar_atletas("atletas.csv")))

def medallistas_por_evento(atletas:list, evento: str) ->list:

    lista = []
    for cada_elemento in atletas:
        if evento == cada_elemento["evento"] and cada_elemento["medalla"] != "na" and cada_elemento["medalla"] != "na\n":
            if cada_elemento["nombre"] not in lista:
                lista.append(cada_elemento["nombre"])
                
    return lista
            
            
#print (medallistas_por_evento(cargar_atletas("atletas.csv"), "athletics women's 5000 metres"))           
            
def atletas_con_mas_medallas_que (atletas:list, numero:int) ->dict:
    dicc={}
    
    for cada_elemento in atletas:
        if cada_elemento["medalla"]!="na" and cada_elemento["medalla"]!="na\n":
            if cada_elemento["nombre"] in dicc:
                dicc[cada_elemento["nombre"]] += 1
            else:
                dicc[cada_elemento["nombre"]]=1
                
    dicc_f={}
    #print (dicc)
        
    for cada_elemento in dicc:
        if int(dicc[cada_elemento])>=numero:
            dicc_f[cada_elemento]=dicc[cada_elemento]
        else:
            None
            
    return dicc_f

#print (atletas_con_mas_medallas_que(cargar_atletas("atletas.csv"), 8))  

def atleta_estrella (atletas:list) ->dict:
    dicc={}
    
    for cada_elemento in atletas:
        if cada_elemento["medalla"]!="na" and cada_elemento["medalla"]!="na\n" :
            if cada_elemento["nombre"] in dicc:
                dicc[cada_elemento["nombre"]] += 1
            else:
                dicc[cada_elemento["nombre"]]=1
    
    mayor=-1
    ganador=""
    dicc_f={}
    
    for cada_elemento in dicc:
        if dicc[cada_elemento]>mayor:
            mayor=dicc[cada_elemento]
            ganador=cada_elemento
            
    dicc_f[ganador]=mayor
            
            
            
    return dicc_f

#print (atleta_estrella(cargar_atletas("atletas.csv"))) 

def auxiliar (diccionario:dict, numero:int) :
    maximo=0
    dicc={}
    
    for cada_elemento in diccionario:
        if int(diccionario[cada_elemento][numero])>int(maximo):
            maximo=diccionario[cada_elemento][numero]
            
    for cada_elemento in diccionario:
        if int(diccionario[cada_elemento][numero]) == int(maximo):
            dicc[cada_elemento]=diccionario[cada_elemento]
    
    return dicc

def mejor_pais_en_un_evento (atletas:list, evento:str) ->dict:
    
    diccionario={}
    
    for cada_elemento in atletas:
        if cada_elemento["evento"]==evento and cada_elemento["medalla"]!="na" and cada_elemento["medalla"]!="na\n":
            
            if cada_elemento["pais"] not in diccionario:
                diccionario[cada_elemento["pais"]]= [0,0,0]
            if cada_elemento["medalla"]=="gold" or cada_elemento["medalla"]=="gold\n" :
                diccionario[cada_elemento["pais"]][0] += 1
            elif cada_elemento["medalla"]=="silver" or cada_elemento["medalla"]=="silver\n":
                diccionario[cada_elemento["pais"]][1] += 1
            else:
                diccionario[cada_elemento["pais"]][2] += 1
                
    respuesta=auxiliar(diccionario, 0)
    if len(diccionario)>1:
        respuesta= auxiliar(respuesta, 1)
    if len(diccionario)>2:
        respuesta=auxiliar(respuesta, 2)
        
            
    return respuesta

#print (mejor_pais_en_un_evento(cargar_atletas("atletas.csv"), "basketball men's basketball"))


                
def todoterreno (atletas:list) ->str:
    dicc={}
    for a in atletas: 
        if a["nombre"] not in dicc:
            dicc[a["nombre"]]= []
            dicc[a["nombre"]] += [a["evento"]]
        else: 
            if a["evento"] not in dicc[a["nombre"]]:
                dicc[a["nombre"]] += [a["evento"]]
    dicci={}
    for x in dicc:
        dicci[x]= len(dicc[x])
        
    mayor=0
    mejor=""
    
    for atleta in dicci:
        if dicci[atleta]>mayor:
            mayor= dicci[atleta]
            mejor= atleta
            
    return mejor
    
#print(todoterreno (cargar_atletas("atletas.csv"))) 
    
def medallistas_por_nacion_y_genero (atletas: list, pais:str, genero:str)->dict:
    
    dicc={}
    
    for cada_elemento in atletas:
        dic_f={}
        if cada_elemento["pais"]==pais and cada_elemento["medalla"] != "na" and cada_elemento["medalla"] != "na\n"and cada_elemento["genero"]==genero:
            #dic_f["nombre"]=cada_elemento["nombre"]
            dic_f["evento"]=cada_elemento["evento"]
            dic_f["anio"]=cada_elemento["anio"]
            dic_f["medalla"]=cada_elemento["medalla"]
            
            if cada_elemento["nombre"] in dicc:
                dicc[cada_elemento["nombre"]].append(dic_f)
            else:
                dicc[cada_elemento["nombre"]] = [dic_f]
                
    return dicc

#print (medallistas_por_nacion_y_genero(cargar_atletas("atletas.csv"), "colombia", "m"))

def porcentaje_medallistas(atletas:list)->float:

    dicc={}
    dicc_2={}
    
    for cada_elemento in atletas:
        if cada_elemento["medalla"]!="na" and cada_elemento["medalla"]!="na\n":
            if cada_elemento["nombre"] in dicc:
                dicc[cada_elemento["nombre"]] += 1
            else:
                dicc[cada_elemento["nombre"]]=1
    
    numero_medallistas= len(dicc)
    #print(numero_medallistas)
    
    for cada_elemento in atletas:
        if cada_elemento["nombre"] in dicc_2:
            dicc_2[cada_elemento["nombre"]] += 1
        else:
            dicc_2[cada_elemento["nombre"]]=1
                
    numero_atletas=len(dicc_2)
    #print(numero_atletas)
    
    porcentaje=numero_medallistas/numero_atletas*100
    
    redondeado=round(porcentaje,2)

    return redondeado

#print (porcentaje_medallistas(cargar_atletas("atletas.csv"))) 
        
            
            
            
            
            
    
    


            
