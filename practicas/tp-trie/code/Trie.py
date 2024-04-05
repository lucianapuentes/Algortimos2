class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False
class queue.Queue(maxsize=0)
#insert(T,element) 
#Descripción: insert un elemento en T, siendo T un Trie.
#Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
#Salida:  No hay salida definida
def insert(T,element):
    if element==None:
        return
    else
        GenerateQueue(element)
        if T.root==None:
            InsertT(T,Q,element,None)
def GenerateQueue(element)
    Q.Queue(0)
    for i in range(0,len(element)):
        Q.Queue.put(element(i)) 
def InsertT(T,Q,element,Prev):
    node=TrieNode()
    if Q.Queue.qsize!=0:
        newNode.key=Q.Queue.get()
        newNode.parent=Prev
        newNode.children=Q
        newNode.isEndOfWord=False
        InsertT(T,Q,element,newNode):
    else:
        newNode.key=Q.Queue.get()
        newNode.parent=Prev
        newNode.children=None
        newNode.isEndOfWord=True