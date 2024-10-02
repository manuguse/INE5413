from grafo import Graph

def dijkstra(graph, s):
    d = [float('inf')] * graph.qtdVertices()
    a = [None] * graph.qtdVertices()
    c = [False] * graph.qtdVertices()

    d[s] = 0
    while True:
        u = -1
        for i in range(graph.qtdVertices()):
            if not c[i] and (u == -1 or d[i] < d[u]):
                u = i
        if u == -1:
            break
        c[u] = True
        for v in graph.vizinhos(u):
            if d[v] > d[u] + graph.peso(u, v):
                d[v] = d[u] + graph.peso(u, v)
                a[v] = u
    return d, a

def reconstroi_caminho(a, u):
    caminho = []
    while u is not None:
        caminho.append(u)
        u = a[u]
    return caminho[::-1]