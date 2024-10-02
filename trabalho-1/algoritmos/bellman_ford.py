from grafo import Graph

def bellman_ford(graph:Graph, s:int):
    dist = [float('inf')] * graph.qtdVertices()
    pred = [None] * graph.qtdVertices()
    dist[s] = 0
    
    for _ in range(graph.qtdVertices() - 1):
        for u, v in graph.edges:
            if dist[v] > dist[u] + graph.peso(u, v):
                dist[v] = dist[u] + graph.peso(u, v)
                pred[v] = u
                
    for u, v in graph.edges:
        if dist[v] > dist[u] + graph.peso(u, v):
            return False, dist, pred
    return True, dist, pred

