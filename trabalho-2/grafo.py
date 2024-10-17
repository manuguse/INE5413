class Grafo:
    def __init__(self, arquivo=None, qtde_vertices=None, arestas=None):
        self.matriz_adjacencia = []
        self.vertices = []
        self.preeche(arquivo, qtde_vertices, arestas)
            
    def qtdVertices(self): # O(1)
        return len(self.vertices)

    def vizinhos(self, u): # O(n)
        return [v for v in range(self.qtdVertices()) if self.matriz_adjacencia[u][v] != float('inf')]
    
    def grau(self, u): # O(n)
        return len(self.vizinhos(u))
    
    def qtdArestas(self): # O(n)
        return sum([self.grau(v) for v in range(self.qtdVertices())]) // 2
    
    def haAresta(self, u, v): # O(1)
        return self.matriz_adjacencia[u][v] != float('inf')
    
    def peso(self, u, v): # O(1)
        return self.matriz_adjacencia[u][v]
    
    def preeche(self, arquivo, vertices, arestas):
        if arquivo is None:
            self.preenche_sem_ler(vertices, arestas)
        else:
            self.ler(arquivo)
            
    def preenche_sem_ler(self, vertices, arestas):
        self.vertices = list(map(str, range(1, vertices+1)))
        self.matriz_adjacencia = [[float('inf')] * vertices for _ in range(vertices)]
        for u, v in arestas:
            self.matriz_adjacencia[u][v] = 1

    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            for line in file:
                if line.startswith('*vertices'):
                    n = int(line.split()[1])
                    for _ in range(n):
                        vertex = file.readline().split('"')[1]
                        self.vertices.append(vertex)
                        self.matriz_adjacencia.append([float('inf')] * n)  
                elif line.startswith('*edges'):
                    for line in file:
                        u, v, w = map(float, line.split())
                        u, v = int(u), int(v)
                        self.matriz_adjacencia[u-1][v-1] = w
                        self.matriz_adjacencia[v-1][u-1] = w
                elif line.startswith('*arcs'):
                    for line in file:
                        u, v, w = map(float, line.split())
                        u, v = int(u), int(v)
                        self.matriz_adjacencia[u-1][v-1] = w