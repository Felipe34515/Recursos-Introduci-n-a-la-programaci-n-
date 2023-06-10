# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:52:14 2020

@author: felip
"""

def atletas (archivo:str)->list:
    atletas = []
    archivo = open(archivo, "r")
    titulos = archivo.readline()
    print(titulos)
    linea = archivo.readline()
    
    
    while len(linea) > 0:
        
        linea= linea[:len(linea)-1]
        datos = linea.split(",")
        deportistas= {}
        
        deportistas["nombre"] = datos[0]
        deportistas["genero"] =datos[1]
        deportistas["edad"]=datos[2]
        deportistas["pais"]=datos[3]
        deportistas["anio"]=datos[4]
        deportistas["evento"]=datos[5]
        deportistas["medalla"]=datos[6]
        atletas.append(deportistas)
        
        linea = archivo.readline()

    archivo.close()
    return atletas

def funcion_2 (atletas:list,anio_in:int)->dict:
    rta= {}
    for atleta in atletas:
        anio = int(atleta["anio"])
        deporte= atleta["evento"]
        nombre= atleta["nombre"]
        if anio== anio_in:
            if deporte not in rta:
                rta[deporte]=[nombre]
            else:
                rta[deporte].append(nombre)
    return rta


def funcion_3(atletas:list,anio_inicio:int,anio_final:int,nom_interes:str)->list:

    rta = []
    
    for atleta in atletas:
        an = int(atleta["anio"])
        n = str(atleta["nombre"])
        m = str(atleta["medalla"])
        if an >= anio_inicio and an <= anio_final and n == nom_interes and m != "na":
            dic = {}
            e = str(atleta["evento"])
            a = str(atleta["anio"])
            m = str(atleta["medalla"])
            dic["evento"] = e
            dic["anio"] = a
            dic["medalla"] = m
            rta.append(dic)
    return rta

def funcion_4(atletas:list,pais_interes:str)->list:
    rta= []
    for atleta in atletas:
        p = str(atleta["pais"])
        if p == pais_interes:
            dic= {}
            dic["nombre"]= str(atleta["nombre"])
            dic["evento"]= str(atleta["evento"])
            dic["anio"]= str(atleta["anio"])
            rta.append(dic)
            
    return rta

def funcion_5(atletas:list)-> dict:
    dic={}
    
    for atleta in atletas:
        lista = []
        p = str(atleta["pais"])
        m = str(atleta["medalla"])
        n= str(atleta["nombre"])
        if p not in dic and m != "na":
            lista.append(n)
            dic[p]= lista
        elif p in dic and m != "na" and n not in dic[p]:
            dic[p].append(n)
    
    
    for i in dic:
        dic[i] =len(dic[i])
    lista1= []   
    for i in dic:
        lista1.append(dic[i])
    maximo = max(lista1)
    
    for llave in dic:
        num = int(dic[llave])
        if maximo == num:
            pa = str(llave)
    rta ={pa:maximo}
    return rta
        
def funcion_6(atletas:list, evento_in:str)-> list:
    rta= []
    for atleta in atletas:
        e = str(atleta["evento"])
        m = str(atleta["medalla"])
        if e == evento_in and m != "na":
            n = str(atleta["nombre"])
            if n not in rta:
                rta.append(n)
            else:
                None
            
    return rta

def funcion_7(atletas: list,minimo:int)->dict:
    dic ={}
    for atleta in atletas:
        m = str(atleta["medalla"])
        n = str(atleta["nombre"])
        if n not in dic and m != "na":
            dic[n]= 1
        elif n in dic and m != "na":
            dic[n]+= 1
    rta = {}
    for llave in dic :
        cifra = int(dic[llave])
        if llave not in rta and  cifra > minimo:
            valor = int(dic[llave])
            rta[llave] = valor
            
    return rta
            
            
    
def funcion_8 (atletas:list)-> str:
    dic =funcion_7(atletas,0)
    lista =[]    
    for i in dic:
        lista.append(dic[i])
    maximo = max(lista)   
    rta = {}
    for nombre in dic:
        num = int(dic[nombre]) 
        if num == maximo:
            
            rta[nombre] = maximo
            
    return rta
        
    
    funcion_9(atletas,"basketball men's basketball")
    
def funcion_9(atletas:list,evento:str)->dict:
    mejores_paises = {}
    for atleta in atletas:
        if atleta["pais"] not in mejores_paises.keys() and atleta["medalla"] != "na" and atleta["evento"] == evento:
            mejores_paises[atleta["pais"]] = [0,0,0]
            if atleta["medalla"] == "gold":
                mejores_paises[atleta["pais"]][0] += 1
            elif atleta["medalla"] == "silver":
                mejores_paises[atleta["pais"]][1] += 1
            else:
                mejores_paises[atleta["pais"]][2] += 1
        elif atleta["pais"] in mejores_paises.keys():
            if atleta["medalla"] != "na":
                if atleta["medalla"] == "gold":
                    mejores_paises[atleta["pais"]][0] += 1
                elif atleta["medalla"] == "silver":
                    mejores_paises[atleta["pais"]][1] += 1
                else:
                    mejores_paises[atleta["pais"]][2] += 1
    mayor = []
    for pais in mejores_paises:
        if mejores_paises[pais] > mayor:
            mayor = mejores_paises[pais]
            pais_mejor_rendimiento = pais
    rta ={pais_mejor_rendimiento:mayor}
    return rta
        
def funcion_11(atletas:list,pais:str,genero:str)-> dict:
     rta = {}
     for atleta in atletas:
         p = str(atleta["pais"])
         g = str(atleta["genero"])
         m = str(atleta["medalla"])
         a = int(atleta["anio"])
         e = str(atleta["evento"])
         n = str(atleta["nombre"])
         if p == pais and g == genero and m != "na" and n not in rta: 
             dic = {}
             lista= []
             dic["evento"] = e
             dic["anio"] = a
             dic["medalla"] = m
             lista.append(dic)
             rta[n] = lista
         if p == pais and g == genero and m != "na" and n in rta:  
             dic = {}
             dic["evento"] = e
             dic["anio"] = a
             dic["medalla"] = m
             rta[n].append(dic)
     return rta 

def funcion_12(atletas:list)->int:
    t={}
    for atleta in atletas:
        n= atleta["nombre"]
        if n not in t:
            t[n]=1
        else:
            t[n]+=1
    todos = len(t)        
    parcial=len(funcion_7(atletas,0))
    rta= parcial/todos
    return round (rta,2)

         
    
  

    
    
    
    
    
    
    
    
    