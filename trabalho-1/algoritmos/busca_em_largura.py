from grafo import Graph

def busca_em_largura(graph:Graph, s:int):
    cv = [False] * graph.qtdVertices()
    dist = [float('inf')] * graph.qtdVertices()
    pred = [None] * graph.qtdVertices()
    
    cv[s] = True
    dist[s] = 0
    queue = [s]
    
    while queue:
        u = queue.pop(0)
        for v in graph.vizinhos(u):
            if not cv[v]:
                cv[v] = True
                dist[v] = dist[u] + 1
                pred[v] = u
                queue.append(v)
                
    return dist, pred