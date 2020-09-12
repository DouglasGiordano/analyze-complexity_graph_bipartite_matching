import networkx as nx
from networkx import write_gpickle
from networkx.algorithms import bipartite

N = 21

#initialize the list with starting elements: 0, 1
fibonacciSeries = [0,1]
print("Initializing graph generator ...")
if N > 2:
    for i in range(2, N):

        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(nextElement)
        nodes1 = nextElement;
        nodes2 = nextElement;
        probability = 0.7;
        print("Generating graph " + str(i) + " with " + str(nextElement) + " nodes in each part...")
        # https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.generators.bipartite.bipartite_random_graph.html
        G = bipartite.random_graph(nodes1, nodes2, probability, seed=None, directed=False)
        write_gpickle(G, "graphs/graph"+str(i)+".pickle")


