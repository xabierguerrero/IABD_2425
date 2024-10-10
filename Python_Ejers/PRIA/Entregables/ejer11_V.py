import pandas as pd
import numpy as np
import matplotlib as plt

print("~~~~~ Ejer 1 ~~~~~~")
data={"x":[],"y":[]}
for i in range(15):
    data["x"].append(np.random.normal())
    data["y"].append(np.random.normal())

points=pd.DataFrame(data=data)
print(points)

print("~~~~~ Ejer 2 ~~~~~~")