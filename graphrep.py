import networkx as nx
import graphlib
import random

def updateReputation(G):
    '''
    Update the reputation of all nodes and return the new graph
    The new reputation of node n is :
         n.rep(t+1) = n.rep(t) + sum({(f.rep(t)-n.rep(t))/2*affect(n,f)/deg(n) , f friend of n})
    '''
    newRep = {}
    affect = nx.get_edge_attributes(G, 'affect')
    for node in G.nodes():
        newRep[node] = G.node[node]['reput']
        for friend in G.neighbors(node):
            if((node, friend) in affect):
                aff = affect[(node, friend)]
            else:
                aff = affect[(friend, node)]
            newRep[node] += (G.node[friend]['reput'] - G.node[node]['reput'])/2 * aff/G.degree(node)
    nx.set_node_attributes(G, 'reput', newRep)
    return G
