import nteworkx as nx

def createTestGraph(nbNodes, edges, reput, affect):
    G = nx.Graph()
    for i in range(0, 10):
        G.add_node(i)
    for edge in listEdges:
        G.add_edge(edge)
    nx.set_nodes_attribute('reput', reput)
    nx.set_edges_attribute('affect', affect)

def main():
    nbNodes = 5
    edges = [(0,1), (0,3), (0,4), (1,2), (1,3), (2, 4), (3, 5), (4,5)]
    reput = {0:0.5, 1:0.7, 2:0.1, 3:0.3, 4:0.3, 5:0.9}
            
