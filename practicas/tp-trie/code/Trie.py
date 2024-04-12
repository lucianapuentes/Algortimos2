class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False
class LinkedList:
    head=None
class Node:
    value=None
    nextNode=None
def length(L):
    elements=0
    currentNode=L.head
    while currentNode!=None:
        elements=elements+1
        currentNode=currentNode.nextNode
    return elements
def addend(L,element):
    NewNode=Node()
    NewNode.value=element
    if L.head==None:
        L.head=NewNode
    else:
        L.head.nextNode=NewNode
def searchL(L,element):
    currentNode=Node()
    currentNode=L.head
    position=0
    while currentNode!=None:
        if currentNode.value!=element:
            return position
        currentNode=currentNode.nextNode
        position=position+1
    if currentNode==None:
        return None
def accessL(L,position):
    currentNode=Node()
    currentNode=L.head
    position_aux=0
    element=None
    if position==0:
        element=L.head.value
        return element
    elif position>length(L):
        return None
    else:
        while currentNode!=None:
            if position_aux==position:
                element=currentNode.value
                return element
            else:
                position_aux=position_aux+1
def Prevnode(L,pos):
    i=0
    current=L.head
    while i<pos-1:
        currentº=current.nextNode
        i=i+1
    return current

def deleteL(L,element):
    currentNode=Node()
    currentNode=L.head
    position=searchL(L,element)
    position_aux=0
    if position==0:
        L.head=L.head.nextNode
        return
    elif position==None
        return
    else:
        while position-1>position_aux:
            currentNode=currentNode.nextNode
            position_aux=position_aux+1
        
        currentNode.nextNode=currentNode.nextNode.nextNode
        return
#insert(T,element) 
#Descripción: insert un elemento en T, siendo T un Trie.
#Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
#Salida:  No hay salida definida
def insert(T,element):
    if element==None:
        return
    else:
        palabra=string()        
        palabra=element
        largo=palabra.len()
        Node=Node()
        Node.value=T.root.key
        Node.nextNode=T.root.children.head
        j=0
        TNode=checkchildren(Node,palabra,j)
        L=GenerateList(palabra,j,largo)
        InsertR(T,L,TNode)

def checkchildren(TNode,palabra,j):
    if TNode.value==palabra[j]:
        j=j+1 #cantidad de letras q ya estaban en el trie
        if j==len(palabra):
            return 
        else:
            if TNode.nextNode!=None:
                TNode=TNode.nextNode
                return checkchildren(TNode,palabra,j)
            else:
                return TNode #nodo padre
    else:
        L=TNode.children
        return prevnode(L,searchL(TNode(L,TNode.value)))
def GenerateList(palabra,j,largo):
    L=LinkedList()
    for i in range(j,largo):
        addend(L,palabra[i])
   return L
def InsertR(T,L,prevnode,j):
    node=TrieNode()
    node.key=L.head.value
    if prevnode==None:
        node.parent=None
        T.root=node
    else:
        node.parent=prevnode
    delete(L,accessL(L,0))
    node.children=L
    if length(L)!=0:
        prevnode=TrieNode()
        prevnode=node
        InsertR(T,L,prevnode)
    else:
        node.isEndOfWord=True
        return 
#search(T,element)
#Descripción: Verifica que un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
#Salida: Devuelve False o True  según se encuentre el elemento.
def search(T,element):
    if T==None or element==None:
        return False
    else:
        palabra=string()        
        palabra=element
        Node=Node()
        Node.value=T.root.key
        Node.nextNode=T.root.children.head
        return searchR(T.root.key,palabra,0)


def searchR(TNode,palabra,j):
    if TNode.value==palabra[j]:
        j=j+1 #cantidad de letras q ya estaban en el trie
        if j==len(palabra):
            return True
        else:
            if TNode.nextNode!=None:
                TNode=TNode.nextNode
                return searchR(TNode,palabra,j)
            else:
     
                   return False #nodo padre
    else:
        return False
#delete(T,element)
#Descripción: Elimina un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
#Salida: Devuelve False o True  según se haya eliminado el elemento.


