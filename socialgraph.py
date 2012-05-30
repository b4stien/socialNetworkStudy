#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import matplotlib.pyplot as plt


#Generating a Graph with 5 nodes
G = graphgen.generator(500)

#Affect is a dict indexed by edges, and with affect's values
affect = nx.get_edge_attributes(G, 'affect')

print affect[(1,2)]