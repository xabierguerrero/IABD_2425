import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

avg=3.2
std=0.5

prob3_5kg=round(st.norm.cdf(3.505,avg,std)-st.norm.cdf(3.495,avg,std),3)
peso_80_mas_pesado=round(st.norm.ppf(0.8, avg, std),3) 

print("Probabilidad peso recien nacido =3.5:",prob3_5kg)
print("Peso minimo del 20% de los bebes mas pesados:",peso_80_mas_pesado)