from grafo import Grafo

class Algoritmos:
    def __init__(self):
        pass
    
    def componentes_fortemente_conexas(self, graph: Grafo):
        c, t, a, f = self.dfs(graph)
        at = set()
        for aresta in graph.get_arestas():
            at.add((aresta[1], aresta[0], aresta[2]))  # Mantenha o peso da aresta
        gt = Grafo(grafo=(graph.get_vertices(), list(at), False))
        _, _, alt, _ = self.dfs_descrescente(gt, f)
        
        return alt
    
    def dfs(self, graph: Grafo):
        qtd = graph.qtdVertices()
        c = [False] * qtd     # Marca de vértices visitados
        t = [float('inf')] * qtd   # Tempo de descoberta
        f = [float('inf')] * qtd   # Tempo de término
        a = [None] * qtd      # Predecessores
        
        tempo = [0]  # Tempo como uma lista para atualização correta em recursão
        
        for u in range(qtd):
            if not c[u]:  # Se o vértice ainda não foi visitado
                self.dfs_visit(graph, u, c, t, a, f, tempo)
                
        return c, t, a, f
    
    def dfs_descrescente(self, graph: Grafo, f):
        qtd = graph.qtdVertices()
        c = [False] * qtd     # Marca de vértices visitados
        t = [float('inf')] * qtd
        f_new = [float('inf')] * qtd
        a = [None] * qtd
        
        tempo = [0]
        
        # Ordena os vértices em ordem decrescente de tempos de término
        vertices_ordenados = sorted(range(qtd), key=lambda u: f[u], reverse=True)
        
        for u in vertices_ordenados:
            if not c[u]:  # Verifica se o vértice ainda não foi visitado
                self.dfs_visit(graph, u, c, t, a, f_new, tempo)
        
        return c, t, a, f_new
    
    
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

