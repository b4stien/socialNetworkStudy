import networkx as nx
import graphlib
import graphrep

def createTestGraph(reputs, affects):
    G = nx.Graph()
    for node in reputs.iterkeys():
        G.add_node(node)
    for edge in affects.iterkeys():
        G.add_edge(edge[0], edge[1])
    nx.set_node_attributes(G, 'reput', reputs)
    nx.set_edge_attributes(G, 'affect', affects)
    return G

def testUpdateReputation(G):
    rep = [[65333,40500,73500,15500,31833,45750],
           [62014,45998,63865,19646,38951,44181],
           [59532,48790,58188,22916,43239,43971]]
    result = True
    for i in range(0, 3, 1):
        G = graphrep.updateReputation(G)
        reputs = nx.get_node_attributes(G, 'reput')
        for j in range(0, len(reputs),1):
            repu = (int)(reputs[j]*100000)
            print(repu)
            result = result and (rep[i][j] == repu or rep[i][j] == repu+1)
    if(result):
        print("Test updateReputation succeeds")
    else:
        print("Test updateReputation fails")
    
def main():
    reput6 = {0:0.7, 1:0.3, 2:0.9, 3:0.1, 4:0.2, 5:0.5}
    affect6 = {(0,1):0.7, (0,2):0.3, (1,2):0.9, (0,3):0.1, (2,3):0.2, (1,4):0.6, (2,4):0.8, (1,5):0.4, (4,5):0.3}
    G = createTestGraph(reput6, affect6)
    testUpdateReputation(G)
    graphlib.plot_graph(G)
    
main()
    
