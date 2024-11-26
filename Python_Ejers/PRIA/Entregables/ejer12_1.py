import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


coor_x = np.random.randint(100, size = 100)
coor_y = np.random.randint(100, size = 100)
data={"X":coor_x,"Y":coor_y}
puntos=pd.DataFrame(data=data)
colores = np.random.randint(100, size = 100)
tamaños = np.random.randint(100, size = 100)*10

plt.figure(figsize=(10,10))
plt.scatter(data = puntos, x = "X", y = "Y",
                cmap="hsv",
                c=colores,
                s = tamaños,
                alpha=0.5)
plt.title("Puntos")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()