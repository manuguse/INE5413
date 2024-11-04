# 1. [Componentes Fortemente Conexas] (3,0pts) Crie um programa que receba um grafo dirigido e não-ponderado
# como argumento. Ao final, imprima na tela as componentes fortemente conexas desse grafo. O exemplo abaixo
# trata de uma saída válida, na qual identificou-se duas componentes fortemente conexas {3, 4, 5} e {1, 2, 6, 7}.

from grafo import Grafo
import sys
from algoritmos import Algoritmos

def main():
    
    try:
        graph = Grafo(sys.argv[1])
        s = int(sys.argv[2]) - 1
        if (s < 0 or s >= graph.qtdVertices()):
            return
    except:
        graph = Grafo('grafos/dirigido1.net')
        s = 0
    
    cfc = Algoritmos().componentes_fortemente_conexas(graph)
    print(cfc)
if __name__ == '__main__':
    main()