import pandas as pd
import numpy as np
import matplotlib as plt

def ejer_1():
    data={"x":[],"y":[]}
    for i in range(15):
        data["x"].append(np.random.normal())
        data["y"].append(np.random.normal())

    puntos=pd.DataFrame(data=data)
    #print(points)
    return puntos

def ejer_2():
    puntos=ejer_1()
    print(puntos)


ejer_2()