import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math

palabras=['LA','AVENTURA','SIGUE']

plt.figure(figsize=(10,8))
plt.text(0.2,0.8,palabras[0],size=50,rotation=25,
         ha='center',va='center',
         bbox={'boxstyle':'round','facecolor':'#242fff',
               'edgecolor':'#242fff','alpha':0.7})
plt.text(0.5,0.55,palabras[1],size=50,rotation=-15,
         ha='center',va='center',
         bbox={'boxstyle':'round','facecolor':'#8a24ff',
               'edgecolor':'#8a24ff','alpha':0.7})
plt.text(0.8,0.3,palabras[2],size=50,rotation=10,
         ha='center',va='center',
         bbox={'boxstyle':'round','facecolor':'#24fff4',
               'edgecolor':'#24fff4','alpha':0.7})

plt.show()