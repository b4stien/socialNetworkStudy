#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import graphlib
import graphrep
import matplotlib.pyplot as plt


#Generating a Graph with 5 nodes
G = graphgen.generator(20)

#Affect is a dict indexed by edges, and with affect's values
affect = nx.get_edge_attributes(G, 'affect')

#rep is a dict indexed by nodes, and with reput's value
rep = nx.get_node_attributes(G, 'reput')

#graphlib.plot_graph(G)

#print graphlib.node_size(G)

'''fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))
for i in range(500):
	G = graphrep.updateReputation(G)
ax2 = fig.add_subplot(122)
ax2.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))
plt.show()'''

print graphlib.plot_graphs(range(5))