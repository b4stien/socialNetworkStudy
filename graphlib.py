#!/usr/bin/env python2.7

import networkx as nx
import matplotlib.pyplot as plt

def max_degree(G):
	'''We search the maximum degree of G's nodes '''
	m = 0
	for i in range(G.number_of_nodes()):
		if G.degree(i) >= m : m = G.degree(i)
	return m

def node_size(G):
	reput = nx.get_node_attributes(G, 'reput')
	node_size = []

	for i in range(G.number_of_nodes()):
		node_size.append(reput[i]*1000)

	return node_size

def plot_graph(G):
	nx.draw_circular(G, node_size=node_size(G), with_labels=False)
	plt.show()
	return True