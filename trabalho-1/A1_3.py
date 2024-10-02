from grafo import Graph
import sys, utils

# 3. [Ciclo Euleriano] (2,0pts) Crie um programa que recebe um grafo como argumento. Ao final, o programa dever´a
# determinar se h´a ou n˜ao um ciclo euleriano e exib´ı-lo na tela de acordo com o exemplo abaixo5
# . A primeira linha
# dever´a conter o n´umero 0 caso o grafo n˜ao contenha o ciclo euleriano. Caso contenha, dever´a ser impresso 1 na
# primeira linha e em seguida, a sequˆencia de v´ertices que corresponde ao ciclo dever´a ser impressa

def main():
    
    graph = Graph(sys.argv[1])
    s = int(sys.argv[2]) - 1
        
    print(1 if utils.hierholzer(graph, s)[0] else 0)
        
    

if __name__ == '__main__':
    main()