import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math


G = nx.Graph()
G.add_nodes_from("abcde")
G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), ("a", "d", 2), ("a", "e", 5), ("b", "e", 4), ("c", "d", 3), ("d", "e", 1)])
node_color="#ad80fa"
edge_color="#b1ddf5"
mult=350
node_weights=[
        len(G.edges('a'))*mult,
        len(G.edges('b'))*mult,
        len(G.edges('c'))*mult,
        len(G.edges('d'))*mult,
        len(G.edges('e'))*mult]
widths = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(8,6))
nx.draw(G,with_labels=True,
        font_color='#ffffff',
        font_weight='bold',
        node_color=node_color,
        edge_color=edge_color,
        node_size=node_weights,
        edgelist=widths.keys(),
        width=list(widths.values()))

plt.show()

