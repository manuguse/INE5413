class Grafo:
    def __init__(self, arquivo=None, grafo=None):
        self.arestas = []
        self.vertices = []
        
        self.preenche(arquivo, grafo)
        
    def preenche(self, arquivo, grafo):
        if arquivo:
            self.le(arquivo)
        elif grafo:
            self.preenche_from_existente(grafo)
            
    def preenche_from_existente(self, grafo):
        vertices = grafo[0]
        arestas = grafo[1]
        direcionado = grafo[2]
        
        self.vertices = vertices
        self.arestas = []
        
        for u, v, w in arestas:
            u -= 1
            v -= 1
            self.arestas.append((u, v, w))
            if not direcionado:
                self.arestas.append((v, u, w))
                
    def le(self, arquivo):
        vertices = []
        arestas = []
        direcionado = False
        
        with open(arquivo, 'r') as file:
            lines = file.readlines()
            v = int(lines[0].split()[1])
            
            for i in range(v):
                vertex = ' '.join(lines[i + 1].split(' ')[1:])
                vertices.append(vertex)
                
            direcionado = lines[v + 1].strip() == "*arcs"
            
            for i in range(v + 2, len(lines)):
                u, v, w = map(int, lines[i].split())
                arestas.append((u, v, w))
                
        self.preenche_from_existente((vertices, arestas, direcionado))

    def get_vertices(self):
        return self.vertices
    
    def get_arestas(self):
        return self.arestas
    
    def get_transposto(self):
        self.arestas = [(v, u, w) for (u, v, w) in self.arestas]
            
    def qtdVertices(self): # O(1)
        return len(self.vertices)

    def vizinhos(self, u): # O(n)
        return [v for (x, v, w) in self.arestas if x == u]
    
    def grau(self, u): # O(n)
        return len(self.vizinhos(u))
    
    def qtdArestas(self): # O(n)
        return len(self.arestas) // 2 if self.is_nao_direcionado() else len(self.arestas)
    
    def haAresta(self, u, v): # O(n)
        return any(x == u and y == v for (x, y, w) in self.arestas)
    
    def peso(self, u, v): # O(n)
        for (x, y, w) in self.arestas:
            if x == u and y == v:
                return w
        return float('inf')
    
    def is_nao_direcionado(self):
        for u, v, w in self.arestas:
            if (v, u, w) not in self.arestas:
                return False
        return True

    def get_matriz_adjacencia(self):
        n = self.qtdVertices()
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        
        for u, v, w in self.arestas:
            matriz[u][v] = w
            
        return matriz