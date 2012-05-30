#!/usr/bin/env python2.7

import networkx as nx
import matplotlib.pyplot as plt
import math

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

def plot_graphs(graph_list):
	fig = plt.figure()

	#Calculating the int as all graphs will fit into a int*int matrix of plot.
	foo = int(math.ceil(math.sqrt(len(graph_list))))

	for i in range(len(graph_list)):
		ax+i = fig.add_subplot(int(str(foo)+str(foo)+str(i)))
ax1.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))
for i in range(500):
	G = graphrep.updateReputation(G)
ax2 = fig.add_subplot(122)
ax2.plot(nx.draw_circular(G, node_size=graphlib.node_size(G), with_labels=False))

	plt.show()
	return True