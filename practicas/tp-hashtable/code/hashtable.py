#insert(D, key, value)
#Descripción: Inserta un key en una posición determinada por la función de hash (1) 
# en el diccionario (dictionary). Resolver colisiones por encadenamiento. 
#En caso de keys duplicados se anexan a la lista.
#Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar. 
#Salida: Devuelve D
import math
class hashnode:
    value=None
    key=None
def hashmod(key,m):
    return key%m

def insert(D,key,value):
    newnode=hashnode()
    newnode.key=key
    newnode.value=value
    if key==None or value==None or D==None:
        return None
    else:
        index=hashmod(key,len(D))
        if D[index]==None:
            D[index]=newnode
        else:
            #colision
            if type(D[index])!=list:
                generateList(D,index)
            D[index].append(newnode)
    return D
           
def generateList(D,index):
    newlist=list()
    node=hashnode()
    node.key=D[index].key
    node.value=D[index].value
    newlist.append(node)
    D[index]=newlist
    return
def printHashTable(D):
    if D==None:
        return None
    for i in range(0,len(D)):
        node=D[i]
        if node!=None:
            if type(node)==list:
                for j in range(0,len(node)):
                    if node[j]!=None:
                        print("index: ", i,"key:",node[j].key,"value:",node[j].value)
            else:
                print("index:", i,"key:",node.key,"value:",node.value)

#D=list()
#D=[None]*15
#insert(D,90,"A")
#insert(D,91,"B")
#printHashTable(D)

#search(D,key)
#Descripción: Busca un key en el diccionario
#Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
#Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
def search(D,key):
    if D==None or key==None:
        return None
    else:
        index=hashmod(key,len(D))
        if D[index]==None:
            return None
        if type(D[index])!=list:
            return D[index].value
        else:
            L=D[index]
            for i in range(0,len(L)):
                if L[i].key==key:
                    return L[i].value
            return None
#D=list()
#D=[None]*15
#insert(D,90,"A")
#insert(D,105,"B")
#print(search(D,1))
#delete(D,key)
#Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
#Poscondición: Se debe marcar como None  el key a eliminar.  
#Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
#Salida: Devuelve D
def delete(D,key):
    if D==None or key==None or search(D,key)==None:
        return None
    else:
        index=hashmod(key,len(D))
        if type(D[index])!=list:
            D[index].value=None
            D[index].key=None
            D[index]=None
        else:
            L=D[index]
            for i in range(0,len(L)):
                if L[i].key==key:
                    L[i].value=None
                    L[i].key=None
                    L[i]=None
        return D
#D=list()
#D=[None]*15
#insert(D,90,"A")
#insert(D,105,"B")
#delete(D,90)
#printHashTable(D)

#Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: 
#dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a
# una permutación de s1...sk. Justificar el costo en tiempo de la solución propuesta.
def IsPermutation(s,p):
    if len(s)!=len(p):
        return False
    else:
        S=list()
        P=list()
        S=[None]*(ord("z")-ord("a"))
        P=[None]*(ord("z")-ord("a"))
        S_index=list()
        P_index=list()
        for i in range(0,len(s)):
            skey=ord(s[i])-ord("a")
            insert(S,skey,s[i])
            S_index.append(hashmod(skey,len(S)))
            pkey=ord(p[i])-ord("a")
            insert(P,pkey,p[i])
            P_index.append(hashmod(pkey,len(P)))
        if len(S_index)!=len(P_index):
            return False
        for k in range(0,len(S_index)):
            if S_index.count(S_index[k])!=P_index.count(S_index[k]):
                return False
        return True
        
#print(IsPermutation("hola","alho"))

#Implemente un algoritmo que devuelva True si la lista que recibe de entrada 
#tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el costo en tiempo de la solución propuesta.
def AreAllElementsUnique(L):
        D=[None]*(ord("z")-ord("0"))
        for i in range(0,len(L)):
            key=ord(chr(L[i]))
            index=hashmod(key,len(D))
            if D[index]!=None:
                return False
            else:
                insert(D,key,L[i])
        return True
            
    
#L=[1,2,5,6]
#print(AreAllElementsUnique(L))

#Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. 
#Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. 
#Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.
#D=hash con provincias, len=ord("z")-ord("a")
#F=hash con cada area
def insertpostal(D,postal):
    node=hashnode()
    provincia=postal[0]
    area=int(postal[1:4])
    manzana=postal[5:7]
    d_index=ord(provincia)
    A=((5^0.5)-1)/2
    f_index=math.floor(162*((area*A)%1))
    node.key=area
    node.value=manzana
    if D[d_index]==None:
        F=[None]*162 #162 es la provincia con mayor cantidad de localidades 
        F[f_index]=node
    else:
        F=D[d_index]
        if F[f_index]!=None:
            if type(F(f_index))==list:
                F[f_index].append(node)
            else:
                L=list()
                L.append(F[f_index])
        else:
            L=[]
        L.append(node)
        F[f_index]=L

def searchpostalcode(D,postal):
    provincia=postal[0]
    area=int(postal[1:4])
    manzana=postal[5:7]
    d_index=ord(provincia)
    A=((5^0.5)-1)/2
    f_index=math.floor(162*((area*A)%1))
    if D[d_index]==None:
        return False
    else:
        F=D[d_index]
        if F[f_index]==None:
            return False
        else:
            if type(F[f_index])==list:
                L=F[f_index]
                for i in range(0,len(L)):
                    Fnode=L[i]
                    if Fnode.key==area and Fnode.value==manzana:
                        return True
                return False
            else:
                if F[f_index].key==area and F[f_index].value==manzana:
                    return True
                else:
                    return False




        