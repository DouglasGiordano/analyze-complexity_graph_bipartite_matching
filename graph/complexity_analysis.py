import os

import networkx as nx
from networkx import read_gpickle
from networkx.algorithms import bipartite, s_metric
from timeit import default_timer as timer
import pandas as pd

from networkx.algorithms.bipartite import hopcroft_karp_matching, density

N = 21
df = pd.DataFrame(columns=['time', 'nodes left', 'nodes right', 'edges'])
for i in range(4, N):
    print("Initializing graph reading "+str(i)+" ...")
    G = read_gpickle("graphs/graph"+str(i)+".pickle")
    left, right = nx.bipartite.sets(G)
    print("Initializing matching "+str(i)+" ...")
    start = timer()
    hopcroft_karp_matching(G, top_nodes=None)
    end = timer()
    time = end - start
    print("Matching finished "+str(i)+" ...")
    df.loc[i] = [time, len(left),len(right), len(G.edges)]
if not os.path.isfile('filename.csv'):
   df.to_csv('output/result_matching.csv', header=['time', 'nodes left', 'nodes right', 'edges'])
else: # else it exists so append without writing the header
   df.to_csv('output/result_matching.csv', mode='a', header=False)