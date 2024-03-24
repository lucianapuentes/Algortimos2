

class AVLTree:
  root = None

class AVLNode:
        parent = None
        leftnode = None
        rightnode = None
        key = None
        value = None
        bf = None
def print_tree(root, level=0, prefix="Root: "):
  if root is not None:
      print(" " * (level * 4) + prefix + str(root.value))
      if root.leftnode is not None or root.rightnode is not None:
          print_tree(root.leftnode, level + 1, "L-- ")
          print_tree(root.rightnode, level + 1, "R-- ")
def height(node):
  if node == None:
      return 0
  else:
     left = height(node.leftnode)
     right = height(node.rightnode)
  return max(left, right) + 1

def max(num1,num2):
  if num1>num2:
    return num1
  else: 
    return num2
def balancedtree(B,node,balance):
  if B.root==None or node==None:
      return 
  else:
      if abs(node.bf)>1:
          #print("No es un arbol balanceado")
          balance=False
          return balance
      else:
          #print("Es un arbol balanceado")
          if node.rightnode!=None:
            balancedtree(B,node.rightnode,balance)
          if node.leftnode!=None:
            balancedtree(B,node.leftnode,balance)
          return balance
  if node==None:
    return
  
def balancefactor(node):
  if node == None:
    return 
  else:
    node.bf= height(node.leftnode) - height(node.rightnode)
    #print("El balance factor de ",node.value," es: ",node.bf)
    return
#rotateLeft(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la izquierda 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
#Salida: retorna la nueva raíz


def rotateLeft(Tree,avlnode):
  newRoot=AVLNode()
  newRoot=avlnode.rightnode
  avlnode.rightnode=newRoot.leftnode
  if newRoot.leftnode!=None:
    newRoot.leftnode.parent=avlnode
  newRoot.parent=avlnode.parent
  if avlnode.parent==None:
    Tree.root=newRoot
  else:
    if avlnode.parent.leftnode==avlnode:
      avlnode.parent.leftnode=newRoot
    else:
      avlnode.parent.rightnode=newRoot
  newRoot.leftnode=avlnode
  avlnode.parent=newRoot
  #print("NewRoot=", newRoot.value)
  return newRoot
#rotateRight(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la derecha 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
#Salida: retorna la nueva raíz
def rotateRight(Tree,avlnode):
  newRoot=AVLNode()
  newRoot=avlnode.leftnode
  avlnode.leftnode=newRoot.rightnode
  if newRoot.rightnode!=None:
    newRoot.rightnode.parent=avlnode
  newRoot.parent=avlnode.parent
  if avlnode.parent==None:
    Tree.root=newRoot
  else:
    if avlnode.parent.rightnode==avlnode:
      avlnode.parent.rightnode=newRoot
    else:
      avlnode.parent.leftnode=newRoot
  newRoot.rightnode=avlnode
  avlnode.parent=newRoot
  #print("NewRoot=", newRoot.value)
  return newRoot
#calculateBalance(AVLTree) 
#Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
#Entrada: El árbol AVL  sobre el cual se quiere operar.
#Salida: El árbol AVL con el valor de balanceFactor para cada subarbol
def calculateBalance(AVLTree):
  if AVLTree.root==None:
    return 
  else:
    calculateBalanceR(AVLTree.root)

def calculateBalanceR(node):
  if node==None:
    return
  else:
    calculateBalanceR(node.leftnode)
    calculateBalanceR(node.rightnode)
    balancefactor(node)
    return
#reBalance(AVLTree) 
#Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
#Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
#Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.
def reBalance(AVLTree):
  if AVLTree.root==None:
    return 
  else:
    reBalanceR(AVLTree,AVLTree.root)
    
def reBalanceR(AVLTree,node):
  rotNode=AVLNode()
  if AVLTree==None or node==None:
    return
  elif abs(node.bf)<=1:
    #print("Nodo balanceado")
    if node.rightnode!=None:
      reBalanceR(AVLTree,node.rightnode)
    if node.leftnode!=None:
      reBalanceR(AVLTree,node.leftnode)
  elif node.bf<-1:
      #print("Inclinacion a la derecha")
      if node.rightnode.bf>1:
        rotateRight(AVLTree,node.rightnode)
       
      rotNode=rotateLeft(AVLTree,node)
      
  elif node.bf>1:
    #print("Inclinacion a la izquierda")
    if node.leftnode.bf<-1:
      rotateLeft(AVLTree,node.leftnode)
    
    rotNode=rotateRight(AVLTree,node)
  #print("RotNode=",rotNode.value)
  calculateBalanceR(rotNode)
  balancefactor(rotNode.parent)
  if balancedtree(AVLTree,AVLTree.root,True)==False:
    reBalanceR(AVLTree,AVLTree.root)
  return
#insert(AVLTree,node)
def insert(AVLTree,node):
  if AVLTree.root==None:
    AVLTree.root=node
    node.parent=None
    node.bf=0
    return
  else:
    insertR(AVLTree,AVLTree.root,node)
def insertR(AVLTree,AVLnode,newnode):
  if newnode==None or AVLnode==None or AVLTree==None:
    return
  if newnode.key<AVLnode.key:
    if AVLnode.leftnode==None:
      AVLnode.leftnode=newnode
      newnode.parent=AVLnode
      newnode.bf=0
      reBalanceR(AVLTree,AVLnode)
      balancefactor(AVLTree.root)
      return
    else:
      insertR(AVLTree,AVLnode.leftnode,newnode)
  elif newnode.key>AVLnode.key:
    if AVLnode.rightnode==None:
      AVLnode.rightnode=newnode
      newnode.parent=AVLnode
      newnode.bf=0
      reBalanceR(AVLTree,AVLnode)
      balancefactor(AVLTree.root)
      return
    else:
      insertR(AVLTree,AVLnode.rightnode,newnode)
  else:
    return
#delete(AVLTree,node)
def delete(AVLTree,node):
  if node==AVLTree.root:
    deleteroot(AVLTree,AVLTree.root)
    return
  else:
    deleteR(node)
def deleteR(node):
  right=AVLNode()
  left=AVLNode()
  parent=AVLNode()
  right=node.rightnode
  left=node.leftnode
  parent=node.parent
  if node==None:
    return
  
  elif parent.leftnode==node:
      if left==None and right==None:
        parent.leftnode=None
        node.parent=None
        reBalance(AVLTree)
        
      elif left==None and right!=None:
        parent.leftnode=right
        right.parent=parent
        reBalanceR(AVLTree,right)
        balancefactor(parent)
        
      elif left!=None and right==None:
        parent.leftnode=left
        node.leftnode.parent=parent
        reBalanceR(AVLTree,left)
        balancefactor(parent)
        
      else:
        findSucesor(node)
        reBalance(AVLTree)
  elif parent.rightnode==node:
      if left==None and right==None:
        parent.rightnode=None
        node.parent=None
        reBalance(AVLTree)
        
      elif left==None and right!=None:
        parent.rightnode=right
        right.parent=parent
        reBalanceR(AVLTree,right)
        balancefactor(parent)
        
      elif left!=None and right==None:
        parent.rightnode=left
        node.leftnode.parent=parent
        reBalanceR(AVLTree,left)
        balancefactor(parent)
      else: 
        findSucesor(node)
        reBalance(AVLTree)
  
  node.rightnode=None
  node.leftnode=None
  return
def deleteroot(B,node):
  if hasleft(node) and hasright(node):
    sucesor = SmallerOf(node.rightnode)
    key = node.key
    node.key = sucesor.key
    parent_nodo = sucesor.parent
    if parent_nodo.leftnode == sucesor:
        parent_nodo.leftnode = None
    elif parent_nodo.rightnode == sucesor:
        parent_nodo.rightnode = None
    sucesor.rightnode = node.rightnode
    sucesor.leftnode = node.leftnode
    B.root = sucesor
    return key
  else:
    if hasleft(node):
      B.root = node.leftnode
      node.leftnode.parent=None
    elif hasright(node):
      B.root = node.rightnode
      node.rightnode.parent=None
    else:
      B.root = None
    return
def hasright(node):
  right = AVLNode()
  right = node.rightnode
  if right != None:
    return True
  else:
    return False


def hasleft(node):
  left = AVLNode()
  left = node.leftnode
  if left != None:
    return True
  else:
    return False



def findSucesor(node):
  parent=AVLNode()
  parent=node.parent
  if hasleft(node) and hasright(node) and parent!=None:
    sucesor=AVLNode()
    origparent=AVLNode()
    sucesor=SmallerOf(node.leftnode)
    node.key=sucesor.key
    origparent=sucesor.parent
    if parent.rightnode==node:
      parent.rightnode=sucesor
    else:
      parent.leftnode=sucesor
    if origparent.leftnode==sucesor:
      origparent.leftnode=None
    elif origparent.rightnode==sucesor:
      origparent.rightnode=None
    sucesor.rightnode=node.rightnode
    sucesor.leftnode=node.leftnode
    return 

def SmallerOf(node):
  if node.leftnode != None:
    changeNode = SmallerOf(node.leftnode)
    if changeNode != None:
      return changeNode
  elif node.rightnode != None:
    changeNode = SmallerOf(node.rightnode)
    if changeNode != None:
      return changeNode
  else:
    return node