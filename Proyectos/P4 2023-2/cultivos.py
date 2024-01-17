"""
Ejercicio nivel 4: Rendimiento de cultivos en Colombia
Modulo de funciones.

@author: Cupi2
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches


def cargar_datos(documento):
    return pd.read_csv(documento)

df = cargar_datos("cultivos.csv")


def requ1 (departamento, df):
    df=df[(df["Departamento"]==departamento)].groupby("Tipo_Cultivo").Toneladas.sum()
    df.plt(kind="pie",  title="Distribución de cultivos en "+str(departamento),autopct='%.1f%%', fontsize=10)
    plt.show()

#req1 = requ1("Vaupes", df )

def requ2(df):
    df = df.groupby(by= "Cultivo").sum()
    df["altura"] = df["Toneladas"]/ df["Hectareas_cosechadas"]
    df = df.sort_values(by = "altura", ascending = False).head(10)
    df.plot(kind="bar", y="altura", title="Top 10 cultivos con mayor cantidad de toneladas cosechadas por hectarea", figsize=(9,5))
    plt.show()

# req2 = requ2( df )

def requ3 (df, minimo, maximo):
    df = df[(df["Toneladas"] >= minimo) & (df["Toneladas"] <= maximo)].copy()
    df.plot(kind="box", column="Toneladas", by="Tipo_Cultivo", vert=False, title="Toneladas por tipo de cultivo", figsize=(9,5))   
    plt.show()
    
requ3(df, 2000, 10000)



#Parte 2
#Requerimiento 4
def crear_matriz(dataframe: pd.DataFrame)->list:
    #Esqueleto diccionarios

    deptos =  sorted(dataframe["Departamento"].unique())
    dept_dict = dict(list(enumerate(deptos)))

    tipos_cultivos =  sorted(dataframe["Tipo_Cultivo"].unique())
    tipos_cultivos_dict = dict(list(enumerate(tipos_cultivos)))
    matriz= []
    
    for dep in deptos:
        fila_temporal= []
        departamentos = dataframe[dataframe["Departamento"] == dep]
        departamentos = departamentos.groupby(by= "Tipo_Cultivo").sum()
        dic_temporal= departamentos.to_dict()["Toneladas"]
        for culti in tipos_cultivos:
            if culti in dic_temporal:
                fila_temporal.append(dic_temporal[culti])
            elif culti not in dic_temporal:
                fila_temporal.append(0)
        matriz.append(fila_temporal)
            
        
    return matriz, tipos_cultivos_dict, dept_dict
    
tupla = crear_matriz(df)

def requ5 (tupla, depto):
    posDepto = 0
    for llave, valor in tupla[2].items():
        if valor  == depto:
            posDepto = llave
    suma = 0
    for i in tupla[0][posDepto]:
        suma += i   
    return suma

#print(requ5(tupla, "Amazonas"))

def requ6(mayor, tupla):
    dept_dict = tupla[2]
    if mayor:
        pico = 0
    else: 
        pico = 100000
    rta_dep =""
    for i in dept_dict.values():
        
        cantidad = requ5(tupla, i )
        if mayor:
            if cantidad > pico:
                pico = cantidad
                rta_dep = i 
        else:
            if cantidad < pico and cantidad != 0:
                pico = cantidad
                rta_dep = i 
    return rta_dep, pico

#print(requ6(True, tupla))


def reque7(tupla, minimo):
    matriz = tupla[0]
    tipos_cultivos_dict = tupla[1]
    dept_dict = tupla[2]
    for fila in range(len(matriz)):
        minimos= 0
        cultivos = []
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna]  > minimo:
                minimos += 1
                cultivos.append(tipos_cultivos_dict[columna])
                if minimos == 3:
                    return {dept_dict[fila]: cultivos}
                
    return {"Ninguno": []}
                
reque7 = reque7(tupla, 29949)

def cargar_coordenadas(nombre_archivo:str)->dict: 
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    titulos = archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos






def requ8 (cultivo, tupla):
    mapa = mpimg.imread("mapa.png").tolist()
    
    ubicacion =  cargar_coordenadas("coordenadas.txt")
    matriz = tupla[0]
    departamentos = tupla[2]
    cultivos = tupla[1]
    pos_culti = 0
    for i in cultivos.keys():
        if cultivos[i] == cultivo:
            pos_culti = i
            
            
    for llave, valor in departamentos.items():
        x = ubicacion[valor][0]
        y = ubicacion[valor][1]
        toneladas = matriz[llave][pos_culti] 
        if toneladas < 10:
            esquinaEnX = x-6
            esquinaEnY = y-6
            for i in range(12):
                for j in range(12):
                    mapa[esquinaEnX+j][esquinaEnY+i] = [0.94, 0.10, 0.10]
        elif toneladas < 100:
            esquinaEnX = x-6
            esquinaEnY = y-6
            for i in range(12):
                for j in range(12):
                    mapa[esquinaEnX+j][esquinaEnY+i] = [0.94, 0.10, 0.85] 
        elif toneladas < 1000:
            esquinaEnX = x-6
            esquinaEnY = y-6
            for i in range(12):
                for j in range(12):
                    mapa[esquinaEnX+j][esquinaEnY+i] = [0.10, 0.50, 0.94]
        elif toneladas < 10000:
            esquinaEnX = x-6
            esquinaEnY = y-6
            for i in range(12):
                for j in range(12):
                    mapa[esquinaEnX+j][esquinaEnY+i] = [0.34, 0.94, 0.10] 
        elif toneladas >= 100000:
            esquinaEnX = x-6
            esquinaEnY = y-6
            for i in range(12):
                for j in range(12):
                    mapa[esquinaEnX+j][esquinaEnY+i] = [0.99, 0.82, 0.09]
            
    colores = {"0 a <10":[0.94, 0.10, 0.10], "10 a <100":[0.94, 0.10, 0.85], "100 a <1000":[0.10, 0.50, 0.94], "1000 a <100000":[0.34, 0.94, 0.10], ">=100000":[0.99, 
    0.82, 0.09]}
    plt.imshow(mapa)
    legends = []
    for i in colores:
        legends.append(mpatches.Patch(color = colores[i], label=i))
    plt.legend(handles = legends, loc = 3, fontsize='x-small')
    plt.title("Producción en toneladas de " + cultivo, fontsize='x-small')
    plt.show()      
    
    
    

# requ8 = requ8("Plantas Aromaticas Condimentarias Y Medicinales", tupla)
            
        
    
    


    
    
    
    
        
        
        
    
    
#m = crear_matriz(df)

    #TODO completar la construcción de la matriz
