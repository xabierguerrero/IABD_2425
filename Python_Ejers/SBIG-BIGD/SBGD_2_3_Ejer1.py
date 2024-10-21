import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns
import networkx as nx
import pandas as pd

data=[[1,5],[2,15],[3,20],[4,10],[5,8],[6,2]]
familias_df=pd.DataFrame(data=data,columns=["Integrantes","Familias"])
colores=sns.color_palette("colorblind",6)

plt.subplot(1,2,1)
plt.pie(list(familias_df["Familias"]), colors=colores , labels = list(familias_df["Integrantes"]), autopct = "%0.3f%%")
plt.title("Familias")
plt.legend(title="Integrantes",bbox_to_anchor=(0,1))

plt.subplot(1,2,2)
sns.barplot(data = familias_df, x = "Integrantes", y = "Familias", color = "m")

plt.show()



