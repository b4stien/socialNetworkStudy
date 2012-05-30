#!/usr/bin/env python2.7

import networkx as nx
import random

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
	md = max_degree(G)
	for i in range(G.number_of_nodes()):
		reput[i] = float(G.degree(i))/float(md)

	nx.set_node_attributes(G,'reput',reput)

	'''And then we set affect'''
	affect = {}
	e = nx.edges(G)
	for i in range(G.number_of_edges()):
		affect[e[i]] = random.random()

	nx.set_edge_attributes(G,'affect',affect)	

	return G

def max_degree(G):
	'''We search the maximum degree of G's nodes '''
	m = 0
	for i in range(G.number_of_nodes()):
		if G.degree(i) >= m : m = G.degree(i)
	return m