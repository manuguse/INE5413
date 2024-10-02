from collections import deque
from grafo import Graph

def busca_em_largura(graph:Graph, s:int):
    cv = [False] * graph.qtdVertices()
    dist = [float('inf')] * graph.qtdVertices()
    pred = [None] * graph.qtdVertices()
    
    cv[s] = True
    dist[s] = 0
    queue = deque([s])
    
    while queue:
        u = queue.popleft()
        for v in graph.vizinhos(u):
            if not cv[v]:
                cv[v] = True
                dist[v] = dist[u] + 1
                pred[v] = u
                queue.append(v)
                
    return dist, pred
    
def ciclo_euleriano(graph):
    if not graph:
        return False
    
    for v in range(graph.qtdVertices()):
        if graph.grau(v) % 2 != 0:
            return False
        
    return True

def buscar_subciclo_euleriano(graph, v, c):
    ciclo = [v]
    while True:
        for u in graph.vizinhos(v):
            if graph.peso(v, u) != 0 and not c[v]:
                c[v] = True
                ciclo.append(u)
                v = u
                break
        else:
            break
    return (all(c[v] for v in range(graph.qtdVertices())), ciclo)

def hierholzer(graph, s):
    c = [False]*graph.qtdVertices()
    v = s
    (r, ciclo) = buscar_subciclo_euleriano(graph, v, c)
    if not r:
        return (False, None)
    if any(not c[v] for v in range(graph.qtdVertices())):
        return (False, None)
    return (True, ciclo)

#     Input :um grafo não-orientado G = (V,E)
# 1 foreach e ∈ E do
# 2 Ce ← false
# 3 v ← selecionar um v ∈ V arbitrariamente, que esteja conectado a uma aresta.
# // “buscar Subci c l oEuler i ano” invoca o Algoritmo 6
# 4 (r,C i c l o) ← buscar Subci c l oEuler i ano(G, v,C)
# 5 if r =false then
# 6 return (false,null)
# 7 else
# 8 if ∃e ∈ E :Ce =false then
# 9 return (false,null)
# 10 else
# 11 return (true,C i c l o)

def dijkstra(graph, s):
    visited = [False] * graph.qtdVertices()
    dist = [float('inf')] * graph.qtdVertices()
    dist[s] = 0
    
    for _ in range(graph.qtdVertices()):
        u = min((dist[v], v) for v in range(graph.qtdVertices()) if not visited[v])[1]
        visited[u] = True
        
        for v in graph.vizinhos(u):
            if not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph.peso(u, v))
                
    return dist

def floyd_warshall(graph):
    dist = [[float('inf')] * graph.qtdVertices() for _ in range(graph.qtdVertices())]
    
    for v in range(graph.qtdVertices()):
        dist[v][v] = 0
        
    for u, v in graph.edges:
        dist[u][v] = graph.weights[(u, v)]
        dist[v][u] = graph.weights[(v, u)]
        
    for k in range(graph.qtdVertices()):
        for i in range(graph.qtdVertices()):
            for j in range(graph.qtdVertices()):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

