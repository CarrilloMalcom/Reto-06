def promedio(a:float, b:float, c:float, d:float, e:float)->float:
    return (a+b+c+d+e)/5

def promedio_multiplicativo(a:float, b:float, c:float, d:float, e:float)->float:
    return (a*b*c*d*e)**0.5

def orden_ascendente(a:float, b:float, c:float, d:float, e:float):
    numeros=[a, b, c, d, e]
    for i in range(len(numeros)):
        menor = i
        for j in range(i+1, len(numeros)):
            if numeros[j] < numeros[menor]:
                menor = j
        numeros[i], numeros[menor] = numeros[menor], numeros[i]
    return numeros

def orden_descendente(a:float, b:float, c:float, d:float, e:float):
    numeros=[a, b, c, d, e]
    for i in range(len(numeros)):
        mayor = i
        for j in range(i+1, len(numeros)):
            if numeros[j] > numeros[mayor]:
                mayor = j
        numeros[i], numeros[mayor] = numeros[mayor], numeros[i]
    return numeros

def mediana(a:float, b:float, c:float, d:float, e:float):
    numeros=orden_ascendente(a, b, c, d, e)
    return numeros[2]

def potencia_mayor_al_menor(a:float, b:float, c:float, d:float, e:float):
    asc=orden_ascendente(a, b, c, d, e)
    return asc[4]**asc[0]

def raiz_del_menor(a:float, b:float, c:float, d:float, e:float):
    numeros=orden_descendente(a, b, c, d, e)
    return numeros[4]**(1/3)
