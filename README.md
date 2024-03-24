# Reto-06

## 1. 
### Función para calcular el area superficial y el volumen de una figura consistente de una esfera y un cono

```python
import math
p=math.pi
def calcular_V(r1:float, r2:float, h:float)->float:
    V1=(4/3)*p*(r1**3)
    V2=(1/3)*p*(r2**2)*h
    Vt=V1+V2
    return Vt

def calcular_SA(r1:float, r2:float, h:float)->int:
    A1=4*p*(r1**2)
    g=(h**2)+(r2**2)
    g=g**0.5
    A2=(p*r2*g)+(p*(r2**2))
    At=A1+A2
    return At

if __name__=="__main__":
    r1=float(input("Ingrese el radio de la esfera: "))
    r2=float(input("Ingrese el radio del cono: "))
    h=float(input("Ingrese la altura: "))
    Area=calcular_SA(r1,r2,h)
    Volumen=calcular_V(r1,r2,h)
    print(f"El área superficial del solido es {Area} y el volumen es {Volumen}")

```

## 2.
### Función para calcular el area y el perimetro de una figura consistente de dos circulos iguales y un rectangulo
``` python
import math
p=math.pi
def calcular_A(r:float, b:float, a:float)->float:
    A1=2*(p*(r**2))
    A2=b*a
    At=A1+A2
    return At
def calcular_P(r:float, b:float, a:float)->float:
    P1=2*(2*p*r)
    P2=(2*a)+(2*b)
    Pt=P1+P2
    return Pt

if __name__ =="__main__":
    r=float(input("Ingrese el radio de los circulos: "))
    b=float(input("Ingrese el ancho del rectangulo: "))
    a=float(input("Ingrese la altura del rectangulo: "))
    Ar=calcular_A(r, b, a)
    Per=calcular_P(r,b, a)
    print(f"El area de la figura es {Ar} y el perimetro es {Per}")
```

## 3.
### Función para el calculo de la cantidad de carne de aves en kg
``` python
n:int=1
m:int=7
k:int=6
def carne_de_ave(N:int, M:int, K:int)->int:
    Nkg=N*n
    Mkg=M*m
    Kkg=K*k
    return Nkg+Mkg+Kkg

if __name__=="__main__":
    N=int(input("Ingrese la cantidad de gallinas: "))
    M=int(input("Ingrese la cantidad de gallos: "))
    K=int(input("Ingrese la cantidad de pollitos: "))
    carne=carne_de_ave(N,M,K)
    print(f"La cantidad de carne de aves es igual a {carne} kg")
```
## 4.
### Calcular vueltas o el dinero faltante de una compra de huevos, pan y bolsas de leche, dada la cantidad de cada producto y el dinero con el que se va a comprar
``` python
p:int=300
m:int=3300
h:int=350
def calcular_vueltas(P:int, M:int, H:int, B:int)->int:
    cnta=(P*p)+(M*m)+(H*h)
    return B-cnta

if __name__=="__main__":
    P=int(input("Ingrese la cantidad de panes que le mandaron a comprar: "))
    M=int(input("Ingrese la cantidad de bolsas de leche que le mandaron a comprar: "))
    H=int(input("Ingrese la cantidad de huevos que le mandaron a comprar: "))
    B=int(input("Ingrese la cantidad de dinero que le dieron (Pesos): "))
    Residuo=calcular_vueltas(P,M,H,B)
    if Residuo>0:
        print(f"Las vueltas de su compra son {Residuo} pesos")
    else:
        Residuo=Residuo*(-1)
        print(f"Le hacen falta {Residuo} pesos para su compra")
```

## 5.
### Calculo del valor de un prestamo con interés compuesto
``` python
def calcular_prestamo(C:int,i:int,n:int)->int:
    return C*((1+(i/100))**n)

def calcular_prestalt(C:int,i:int,n:int)->int:
    prest=C
    for j in range(n):
        prest=prest+(prest*(i/100))
    return prest

if __name__=="__main__":
    C=int(input("Ingrese el valor base del prestamo: "))
    i=int(input("Ingrese el valor del interés: "))
    n=int(input("Ingrese la cantidad de meses para el valor del prestamo: "))
    P=calcular_prestamo(C,i,n)
    Palt=calcular_prestalt(C,i,n)
    print(f"El valor del prestamo es {P} \n El valor es {Palt}")
```
## 6.
### Numero de contagiados de COVID-19 de nuncalandia si la cantidad se duplica cada día, dada la cantidad de dias y la cantidad de contagiados inicial
``` python
def numero_contagiados(D:int, C:int)->int:
    cont=C
    for j in range (D):
        cont=cont*2
    return cont

if __name__ =="__main__":
    C=int(input("Ingrese el numero actual de contagiados: "))
    D=int(input("Ingrese el numero de dias para la predicción de contagiados: "))
    cont=numero_contagiados(D, C)
    print(f"El numero de contagiados dentro de {D} dias si el numero actual son {C} contagiados serán {cont}")
```
## 7.
### Funciones matematicas para promedio, promedio multiplicativo, orden ascendente, orden descendente, mediana, raiz del numero menor, y potencia del numero mayor elevado al menor entre 5 numeros dados
``` python
from Funciones_reto06 import promedio, promedio_multiplicativo, potencia_mayor_al_menor, orden_ascendente, orden_descendente, mediana, raiz_del_menor


if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    promed=promedio(a,b,c,d,e)
    median=mediana(a,b,c,d,e)
    promultip=promedio_multiplicativo(a,b,c,d,e)
    asc=orden_ascendente(a,b,c,d,e)
    desc=orden_descendente(a,b,c,d,e)
    potencia=potencia_mayor_al_menor(a,b,c,d,e)
    raiz=raiz_del_menor(a,b,c,d,e)

    print(f"El promedio de los numeros es {promed}")
    print(f"La mediana de los numeros es {median}")
    print(f"El promedio multiplicativo de los numeros es {promultip}")
    print(f"El orden ascendente de los numeros es {asc}")
    print(f"El orden descendente de los numeros es {desc}")
    print(f"La potencia del numero mayor elevado al menor de los numeros es {potencia}")
    print(f"La raiz cubica del numero menor es {raiz}")

```
>Las funciones se encuentran en un archivo aparte y se importan a este


## pip
pip es un administrador de paquetes de python que viene ya incluido por defecto con python desde la versión 3.4. Este administrador de paquetes nos deja a través de la linea de comando instalar paquetes de python con todas sus funciones que podemos utilizar en nuestros codigos al importar el paquete completo o las funciones que se van a usar del paquete.

```
python -m pip install pandas
```
>Ejemplo de linea de comando para instalación del paquete o libreria pandas

### Lista de paquetes o librerias conocidos o muy usados
-Matplotlib: para crear gráficos
```
python -m pip install -U matplotlib
```
-Tensorflow: construir y entrenar redes neuronales
```
python3 -m pip install tensorflow[and-cuda]
```
-Pytorch: aprendizaje automático
```
python -m pip3 install torch torchvision torchaudio
```
-Pandas: para datos y estadistica
```
python -m pip install pandas
```
-Nummpy: para una estructura de datos universal
```
python -m pip install numpy
```
-Pyautogui: Controla entrada de teclado y mouse por codigo
```
python -m pip install pyautogui
```

### Referencias:
-https://pip.pypa.io/en/latest/installation/
-https://www.w3schools.com/python/python_pip.asp
-https://immune.institute/blog/librerias-python-que-son/
-https://matplotlib.org/stable/users/installing/index.html
-https://www.tensorflow.org/install/pip?hl=es-419
-https://pytorch.org/
-https://pandas.pydata.org/docs/getting_started/install.html
-https://numpy.org/install/
