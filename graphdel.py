import networkx as nx
import random

def deleteLinks(G):
	'''
	Delete links in the graph if they disavantage the person.
	The link is deleted if (r1-r2)/affect(n1, n2)*deg(n1) > alpha
	where r1 > r2 and alpha is a random number between 0 and a given paramater beta.
	'''
	beta = 100
	reput = nx.get_node_attributes(G, "reput")
	affect = nx.get_edge_attributes(G, "affect")
	n = 0
	for edge in nx.edges(G):
		# Calculate alpha
		alpha = beta*random.random()

		# Define who has the higher reputation
		n1 = edge[1]
		n2 = edge[0]
		if(reput[edge[0]] > reput[edge[1]]):
			n1 = edge[0]
			n2 = edge[1]
		
		# Compute the coefficient
		coef = (reput[n1]-reput[n2])/affect[edge]*G.degree(n1)

		# Decide wether we delete the link
		if(coef > alpha):
			G.remove_edge(edge[0], edge[1])
			del affect[edge]

	# Set the new affect dict and return the graph
	nx.set_edge_attributes(G, "affect", affect)
	return G