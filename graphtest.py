import networkx as nx
import graphlib

def createTestGraph(reputs, affects):
    G = nx.Graph()
    for node in reputs.iterkeys():
        G.add_node(node)
    for edge in affects.iterkeys():
        G.add_edge(edge[0], edge[1])
    nx.set_node_attributes(G, 'reput', reputs)
    nx.set_edge_attributes(G, 'affect', affects)
    return G

def main():
    reput5 = {0:0.7, 1:0.3, 2:0.1, 3:0.5, 4:0.9}
    affect5 = {(0,1):0.4, (0,3):0.1, (1,2):0.9, (1,4):0.3, (2,3):0.5, (3,4):0.3}
    G = createTestGraph(reput5, affect5)
    graphlib.plot_graph(G)

main()
    
