from grafo import Grafo

class Algoritmos:
    def __init__(self):
        pass
    
    def componentes_fortemente_conexas(self, graph):
        c, t, a, f = self._busca_em_largura(graph, 0)

        at = []
        for u in range(graph.qtdVertices()):
            for v in graph.vizinhos(u):
                at.append((v, u))
                
        gt = Grafo(qtde_vertices=graph.qtdVertices(), arestas=at)
        
        ordem_decrescente_f = sorted(range(len(f)), key=lambda k: f[k], reverse=True)
        c_t, t_t, a_t, f_t = self._dfs_adaptado(gt, ordem_decrescente_f)
        
        componentes = []
        for i in range(len(c_t)):
            if c_t[i]:
                componente = []
                for j in range(len(a_t)):
                    if a_t[j] == i or j == i:
                        componente.append(j)
                componentes.append(componente)
        
        return componentes
    
    def _busca_em_largura(self, graph, s):
        c = [False] * graph.qtdVertices()
        t = [float('inf')] * graph.qtdVertices()
        f = [float('inf')] * graph.qtdVertices()
        a = [None] * graph.qtdVertices()
        
        tempo = 0
        
        for u in range(graph.qtdVertices()):
            if not c[u]:
                c, t, a, f = self._visita(graph, u, c, t, a, f, tempo)
        return c, t, a, f
    
    def _visita(self, graph, v, c, t, a, f, tempo):
        c[v] = True
        tempo += 1
        t[v] = tempo
        for u in graph.vizinhos(v):
            if not c[u]:
                a[u] = v
                c, t, a, f = self._visita(graph, u, c, t, a, f, tempo)
        tempo += 1
        f[v] = tempo
        
        return c, t, a, f
    
    def _dfs_adaptado(self, graph, ordem):
        c = [False] * graph.qtdVertices()
        t = [float('inf')] * graph.qtdVertices()
        f = [float('inf')] * graph.qtdVertices()
        a = [None] * graph.qtdVertices()
        
        tempo = 0
        
        for u in ordem:
            if not c[u]:
                c, t, a, f = self._visita(graph, u, c, t, a, f, tempo)
        return c, t, a, f