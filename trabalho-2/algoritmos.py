from grafo import Grafo

class Algoritmos:
    def __init__(self):
        pass

    def componentes_fortemente_conexas(self, graph: Grafo):
        qtd_vertices = graph.qtdVertices()
        _, t, _, f = self.dfs(graph)
        
        graph_transposto = Grafo()
        graph_transposto.vertices = graph.get_vertices()
        for u, v, w in graph.get_arestas():
            graph_transposto.adiciona_aresta(v, u)

        ordem = sorted(range(qtd_vertices), key=lambda x: f[x], reverse=True)

        visitado = [False] * qtd_vertices
        componentes = []

        for u in ordem:
            if not visitado[u]:
                componente = []
                self._dfs_componentes(graph_transposto, u, visitado, componente)
                componentes.append(componente)

        return componentes

    def _dfs_componentes(self, graph: Grafo, u: int, visitado: list, componente: list):
        visitado[u] = True
        componente.append(u)
        for v in graph.vizinhos(u):
            if not visitado[v]:
                self._dfs_componentes(graph, v, visitado, componente)

    def dfs(self, graph: Grafo):
        qtd = graph.qtdVertices()
        c = [False] * qtd
        t = [float('inf')] * qtd
        f = [float('inf')] * qtd
        a = [None] * qtd
        
        tempo = [0] 
        
        for u in range(qtd):
            if not c[u]:
                self.dfs_visit(graph, u, c, t, a, f, tempo)
                
        return c, t, a, f
    
    def dfs_visit(self, graph: Grafo, u: int, c: list, t: list, a: list, f: list, tempo: list):
        c[u] = True
        tempo[0] += 1
        t[u] = tempo[0]
        
        for v in graph.vizinhos(u):
            if not c[v]:
                a[v] = u
                self.dfs_visit(graph, v, c, t, a, f, tempo)
        
        tempo[0] += 1
        f[u] = tempo[0]
        
        return c, t, a, f
    
    def ordenacao_topologica(self, graph: Grafo):
        qtd = graph.qtdVertices()
        visitados = [False] * qtd
        pilha = []
        
        for u in range(qtd):
            if not visitados[u]:
                self._dfs_topologico(graph, u, visitados, pilha)
                
        return [graph.get_vertices()[v] for v in reversed(pilha)]
    
    def _dfs_topologico(self, graph: Grafo, u, visitados, pilha):
        visitados[u] = True
        
        for v in graph.vizinhos(u):
            if not visitados[v]:
                self._dfs_topologico(graph, v, visitados, pilha)
                
        pilha.append(u)
