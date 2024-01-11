#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 07:00:27 2023

@author: mac
"""

def leer_archivo( nombre_archivo:str )-> list:
    archivo = open( nombre_archivo, "r", encoding='utf8' );
    linea = archivo.readline();
    linea = archivo.readline();
    contratos = []
    i = 0
    while linea != "":
        scontrato = linea.split(";");
        
        plataforma = scontrato[0];
        nombre_entidad = scontrato[1];
        nit_entidad = scontrato[2];
        id_contrato = scontrato[3];
        documento_proveedor = scontrato[4];
        nombre_proveedor = scontrato[5];
        valor_proveedor = scontrato[6];
        fecha_contrato = scontrato[7];
        contrato = {
                        "plataforma":plataforma, 
                        "nombre_entidad": nombre_entidad,
                        "nit_entidad":nit_entidad,
                        "id_contrato":id_contrato,
                        "documento_proveedor":documento_proveedor,
                        "nombre_proveedor": nombre_proveedor,
                        "valor": float(valor_proveedor),
                        "fecha_contrato":fecha_contrato
                    }
        contratos.append( contrato )
        linea = archivo.readline();

    archivo.close();
    
    return contratos;

x = (leer_archivo("MuestreoContrato.csv"))


def buscar_contrato_por_identificador(contratos, identificador_contrato ):
    tamnio = len(contratos)
    rta = "No hay contrato con eso ID"
    contador = 0
    while (contador < tamnio ):
        lista = contratos
        elemento = contratos[contador]
        ID = contratos[contador]["id_contrato"]
        if contratos[contador]["id_contrato"] == identificador_contrato:
            rta = contratos[contador]
        contador +=1
    return rta
        
           
print(buscar_contrato_por_identificador(x, 'CO1.PCCNTR.4354117'))


def sumatoria_contratos_mes( contratos, numero_mes):
    tamnio= len(contratos) #concoer las iteraciones dle While
    contador = 0
    rta = 0
    while (contador < tamnio):
        fecha = contratos[contador]["fecha_contrato"]
        fecha = fecha.split("/")
        if fecha[1] == numero_mes:
            rta += contratos[contador]["valor"]
            rta += 1
        contador+=1
    return rta

    
# print(sumatoria_contratos_mes(x, "08"))

def cantidad_contratos_mes (contratos, numero_mes):
    tamanio = len (contratos)
    contador = 0
    rta = 0
    while (contador < tamanio):
        fecha = contratos [contador]["fecha_contrato"]
        fecha_lista = fecha.split("/")
        mes = fecha_lista [1]
        if mes == numero_mes :
            rta +=1
        contador += 1
    return rta


# print (cantidad_contratos_mes(x,"08"))     

def contrato_mayor_valor (contratos) :
    max = 0
    rta = {}
    for contrato in contratos:
        if contrato["valor"]> max:
            max = contrato["valor"]
    for contrato in contratos:
        if contrato["valor"]== max:
            rta = contrato
    return rta
        

# print(contrato_mayor_valor(x))   

# Diccionario principal con diccionarios anidados
empleados = {
    '001': {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 30,
        'puesto': 'Ingeniero'
    },
    '002': {
        'nombre': 'María',
        'apellido': 'González',
        'edad': 28,
        'puesto': 'Diseñador'
    },
    '003': {
        'nombre': 'Carlos',
        'apellido': 'López',
        'edad': 35,
        'puesto': 'Gerente'
    }
}

# Acceder a la información de un empleado específico
# informacion_empleado = empleados['002']
# print("Información del empleado '002':")
# print(informacion_empleado['nombre'])
# print(informacion_empleado['apellido'])
# print(informacion_empleado['edad'])
# print(informacion_empleado['puesto'])

# for i in empleados.keys():
#     print(empleados[i]["edad"])
