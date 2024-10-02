# 5. [Algoritmo de Floyd-Warshall] (2,0pts) Crie um programa que recebe um arquivo de grafo como argumento. O
# programa dever´a exercutar o algoritmo de Floyd-Warshall e mostrar as distˆancias para cada par de v´ertices na tela
# utilizando o formato do exemplo abaixo. Na sa´ıda, cada linha ter´a as distˆancias para v´ertice na ordem crescente
# dos ´ındices informados no arquivo de entrad

import sys, utils
from grafo import Graph
import algoritmos.floyd_warshall as fw

def main():
    try:
        graph = Graph(sys.argv[1])
        s = int(sys.argv[2]) - 1
        if (s < 0 or s >= graph.qtdVertices()):
            return
    except:
        graph = Graph('grafos/fln_pequena.net')
        s = 0

    dist = fw.floyd_warshall(graph)

    # exemplo de saída esperada:
    # 1:0,10,3,5
    # 2:10,0,9,8
    # 3:3,9,0,11
    # 4:5,8,11,0

    for i in range(len(dist)):
        print(f'{i+1}:{",".join([str(v) for v in dist[i]])}')

if __name__ == '__main__':
    main()
