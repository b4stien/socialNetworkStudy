import networkx as nx
import graphgen
import graphrep
import random

G = graphgen.generator(10)

randomNode = random.choice(range(nx.number_of_nodes(G)))

print(G.node[randomNode]['reput'])

for i in range(0, 10, 1):
    graphrep.updateReputation(G)
    print(G.node[randomNode]['reput'])
