from grafo import Grafo

class Algoritmos:
    def __init__(self):
        pass

    def componentes_fortemente_conexas(self, graph: Grafo):
        qtd_vertices = graph.qtdVertices() # quantidade de vértices
        _, _, _, f = self.dfs(graph)       # executa a DFS e salva em f o tempo de término de cada vértice
        
        graph_transposto = Grafo() # cria um grafo que será transposto
        graph_transposto.vertices = graph.get_vertices() # copia os vértices do grafo original
        for u, v, _ in graph.get_arestas(): # para cada aresta (u, v, _) do grafo original
            graph_transposto.adiciona_aresta(v, u) # adiciona a aresta (v, u) no grafo transposto

        ordem = sorted(range(qtd_vertices), key=lambda x: f[x], reverse=True) # ordena os vértices de acordo com o tempo de término

        visitado = [False] * qtd_vertices # cria uma lista de visitados
        componentes = [] # cria uma lista de componentes

        for u in ordem: # para cada vértice u na ordem
            if not visitado[u]: # se u não foi visitado
                componente = [] # cria uma lista de componentes
                self._dfs_componentes(graph_transposto, u, visitado, componente) # executa a DFS no grafo transposto
                componentes.append(componente) # adiciona a componente na lista de componentes

        return componentes # retorna a lista de componentes

    def _dfs_componentes(self, graph: Grafo, u: int, visitado: list, componente: list):
        visitado[u] = True # marca u como visitado
        componente.append(u) # adiciona u na lista de componentes
        for v in graph.vizinhos(u): # para cada vizinho v de u (ou seja, para cada vértice v que tem uma aresta de v para u)
            if not visitado[v]: # se v não foi visitado
                self._dfs_componentes(graph, v, visitado, componente) # executa a DFS em v

    def dfs(self, graph: Grafo):
        qtd = graph.qtdVertices() # quantidade de vértices
        c = [False] * qtd # cria uma lista de visitados
        t = [float('inf')] * qtd # cria uma lista de tempo de descoberta
        f = [float('inf')] * qtd # cria uma lista de tempo de término
        a = [None] * qtd # cria uma lista de predecessores
        
        tempo = [0] # cria uma lista de tempo com 
        
        for u in range(qtd): # para cada vértice u
            if not c[u]: # se u não foi visitado
                self.dfs_visit(graph, u, c, t, a, f, tempo) # executa a DFS em u
                
        return c, t, a, f # retorna as listas de visitados, tempo de descoberta, predecessores e tempo de término
    
    def dfs_visit(self, graph: Grafo, u: int, c: list, t: list, a: list, f: list, tempo: list):
        c[u] = True  # marca u como visitado
        tempo[0] += 1 # incrementa o tempo
        t[u] = tempo[0] # salva o tempo de descoberta de u
        
        for v in graph.vizinhos(u): # para cada vizinho v de u
            if not c[v]: # se v não foi visitado
                a[v] = u # salva u como predecessor de v
                self.dfs_visit(graph, v, c, t, a, f, tempo) # executa a DFS em v
        
        tempo[0] += 1 # incrementa o tempo
        f[u] = tempo[0] # salva o tempo de término de u
        
        return c, t, a, f # retorna as listas de visitados, tempo de descoberta, predecessores e tempo de término
    
    def ordenacao_topologica(self, graph: Grafo):
        qtd = graph.qtdVertices() # quantidade de vértices
        visitados = [False] * qtd # cria uma lista de visitados
        pilha = [] # cria uma pilha
        
        for u in range(qtd): # para cada vértice u
            if not visitados[u]: # se u não foi visitado
                self._dfs_topologico(graph, u, visitados, pilha) # executa a DFS topológica em u
                
        return [graph.get_vertices()[v] for v in reversed(pilha)] # retorna a ordem topológica em ordem reversa
    
    def _dfs_topologico(self, graph: Grafo, u, visitados, pilha):
        visitados[u] = True # marca u como visitado
        
        for v in graph.vizinhos(u): # para cada vizinho v de u
            if not visitados[v]: # se v não foi visitado
                self._dfs_topologico(graph, v, visitados, pilha) # executa a DFS topológica em v
                
        pilha.append(u) # adiciona u na pilha

    def arvore_geradora_minima(self, graph: Grafo):
        arestas_ordenadas = sorted(graph.get_arestas(), key=lambda x: x[2]) # ordena as arestas pelo peso
        pai = list(range(graph.qtdVertices())) # cria uma lista de pais
        rank = [0] * graph.qtdVertices() # cria uma lista de rank

        def find(u):
            if pai[u] != u: # se u não é o pai de u 
                pai[u] = find(pai[u]) # atualiza o pai de u
            return pai[u] # retorna o pai de u

        def union(u, v):
            raiz_u = find(u) # encontra a raiz de u
            raiz_v = find(v) # encontra a raiz de v
            if raiz_u != raiz_v: # se as raízes são diferentes
                if rank[raiz_u] > rank[raiz_v]: # se a raiz de u tem rank maior que a raiz de v
                    pai[raiz_v] = raiz_u  # atualiza o pai de v para u
                elif rank[raiz_u] < rank[raiz_v]: # se a raiz de u tem rank menor que a raiz de v
                    pai[raiz_u] = raiz_v # atualiza o pai de u para v
                else:
                    pai[raiz_v] = raiz_u # atualiza o pai de v para u
                    rank[raiz_u] += 1 # incrementa o rank de u

        peso_total = 0 # inicializa o peso total
        arestas_mst = [] # inicializa a lista de arestas da árvore geradora mínima

        for u, v, peso in arestas_ordenadas: # para cada aresta (u, v, peso) ordenada
            if find(u) != find(v): # se u e v não estão na mesma componente
                union(u, v) # une u e v
                peso_total += peso # incrementa o peso total
                arestas_mst.append((u, v)) # adiciona a aresta na árvore geradora mínima

        return peso_total, arestas_mst # retorna o peso total e a lista de arestas da árvore geradora mínima