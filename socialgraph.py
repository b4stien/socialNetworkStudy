#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import graphlib
import matplotlib.pyplot as plt


#Generating a Graph with 5 nodes
G = graphgen.generator(100)

#Affect is a dict indexed by edges, and with affect's values
affect = nx.get_edge_attributes(G, 'affect')

#rep is a dict indexed by nodes, and with reput's value
rep = nx.get_node_attributes(G, 'reput')

#nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False)
#plt.show()

#print graphlib.node_size(G)