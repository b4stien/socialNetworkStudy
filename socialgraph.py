#!/usr/bin/env python2.7

import networkx as nx
import graphgen
import graphlib
import graphrep
import matplotlib.pyplot as plt


def evolution(nbNodes, nbRepUpdates):
        G = graphgen.generator(nbNodes)
        G0 = G.copy()
        #for i in range(nbRepUpdates):
        #        G = graphrep.updateReputation(G)
        nG = graphrep.create_links(G)
        graphlib.plot_graphs([G0, G, nG])

evolution(20, 50)