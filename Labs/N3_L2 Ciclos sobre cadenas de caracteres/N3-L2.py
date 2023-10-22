a = "cabello"
b = "bello"
c = "xxxxxyyyyy"
d = "Hola qué tal"

def encontrarSubcadena (cadena: str, subcadena: str):
    rta = False
    if cadena.find(subcadena) != -1:
        rta = True
    return rta

def encontrarSubcadena1 (cadena: str, subcadena: str):
    rta = False
    i = 0
    j = 0
    while ( i < len(cadena) and rta == False):
        if cadena[i] == subcadena[j]:
            j += 1
        if j == len(subcadena):
            rta = True
        i += 1
    return rta

def invertirSucadena1 (cadena : str):
    rta = cadena[::-1]
    return rta

def invertirSucadena2 (cadena : str):
    rta = ""
    i = len(cadena)-1
    while (i >= 0):
        rta = rta + cadena[i]
        i -= 1
    return rta

def eliminarDuplicados(cadena: str):
    rta = ""
    i = 0
    while (i < len(cadena)):
        if rta.find(cadena[i]) == -1:
            rta = rta + cadena[i]
        i += 1
    return rta

def conteoCaracteres(cadena: str):
    rta = {}
    i = 0
    while (i < len(cadena)):
        rta[cadena[i]] = i
        i += 1
    return rta

def conteoPalabras(cadena: str):
    rta = 0
    i = 0
    while (i < len(cadena)):
        if cadena[i] == " " and i != len(cadena):
            rta += 1
        i += 1
    return rta

def conteo_de_palabrasVersionPro (cadena: str)-> int:
    respu=1
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    
    for i in range(len(cadena)):
        palabra = False
        if cadena[i]==" ":
            if i != 0:
                if (cadena[i-1] in abecedario):
                   palabra = True    
            elif i != len(cadena)-1:
                if (cadena[i+1] in abecedario):
                    palabra = True  
        if palabra:
            respu += 1
    if cadena == "":
        respu = 0
    return  respu
   
# print(encontrarSubcadena(a, b))
#print(encontrarSubcadena1(a, b))
# print(invertirSucadena1(a))
# print(invertirSucadena2(a))
# print(eliminarDuplicados(c))
# print(conteoCaracteres(a))
# print(conteoPalabras(d))
# print(conteo_de_palabrasVersionPro(a))