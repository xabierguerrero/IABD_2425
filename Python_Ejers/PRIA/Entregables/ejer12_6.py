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
fig, ax = plt.subplots()
nx.draw(G,ax=ax,with_labels=True,
        font_color='#ffffff',
        font_weight='bold',
        node_color=node_color,
        edge_color=edge_color)
plt.show()