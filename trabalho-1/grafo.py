class Graph:
    def __init__(self, arquivo):
        self.matriz_adjacencia = []
        self.vertices = []
        
        self.ler(arquivo) 
            
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

    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            lines = file.readlines()
            vertices = int(lines[0].split()[1])
            for i in range(vertices):
                vertex = ' '.join(lines[i + 1].split(' ')[1:])
                self.vertices.append(vertex)
                self.matriz_adjacencia.append([float('inf')] * vertices)  
            
            for line in lines[vertices + 2:]:
                if line == '':
                    continue
                try:
                    u, v, w = map(float, line.split())
                    u, v = int(u), int(v)
                    self.matriz_adjacencia[u-1][v-1] = w
                    self.matriz_adjacencia[v-1][u-1] = w
                except:
                    pass
