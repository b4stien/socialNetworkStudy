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

def graph(G, layout=None):

        if(layout == None):
                layout = nx.spring_layout(G)
        return nx.draw(G,layout, with_labels=False,
                       node_color = nx.get_node_attributes(G, 'reput').values(),
                       cmap=plt.cm.Blues, node_size = 100,
                       vmin = 0, vmax = 1,
                       linewidths = 0.3,
                       edge_color = nx.get_edge_attributes(G, 'affect').values(),
                       edge_cmap = plt.cm.Reds, width = 2,
                       edge_vmin = 0, edge_vmax = 1)

def plot_graph(G):
	graph(G)
	plt.show()
	return True

def plot_graphs(graph_list):
	length = len(graph_list)
	fig = plt.figure()
	layout = nx.spring_layout(graph_list[0])
	for i in range(length):
		G = graph_list[i]
		ax1 = fig.add_subplot(3*100+length*10+i+1)
		ax1.plot(graph(G, layout))
		ax3 = fig.add_subplot(3*100+length*10+length+i+1)
		ax3.hist(nx.degree_histogram(G))
		ax5 = fig.add_subplot(3*100+length*10+2*length+i+1)
		ax5.hist(nx.get_node_attributes(G, 'reput').values())

	plt.show()
	return True

def possible_friends(G, node):
	ret = []
	for i in G.neighbors(node):
		for j in G.neighbors(i):
			if G.node[j]['reput']>G.node[node]['reput'] and j not in ret:
				ret.append(j)
	return ret
