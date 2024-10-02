# 3. [Ciclo Euleriano] (2,0pts) Crie um programa que recebe um grafo como argumento. Ao final, o programa dever´a
# determinar se h´a ou n˜ao um ciclo euleriano e exib´ı-lo na tela de acordo com o exemplo abaixo5
# . A primeira linha
# dever´a conter o n´umero 0 caso o grafo n˜ao contenha o ciclo euleriano. Caso contenha, dever´a ser impresso 1 na
# primeira linha e em seguida, a sequˆencia de v´ertices que corresponde ao ciclo dever´a ser impressa

from grafo import Graph
import algoritmos.euleriano as e
import sys, utils

def main():
    try:
        graph = Graph(sys.argv[1])
        # s = int(sys.argv[2]) - 1
    except:
        graph = Graph('grafos/ContemCicloEuleriano.net')
        s = 0
        
    ciclo = e.ciclo_euleriano(graph)
    if ciclo[0]:
        print(1)
        print(*[v+1 for v in ciclo[1]], sep=',')
    else:
        print(0)


if __name__ == '__main__':
    main()