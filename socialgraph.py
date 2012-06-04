#!/usr/bin/env python2.7

import networkx as nx
import copy
import graphgen
import graphlib
import graphrep
import graphevo


def evolution(nbNodes, nbRepUpdates):
    G = graphgen.generator(nbNodes)
    layout = nx.spring_layout(G)
    G0 = G.copy()
    again = "y"
    n = 2
    while(again == "y" and n < 9):
        Gn = G.copy()
        for i in range(nbRepUpdates):
            for j in range(5):
                G = graphevo.delete_links(G)
                for k in range(10):
                    G = graphevo.create_links(G)
            G = graphrep.updateReputation(G)
        n += 1
        graphlib.plot_graphs([G0, Gn, G], layout)
        again = raw_input("Do you want to continue ? (y or n)")

evolution(110, 20)