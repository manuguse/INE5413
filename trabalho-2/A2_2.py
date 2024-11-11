# 2. [Ordena¸c˜ao Topol´ogica] (3,0pts) Crie um programa que receba um arquivo de grafo dirigido n˜ao-ponderado com
# v´ertices rotulados como argumento. O programa deve fazer executar uma Ordena¸c˜ao Topol´ogica. Depois exiba a
# ordem topol´ogica, utilizando os r´otulos de cada v´ertice, como no exemplo abaixo:

from grafo import Grafo
import sys
from algoritmos import Algoritmos

def main():
    try:
        graph = Grafo(sys.argv[1])
    except:
        graph = Grafo('grafos/dirigido1.net')

    ot = Algoritmos().ordenacao_topologica(graph)
    print(" → ".join(ot), end='')

main() 