# 4. [Algoritmo de Bellman-Ford ou de Dijkstra] (2,0pts) Crie um programa que recebe um arquivo de grafo como
# argumento e um v´ertice s. O programa dever´a executar o algoritmo de Bellman-Ford ou de Dijkstra e informar o
# caminho percorrido de s at´e todos os outros v´ertices do grafo e a distˆancia necess´aria. A sa´ıda dever´a ser impressa
# na tela de acordo com o exemplo abaixo. Cada linha representa o caminho realizado de s para o v´ertice da respectiva
# linha. Em cada linha, antes dos s´ımbolo “:” dever´a estar o v´ertice destino. `A direita de “:”, encontra-se o caminho
# percorrido de s at´e o v´ertice destino. Mais `a direita encontram-se os s´ımbolos “d=” seguidos da distˆancia necess´aria
# para percorrer o caminho.

import sys, utils
from grafo import Graph
import algoritmos.dijkstra  as d

def print_formatado(dist, pred):
    for i in range(len(dist)):
        caminho = d.reconstroi_caminho(pred, i)
        print(f'{i+1}: {",".join([str(v+1) for v in caminho])}; d={dist[i]}')

def main():
    try:
        graph = Graph(sys.argv[1])
        s = int(sys.argv[2]) - 1
        if (s < 0 or s >= graph.qtdVertices()):
            return
    except:
        graph = Graph('grafos/fln_pequena.net')
        s = 0
    
    dist, pred = d.dijkstra(graph, s)

    # exemplo de saída esperada:
    # 1: 2,3,4,1; d=7
    # 2: 2; d=0
    # 3: 2,3; d=4
    # 4: 2,3,4; d=6
    # 5: 2,3,5; d=8

    print_formatado(dist, pred)
    

if __name__ == '__main__':
    main()