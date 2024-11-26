import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print("Introduce los valores de un color en RGB (0-255,0-255,0-255)[Sin parentesis]:")
r,g,b=input().split(',')

r_hex=hex(int(r)).split('x')[1]
g_hex=hex(int(g)).split('x')[1]
b_hex=hex(int(b)).split('x')[1]

if len(r_hex)==1:
    r_hex="0"+r_hex
if len(g_hex)==1:
    g_hex="0"+g_hex
if len(b_hex)==1:
    b_hex="0"+b_hex


print("Hexadecimal: #{}{}{}".format(r_hex,g_hex,b_hex))
