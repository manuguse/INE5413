# 1. [Componentes Fortemente Conexas] (3,0pts) Crie um programa que receba um grafo dirigido e não-ponderado
# como argumento. Ao final, imprima na tela as componentes fortemente conexas desse grafo. O exemplo abaixo
# trata de uma saída válida, na qual identificou-se duas componentes fortemente conexas {3, 4, 5} e {1, 2, 6, 7}.

from grafo import Grafo
import sys
from algoritmos import Algoritmos

def main():
    try:
        graph = Grafo(sys.argv[1])
    except:
        graph = Grafo('grafos/dirigido2.net')

    cfc = Algoritmos().componentes_fortemente_conexas(graph)
    for componente in cfc:
        print(','.join([str(v + 1) for v in componente]))

main() 