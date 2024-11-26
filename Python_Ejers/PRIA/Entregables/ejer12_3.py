import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math


dominio=np.linspace(-5*math.pi,5*math.pi,100)
recorrido=[]
data={"x":dominio,
      "f(x)_1":[],
      "f(x)_2":[],
      "f(x)_3":[]}

# Funcion sin(x)/x
for x in dominio:
    y=math.sin(x)/x
    recorrido.append(y)

data["f(x)_1"]=recorrido
recorrido=[]

# Funcion 2sin(x)/x
for x in dominio:
    y=2*math.sin(x)/x
    recorrido.append(y)

data["f(x)_2"]=recorrido
recorrido=[]

# Funcion -sin(x)/x
for x in dominio:
    y=-1*math.sin(x)/x
    recorrido.append(y)

data["f(x)_3"]=recorrido
recorrido=[]

funciones=pd.DataFrame(data=data)


plt.figure(figsize=[8,6])
sns.lineplot(data = funciones, x = "x", y = "f(x)_1", color = "#f06741",label="sin(x)/x")
sns.lineplot(data = funciones, x = "x", y = "f(x)_2", color = "#a4f041",label="2sin(x)/x")
sns.lineplot(data = funciones, x = "x", y = "f(x)_3", color = "#8d41f0",label="-sin(x)/x")
plt.legend(title="Funciones")
plt.ylabel("f(x)")
plt.show()


