import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math

options = ["Suspenso", "Aprobado", "Notable", "Excelente"]
count = [20, 10, 45, 25]
colors = ["#ff2667", "#ff7226", "#26a8ff", "#67ff26"]

plt.pie(count, colors = colors, labels = options, 
        startangle = 45, explode = [0,0.2,0,0], shadow = True,autopct = "%0.2f%%")
plt.title("Notas")
plt.show()