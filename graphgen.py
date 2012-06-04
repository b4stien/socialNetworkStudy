#!/usr/bin/env python2.7

import networkx as nx
import graphlib
import random
import copy
import matplotlib.pyplot as plt
import numpy as np

def generator(n):
	'''Generator for our social graph.

	Our graph will have n nodes, it will be a Dorogovtsev-Mendes's Graph, and
	it will handle reputation (for 	nodes) and affect (for edges).'''
	
	G = nx.dorogovtsev_goltsev_mendes_graph(1)
	
	'''In this loop we generate a raw network'''
	for i in range(n-3):
		r = random.choice(range(nx.number_of_edges(G)))
		
		e = nx.edges(G)
		e = e[r] #e is the selected edge
		
		nn = G.number_of_nodes() #nn is the new node number

		G.add_node(nn)

		G.add_edge(nn, e[0])
		G.add_edge(nn, e[1])

	'''In this bloc we set reputations'''
	reput = {}
	md = graphlib.max_degree(G)
	for i in range(G.number_of_nodes()):
		reput[i] = random.random() #float(G.degree(i))/float(md)

	nx.set_node_attributes(G,'reput',reput)

	'''And then we set affect'''
	affect = {}
	e = nx.edges(G)
	for i in range(G.number_of_edges()):
		affect[e[i]] = random.random()

	nx.set_edge_attributes(G,'affect',affect)	

	return G

if __name__ == "__main__":

	G1 = nx.dorogovtsev_goltsev_mendes_graph(1)

	G2 = G1.copy()
	r = random.choice(range(nx.number_of_edges(G2)))
	
	e = nx.edges(G2)
	e = e[r] #e is the selected edge
	
	nn = G2.number_of_nodes() #nn is the new node number

	G2.add_node(nn)

	G2.add_edge(nn, e[0])
	G2.add_edge(nn, e[1])

	G3 = G2.copy()

	for i in range(10):
		r = random.choice(range(nx.number_of_edges(G3)))
		
		e = nx.edges(G3)
		e = e[r] #e is the selected edge
		
		nn = G3.number_of_nodes() #nn is the new node number

		G3.add_node(nn)

		G3.add_edge(nn, e[0])
		G3.add_edge(nn, e[1])

	listG = [G1,G2,G3]

	for G in listG:
		'''In this bloc we set reputations'''
		reput = {}
		md = graphlib.max_degree(G)
		for i in range(G.number_of_nodes()):
			reput[i] = random.random() #float(G.degree(i))/float(md)

		nx.set_node_attributes(G,'reput',reput)

		'''And then we set affect'''
		affect = {}
		e = nx.edges(G)
		for i in range(G.number_of_edges()):
			affect[e[i]] = random.random()

		nx.set_edge_attributes(G,'affect',affect)
	layout = nx.spring_layout(G3)
	#graphlib.plot_graphs([G1,G2,G3], layout)



	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	N = len(nx.degree_histogram(G1))+2
	rep = [0]+nx.degree_histogram(G1)+[0]
	legend = ['']+[str(i) for i in range(len(nx.degree_histogram(G1)))]+['']
	ind = np.arange(N)
	width = 0.1
	ax1.bar(ind, rep,   width, color='r')
	plt.xticks(ind+width/2., legend)
	plt.show()