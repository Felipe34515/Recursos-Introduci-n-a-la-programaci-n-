def calcular_precio_pasaje(temporada, compania, edad, estudiante):
    taf = 5000000
    descu = 1
    seguro = 0

    if compania == "ALAS" and temporada == "ALTA":
        descu += 0.3
    elif compania == "VOLAR" and temporada == "ALTA":
        descu += 0.2

    if edad < 18:
        descu -= 0.5
    elif edad > 60 and compania == "VOLAR":
        seguro = 100000

    if compania == "ALAS" and edad > 18 and temporada == "BAJA" and estudiante == True:
        descu -= 0.1
    return (taf *descu) + seguro

# a = calcular_precio_pasaje("ALTA", "ALAS", 42, True) #6500000.0
# b = calcular_precio_pasaje("ALTA", "ALAS", 8, True) #4000000.0
# c = calcular_precio_pasaje("ALTA", "VOLAR", 80, False) #6100000.0
# d = calcular_precio_pasaje("ALTA", "ALAS", 22, True) #6500000.0

# print(a,b,c,d)


#recursivo
def ConejosR (n):
    if n == 0 or n == 1:
        return 1
    else:
        return ConejosR(n-1) + ConejosR(n-2)
    
#DP
l = [1,1]
def conejosDP(n):
    if n== 0:
        return 1
    if n == 1:
        return 1
    for i in range(2, n+1):
        l.append(l[i-1]+ l[i-2])  
    return l[-1], l

# print(ConejosR(20))
# print(conejosDP(20))


SubM = [[0,1,1,0,1,0],
        [0,1,1,1,0,1],
        [1,1,1,1,1,1],
        [1,1,1,0,0,1],
        [1,1,1,1,1,1]]


def SubMatriz(a, b, m):
    f = [[-1 for i in range(b+1)] for i in range(0,a+1)]
    r = 0
    
    for i in range(b):
        for j in range(a):
            if m[i][j] == 0:
                f[i][j] = 0
            elif m[i][j] == 1 and (i == 0 or j == 0):
                f[i][j] = 1
            elif m[i][j] == 1 and (i > 0 or j == 0):
                f[i][j] = min(f[i-1][j], f[i-1][j-1], f[i][j-1])
            #busca y actualiza filas
            if f[i][j] > r:
                r = f[i][j]
    return r, f
        
print(SubMatriz(len(SubM)-1, len(SubM[0])-1, SubM))
    
    

