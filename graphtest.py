import nteworkx as nx
import graphlib

def createTestGraph(reputs, affects):
    G = nx.Graph()
    for node, reput in reputs:
        G.add_node(key)
    for edge, affect in affects:
        G.add_edge(edge)
    nx.set_nodes_attribute('reput', reputs)
    nx.set_edges_attribute('affect', affects)

def main():
    reput5 = {0:0.7, 1:0.3, 2:0.1, 3:0.5, 4:0.9}
    affect5 = {(0,1):0.4, (0,3):0.1, (1,2):0.9, (1,4):0.3, (2,3):0.5, (3,4):0.3}
    
