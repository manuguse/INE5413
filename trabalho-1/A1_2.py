# 2. [Buscas] (2,0pts) Crie um programa que receba um arquivo de grafo e o ´ındice do v´ertice s como argumentos3
# . O
# programa deve fazer uma busca em largura4 a partir de s e dever´a imprimir a sa´ıda na tela, onde cada linha dever´a
# conter o n´ıvel seguido de “:” e a listagem de v´ertices encontrados naquele n´ıvel. O exemplo abaixo trata de uma
# sa´ıda, na qual a busca se iniciou pelo v´ertice s no n´ıvel 0, depois prosseguiu nos v´ertices 3, 4 e 5 para o pr´oximo
# n´ıvel. No n´ıvel seguinte, a busca encontrou os v´ertices 1, 2, 6 e 7.


import sys, utils
import algoritmos.busca_em_largura as b
from grafo import Graph

def main():

    try:
        graph = Graph(sys.argv[1])
        s = int(sys.argv[2]) - 1
        if (s < 0 or s >= graph.qtdVertices()):
            return
    except:
        graph = Graph('grafos/fln_pequena.net')
        s = 0
    
    dist, _ = b.busca_em_largura(graph, s)
    try:
        for i in range(max(dist) + 1):
            print(f'{i}:', end=' ')
            print(*[v+1 for v in range(graph.qtdVertices()) if dist[v] == i and dist[v] != float('inf')], sep=',')
    except:
        pass

    # expected output:
    # 0: 1
    # 1: 2, 4, 9, 10
    # 2: 3, 5, 8
    # 3: 7, 6
                
if __name__ == '__main__':
    main()