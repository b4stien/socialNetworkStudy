#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import graphlib
import graphrep
import matplotlib.pyplot as plt


#Generating a Graph with 5 nodes
G = graphgen.generator(1000)

#Affect is a dict indexed by edges, and with affect's values
affect = nx.get_edge_attributes(G, 'affect')

#rep is a dict indexed by nodes, and with reput's value
rep = nx.get_node_attributes(G, 'reput')

#graphlib.plot_graph(G)

#print graphlib.node_size(G)

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax1.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))
ax3 = fig.add_subplot(323)
ax3.hist(nx.degree_histogram(G))
ax5 = fig.add_subplot(325)
ax5.hist(nx.get_node_attributes(G, 'reput').values())
for i in range(200):
	G = graphrep.updateReputation(G)
ax2 = fig.add_subplot(322)
ax2.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))
ax4 = fig.add_subplot(324)
ax4.hist(nx.degree_histogram(G))
ax6 = fig.add_subplot(326)
ax6.hist(nx.get_node_attributes(G, 'reput').values())
plt.show()

#print graphlib.plot_graphs(range(5))