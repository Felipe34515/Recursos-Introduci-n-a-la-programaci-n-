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
    encontrado = False
    rta = 0
    for i in cadena:
        if i != " " and encontrado == False:
            encontrado = True
            rta += 1
        elif i == " " and encontrado == True:
            encontrado = False
    return rta
   
# print(encontrarSubcadena(a, b))
#print(encontrarSubcadena1(a, b))
# print(invertirSucadena1(a))
# print(invertirSucadena2(a))
# print(eliminarDuplicados(c))
# print(conteoCaracteres(a))
# print(conteoPalabras(d))