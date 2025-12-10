from collections import deque
#def createGraph(List, List) 
#Descripción: Implementa la operación crear grafo
#Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos 
#representa una conexión entre dos vértices.
#Salida: retorna el nuevo grafo
def createGraph(vertices,aristas):
    graph=[]
    if vertices==None or aristas==None:
        return
    if len(aristas)==0:
        for i in range(0,len(vertices)):
            graph.append((vertices[i],[]))
    else:
        for i in range(0,len(vertices)):
            vertice=vertices[i]
            listavertice=[]
            for arista in aristas:
                #print("arista",arista)
                if arista[0]==vertice:
                    vert=arista[1]
                    flag=True
                elif arista[1]==vertice:
                    vert=arista[0]
                    flag=True
                else:
                    flag=False      
                if vert not in listavertice and flag:
                        listavertice.append((vert))
                        flag=False
            graph.append((vertice,listavertice))
    return graph

#def existPath(Grafo, v1, v2): 
#Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
#Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
def existPath(graph,v1,v2):
    if graph==None or v1==None or v2==None:
        return
    listv1=graph[v1-1][1]
    #print(listv1)
    if v2 in listv1:
        return True
    else:
       return existPathR(graph,v1,v2,[])
       
def existPathR(graph,v1,v2,visited):
    if v1 in visited:
        return False
    visited.append(v1)

    listv1 = graph[v1][1]

    if v2 in listv1:
        return True
    else:
        for v3 in listv1:
            if existPathR(graph, v3, v2, visited):
                return True
        return False

#V=[1,2,3,4]
#A=[(1,2),(1,3),(2,4)]
#graph=createGraph(V,A)
#print(existPath(graph,3,1))


#def isConnected(Grafo): 
#Descripción: Implementa la operación es conexo 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
def isConnected(graph):
    if graph==None:
        return
    for i in range(0,len(graph)):
        v=graph[i][0]
        for j in range(0,len(graph)):
            if j!=i:
                v2=graph[j][0]
                if existPath(graph,v2,v)==False:
                    return False
    return True
        
#V=[1,2,3,4]
#A=[(1,3),(1,2),(2,4)]
#graph=createGraph(V,A)
#print(isConnected(graph))


#def isTree(Grafo): 
#Descripción: Implementa la operación es árbol 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si el grafo es un árbol.
#hay que verificar que no hayan ciclos
class Tree:
    root=None
class TreeNode:
    value=None
    children=None
    parent=None
    color=None
    distance=None
def enqueue(Q,element):
    Q.append(element)
def dequeue(Q):
    return Q.pop()
def BFS(graph):
    if graph==None or not isConnected(graph):
        return
    else:
        BFS_R(graph,False)
def BFS_R(graph,cycles):
    for i in range(0,len(graph)):
        vertice=TreeNode()
        vertice.value=i
        vertice.color="white"
        vertice.distance=None
        vertice.parent=""
        vertice.children=graph[i][1]
        graph[i]=vertice
    root=TreeNode
    root=graph[0]
    root.color="gray"
    root.distance=0
    root.parent=None
    Q=[]
    enqueue(Q,root)
    while Q!=[]:
        print("queue",Q)
        u=dequeue(Q)
        print("u",u.value)
        L=graph[u.value].children
        print("nodos hijos",L)
        for v in L:
            vert=graph[v]
            if vert.color=="white":
                vert.color="gray"
                vert.distance=u.distance+1
                vert.parent=u
                enqueue(Q,vert)
            else:
                #print("hay ciclo")
                cycles=True
        u.color="black"
def isTree(graph):
    cycles=False
    BFS_R(graph,cycles)
    if cycles:
        return False
    else:
        return True
    
#V=[0,1,2,3]
#A=[(0,2),(0,1),(1,3)]
#print(createGraph(V,A))
#BFS(createGraph(V,A))
class DFSnode:
    value=None
    children=None
    parent=None
    color=None
    discoverytime=None
    endtime=None
def DFS(graph):
    if graph==None:
        return
    else:
        for i in range(0,len(graph)):
            v=DFSnode()
            v.color="white"
            v.value=i
            v.parent=None
            v.children=graph[i][1]
            graph[i]=v
        time=0
        for vert in graph:
            if vert.color=="white":
                DFSVisit(graph,vert,time)
def DFSVisit(graph,vertice,time):
    time=time+1
    vertice.discoverytime=time
    vertice.color="gray"
    for u in vertice.children:
        child=graph[u]
        if child.color=="white":
            child.parent=vertice
            DFSVisit(graph,child,time)
    vertice.color="black"
    time=time+1
    vertice.endtime=time


#def convertTree(Grafo)
#Descripción: Implementa la operación es convertir a árbol
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: LinkedList de las aristas que se pueden eliminar y el grafo
#resultante se convierte en un árbol.

def convertTree(graph): 
    s = next(iter(graph)) 
    parents = {}
    visited = set() 
    visited.add(s) 
    queue = deque() 
    queue.append(s) 
    parents[s] = None 
    edges = [] 
    while queue: 
        u = queue.popleft() 
        for vertex in graph[u]: 
            if vertex not in visited: 
                visited.add(vertex)
                parents[vertex] = u 
                queue.append(vertex)
            elif parents[u] != vertex:
                edges.append((u,vertex))

    return edges    
#def bestRoad(Grafo, v1, v2):
#Descripción: Encuentra el camino más corto, en caso de existir, entre
#dos vértices.
#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2
#vértices del grafo.
#Salida: retorna la lista de vértices que representan el camino más
#corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al
#final a v2. En caso que no exista camino se retorna la lista vacía.

from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Encuentra el camino más corto entre start y goal usando BFS.
    Entrada: 'graph' es un diccionario de listas de adyacencia.
    """
    
    # 1. Optimización clave:
    # 'visited' actúa como:
    #   a) Registro de visitados (si la clave existe, ya pasamos por ahí).
    #   b) Mapa de padres (key: nodo, value: padre) para reconstruir el camino.
    visited = {start: None} 
    
    queue = deque() 
    queue.append(start) 
    
    while queue:  
        u = queue.popleft() # Extraemos el nodo actual (FIFO)
        
        # 2. Chequeo de destino
        if u == goal: 
            path = [] 
            # 3. Backtracking (Reconstrucción del camino)
            # Retrocedemos usando el diccionario 'visited' hasta llegar al inicio (None)
            while u is not None: 
                path.append(u)
                u = visited[u] # Saltamos al padre del nodo actual
            
            # Invertimos la lista porque la reconstruimos del final al principio
            return path[::-1]

        # 4. Exploración de vecinos
        for vertex in graph[u]: 
            # Solo procesamos si NO está en el diccionario (no visitado)
            if vertex not in visited:
                visited[vertex] = u   # Marcamos como visitado y guardamos a 'u' como su padre
                queue.append(vertex)
                
    # Retorno implícito None o lista vacía si no se encuentra camino 
    return []

def isBipartite(graph):
    # Diccionario para almacenar el color de cada nodo (0 o 1).
    # También sirve como conjunto de 'visitados'.
    colors = {}

    # Iteramos sobre todos los nodos del grafo para manejar grafos NO CONEXOS 
    # (islas separadas).
    for start_node in graph:
        if start_node not in colors:
            # Iniciamos el coloreado de este componente
            colors[start_node] = 0
            queue = deque([start_node])

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    # Caso 1: El vecino no ha sido coloreado
                    if v not in colors:
                        # Lo pintamos del color opuesto al actual (1 - 0 = 1, o 1 - 1 = 0)
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    
                    # Caso 2: El vecino YA tiene color y es EL MISMO que el actual
                    elif colors[v] == colors[u]:
                        # Conflicto encontrado: Arista conecta dos nodos del mismo color.
                        # Esto confirma un ciclo impar.
                        return False

    # Si logramos colorear todo el grafo sin conflictos
    return True
# Grafo Bipartito (Un cuadrado: 0-1-2-3-0) -> Ciclo par

'''
grafo_ok = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# Grafo NO Bipartito (Un triángulo: 0-1-2-0) -> Ciclo impar
grafo_bad = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
'''
def PRIM(Grafo):
    """
    Implementa el algoritmo de PRIM para encontrar el árbol abarcador de costo mínimo.
    
    Parámetros:
    -----------
    Grafo : list[list[int/float]]
        Matriz de adyacencia donde Grafo[i][j] representa el peso de la arista
        entre los vértices i y j. Usar 0 o float('inf') para indicar que no hay arista.
    
    Retorna:
    --------
    list[tuple]
        Lista de aristas del árbol abarcador mínimo en formato (u, v, peso)
    float
        Costo total del árbol abarcador mínimo
    """
    n = len(Grafo)  # Número de vértices
    
    # Validación de entrada
    if n == 0:
        return [], 0
    
    # Inicialización
    visitado = [False] * n  # Marca los vértices incluidos en el árbol
    costo_min = [float('inf')] * n  # Costo mínimo para conectar cada vértice
    padre = [-1] * n  # Almacena el padre de cada vértice en el árbol
    arbol = []  # Aristas del árbol abarcador mínimo
    costo_total = 0
    
    # Comenzar desde el vértice 0
    costo_min[0] = 0
    
    for _ in range(n):
        # Encontrar el vértice no visitado con el costo mínimo
        u = -1
        for v in range(n):
            if not visitado[v] and (u == -1 or costo_min[v] < costo_min[u]):
                u = v
        
        # Marcar el vértice como visitado
        visitado[u] = True
        
        # Agregar la arista al árbol (excepto para el primer vértice)
        if padre[u] != -1:
            peso = Grafo[padre[u]][u]
            arbol.append((padre[u], u, peso))
            costo_total += peso
        
        # Actualizar los costos de los vértices adyacentes
        for v in range(n):
            # Si existe una arista u-v y v no ha sido visitado
            if Grafo[u][v] != 0 and Grafo[u][v] != float('inf') and not visitado[v]:
                # Si el peso de esta arista es menor que el costo actual
                if Grafo[u][v] < costo_min[v]:
                    costo_min[v] = Grafo[u][v]
                    padre[v] = u
    
    return arbol, costo_total


def KRUSKAL(Grafo):
    """
    Implementa el algoritmo de KRUSKAL para encontrar el árbol abarcador de costo mínimo.
    
    Parámetros:
    -----------
    Grafo : list[list[int/float]]
        Matriz de adyacencia donde Grafo[i][j] representa el peso de la arista
        entre los vértices i y j. Usar 0 o float('inf') para indicar que no hay arista.
    
    Retorna:
    --------
    list[tuple]
        Lista de aristas del árbol abarcador mínimo en formato (u, v, peso)
    float
        Costo total del árbol abarcador mínimo
    """
    n = len(Grafo)  # Número de vértices
    
    # Validación de entrada
    if n == 0:
        return [], 0
    
    # Paso 1: Extraer todas las aristas del grafo
    aristas = []
    for i in range(n):
        for j in range(i + 1, n):  # Solo la mitad superior para evitar duplicados
            if Grafo[i][j] != 0 and Grafo[i][j] != float('inf'):
                aristas.append((i, j, Grafo[i][j]))
    
    # Paso 2: Ordenar las aristas por peso (orden ascendente)
    aristas.sort(key=lambda x: x[2])
    
    # Paso 3: Inicializar Union-Find (Conjuntos disjuntos)
    padre = list(range(n))  # Cada vértice es su propio padre inicialmente
    rango = [0] * n  # Rango para optimización por rango
    
    def encontrar(v):
        """Encuentra el representante del conjunto con compresión de camino"""
        if padre[v] != v:
            padre[v] = encontrar(padre[v])  # Compresión de camino
        return padre[v]
    
    def unir(u, v):
        """Une dos conjuntos usando unión por rango"""
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)
        
        if raiz_u != raiz_v:
            # Unión por rango
            if rango[raiz_u] < rango[raiz_v]:
                padre[raiz_u] = raiz_v
            elif rango[raiz_u] > rango[raiz_v]:
                padre[raiz_v] = raiz_u
            else:
                padre[raiz_v] = raiz_u
                rango[raiz_u] += 1
            return True
        return False
    
    # Paso 4: Construir el árbol abarcador mínimo
    arbol = []
    costo_total = 0
    
    for u, v, peso in aristas:
        # Si los vértices están en diferentes conjuntos, agregar la arista
        if encontrar(u) != encontrar(v):
            arbol.append((u, v, peso))
            costo_total += peso
            unir(u, v)
            
            # Si ya tenemos n-1 aristas, el árbol está completo
            if len(arbol) == n - 1:
                break
    
    return arbol, costo_total


def shortestPath(Grafo, s, v):
    """
    Implementa el algoritmo de Dijkstra para encontrar el camino más corto.
    
    Parámetros:
    -----------
    Grafo : list[list[int/float]]
        Matriz de adyacencia donde Grafo[i][j] representa el peso de la arista
        entre los vértices i y j. Usar 0 o float('inf') para indicar que no hay arista.
    s : int
        Vértice de inicio
    v : int
        Vértice de destino
    
    Retorna:
    --------
    list[int] or None
        Lista de vértices que conforman el camino desde s hasta v.
        Retorna None si no existe camino entre s y v.
    """
    n = len(Grafo)  # Número de vértices
    
    # Validación de entrada
    if n == 0 or s < 0 or s >= n or v < 0 or v >= n:
        return None
    
    # Caso especial: inicio y destino son el mismo
    if s == v:
        return [s]
    
    # Inicialización
    distancia = [float('inf')] * n  # Distancia mínima desde s a cada vértice
    visitado = [False] * n  # Marca los vértices procesados
    padre = [-1] * n  # Almacena el padre de cada vértice en el camino
    
    # La distancia del vértice inicial a sí mismo es 0
    distancia[s] = 0
    
    # Algoritmo de Dijkstra
    for _ in range(n):
        # Encontrar el vértice no visitado con la distancia mínima
        u = -1
        for i in range(n):
            if not visitado[i] and (u == -1 or distancia[i] < distancia[u]):
                u = i
        
        # Si la distancia mínima es infinita, no hay más vértices alcanzables
        if distancia[u] == float('inf'):
            break
        
        # Marcar el vértice como visitado
        visitado[u] = True
        
        # Si hemos llegado al destino, podemos terminar
        if u == v:
            break
        
        # Actualizar las distancias de los vértices adyacentes
        for w in range(n):
            # Si existe una arista u-w y w no ha sido visitado
            if Grafo[u][w] != 0 and Grafo[u][w] != float('inf') and not visitado[w]:
                # Calcular la nueva distancia a través de u
                nueva_distancia = distancia[u] + Grafo[u][w]
                
                # Si encontramos un camino más corto, actualizamos
                if nueva_distancia < distancia[w]:
                    distancia[w] = nueva_distancia
                    padre[w] = u
    
    # Si no se encontró un camino al destino
    if distancia[v] == float('inf'):
        return None
    
    # Reconstruir el camino desde v hasta s
    camino = []
    actual = v
    while actual != -1:
        camino.append(actual)
        actual = padre[actual]
    
    # Invertir el camino para que vaya de s a v
    camino.reverse()
    
    return camino

