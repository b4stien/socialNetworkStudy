import networkx as nx
import random
import graphlib

def delete_links(G):
	'''
	Delete links in the graph if they disavantage the person.
	The link is deleted if (r1-r2)/affect(n1, n2)*deg(n1) > alpha
	where r1 > r2 and alpha is a random number between 0 and a given paramater beta.
	'''
	beta = 10
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

def create_links(G):
    '''We browse the graph, and for each node of the graph we are searching
    for possible new friends.

    One can create a link only with a friend of his friends.

    Then, some links can be created randomly
    '''
    Gret = G.copy()
    for node in G.nodes():
        for i in graphlib.possible_friends(G,node):
            rnode = G.node[node]['reput']
            ri = G.node[i]['reput']
            if rnode < ri and random.random()*0.05 > (ri - rnode):
                graphlib.create_link(G, node, i)
                break
                
    for i in range((int)(2*random.random())):
        n1 = random.choice(G.nodes())
        n2 = random.choice(G.nodes())
        if(n1 != n2 and not((n1, n2) in Gret.edges()) and not((n2, n1) in Gret.edges())):
            graphlib.create_link(G, n1, n2)

    return Gret