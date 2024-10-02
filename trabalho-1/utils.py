from grafo import Graph

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

