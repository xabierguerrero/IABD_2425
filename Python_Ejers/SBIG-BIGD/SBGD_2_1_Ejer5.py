import math
import numpy as np
import scipy as sp
#ejer 5

#aqui cada dato es es una ocurrencia distinta
#por eso el tratamiento para este array es distinto al anterior
datos=[15, 20, 15, 18, 22, 13, 13, 16, 15, 19, 18, 15, 16, 20, 16, 15, 18, 16, 14, 13] 


datos.sort()
media=np.average(datos)
mediana=np.median(datos)
moda=sp.stats.mode(datos)[0]
q1=np.quantile(datos,.25)
q3=np.quantile(datos,.75)

print("Media:",media)
print("Moda:",moda)
print("Mediana:",mediana)
print("Q1:",q1)
print("Q3:",q3)