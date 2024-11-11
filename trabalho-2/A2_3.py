# 3. [Kruskal ou Prim] (3,0pts) Crie um programa que recebe um grafo n˜ao-dirigido e ponderado como argumento.
# Ao final, o programa dever´a determinar qual a ´arvore geradora m´ınima. O programa dever´a imprimir o somat´orio
# do peso das arestas da ´arvore na primeira linha e as arestas que pertencem a ´arvore geradora m´ınima na segunda
# linha, como no exemplo abaixo:

from grafo import Grafo
import sys
from algoritmos import Algoritmos

def main():
    try:
        graph = Grafo(sys.argv[1])
    except:
        graph = Grafo('grafos/agm_tiny.net')

    peso, arestas = Algoritmos().arvore_geradora_minima(graph)
    print(float(peso))
    print((', ').join(f'{aresta[0] + 1}-{aresta[1]+1}' for aresta in arestas))

main() 