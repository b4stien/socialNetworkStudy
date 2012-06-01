#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import graphlib
import graphrep
import graphevo
import matplotlib.pyplot as plt


def evolution(nbNodes, nbRepUpdates):
    G = graphgen.generator(nbNodes)
    G0 = G.copy()
    for i in range(nbRepUpdates):
      	G = graphevo.delete_links(G)
      	G = graphevo.create_links(G)
        G = graphrep.updateReputation(G)
    graphlib.plot_graphs([G0, G])

evolution(100, 100)

