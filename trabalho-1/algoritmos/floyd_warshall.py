from grafo import Graph

def floyd_warshall(graph:Graph):
    n = graph.qtdVertices()
    dist = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in graph.vizinhos(i):
            dist[i][j] = graph.peso(i, j)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist