import math
import numpy as np
import scipy as sp
#ejer 4
#la posicion del array tambien aporta informacion ya que es el numero de hijos tambien, por eso NO lo ordenamos
datos={0:5,1:6,2:8,3:4,4:2}

media=np.average([*datos.keys()], weights=[*datos.values()])
varianza = np.average((list(datos.keys())-media)**2, weights=[*datos.values()])
desviacion=np.sqrt(varianza)
print("Media:",media)
print("Varianza:",varianza)
print("Desviacion:",desviacion)
