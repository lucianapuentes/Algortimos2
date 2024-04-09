#Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y 
#un entero n y devuelve True si existen en A un par de elementos que sumados den n. 
#Analice el costo computacional.
def ContieneSuma(A,n):
  if A==None or n==None:
    return 
  else:
    A.sort()
    posmax=len(A)-1
    posmin=0
    max=A(posmax)
    min=A(0)
    return calculatesum(A,n,max,min,posmax,posmin)
  
  
def calculatesum(A,n,max,min,posmax,posmin):
  sum=min+max
  if sum==n:
    return True
  elif posmax==posmin:
    return False
  elif sum>n:
    posmax=posmax-1
    max=A(posmax)
    return calculatesum(A,n,max,min,posmax,posmin)
  else:
    posmin=posmin+1
    min=A(posmin)
    return calculatesum(A,n,max,min,posmax,posmin)
#Implementar un algoritmo que ordene una lista de elementos de acuerdo al siguiente criterio: 
#siempre el elemento del medio de la lista contiene antes que él en la lista la mitad de los elementos 
#menores que él. 
#Explique la estrategia de ordenación utilizada.
from random import randint
import math
def ordenar(lista):
    posmedio=math.trunc(len(lista)/2)
    medio=lista[posmedio]
    menores=0
    posmenoresant=list()
    posmayoresant=list()
    posmenoresdsp=list()
    posmayoresdsp=list()
    menoresant=0
    for i in range(0,len(lista)):
        if i<posmedio:
            if lista[i]<medio:
                posmenoresant.append(i)
                menores=menores+1
                menoresant=menoresant+1
            else:
                posmayoresant.append(i)
        elif i>posmedio:
            if lista[i]<medio:
                menores=menores+1
                posmenoresdsp.append(i)
            else:
                posmayoresdsp.append(i)
    if menoresant==math.trunc(menores/2):
        print("ya estaba ordenado")
        return lista
    elif menoresant<math.trunc(menores/2):
        while menoresant<math.trunc(menores/2):
            if len(posmayoresant)==0 or len(posmenoresdsp)==0:
                print("no es posible ordenar. caso 1")
                return lista
            swap(lista,posmenoresdsp[0],posmayoresant[0])
            posmayoresant.remove(posmayoresant[0])
            posmenoresdsp.remove(posmenoresdsp[0])
            menoresant=menoresant+1
        print("fue ordenado. caso 1")
        return lista
    else:
        while menoresant>math.trunc(menores/2):
            if len(posmayoresdsp)==0 or len(posmenoresant)==0:
                print("no es posible ordenar. caso 2")
                return lista
            swap(lista,posmenoresant[0],posmayoresdsp[0])
            posmayoresdsp.remove(posmayoresdsp[0])
            posmenoresant.remove(posmenoresant[0])
            menoresant=menoresant-1
        print("fue ordenado. caso 2")
        return lista  

def swap(lista, indice1, indice2):
    temp=lista[indice1]
    lista[indice1]=lista[indice2]
    lista[indice2]=temp

