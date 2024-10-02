from grafo import Graph
    
def ciclo_euleriano(graph:Graph):
    for v in range(graph.qtdVertices()):
        if graph.grau(v) % 2 != 0:
            return False, [] # se for impar, nao pode ser euleriano
    if not eh_conexo(graph):
        return False, []

    ciclo = []
    stack = [0]

    while stack:
        u = stack[-1]
        if graph.grau(u) == 0:
            ciclo.append(stack.pop())
        else:
            for v in graph.vizinhos(u):
                graph.matriz_adjacencia[u][v] = float('inf')
                graph.matriz_adjacencia[v][u] = float('inf')
                stack.append(v)
                break
    return True, ciclo

def eh_conexo(graph:Graph):
    visited = [False] * graph.qtdVertices()
    stack = [0]
    visited[0] = True

    while stack:
        u = stack.pop()
        for v in graph.vizinhos(u):
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return all(visited)
    