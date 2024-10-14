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
    x_pos= puntos.loc[puntos["x"]>0] 
    print(x_pos)       

def ejer_3():
    puntos=ejer_1()
    y_pos= puntos.loc[puntos["y"]>0] 
    print(y_pos)       

def ejer_4():
    puntos=ejer_1()
    cuad_1= puntos.loc[puntos["y"]>0].loc[puntos["x"]>0]
    print(cuad_1)       

def ejer_5():
    puntos=ejer_1()
    valores=[]
    
    for punto in puntos.itertuples():
        if punto[1]>0 and punto[2]>0:
            valores.append(True)
        else:
            valores.append(False)
        
    puntos.insert(loc=2,column="Primer_Cuadrante",value=valores)
    print(puntos)

def ejer_6():
    vocales=["a","e","i","o","u"]
    cont_vocal=0
    cont_cons=0
    data={"Palabra":["euro",
                     "diez",
                     "algas",
                     "broma",
                     "cicuta",
                     "fatiga",
                     "nachos",
                     "jadeos",
                     "hazañas",
                     "boutique"],
          "Longitud":[],
          "Vocales":[],
          "Consonantes":[]}
    
    for palabra in data["Palabra"]:
        data["Longitud"].append(len(palabra))
        for x in range(len(palabra)):
            if str.lower(palabra[x]) in vocales:
                cont_vocal +=1
            else:
                cont_cons +=1
        data["Consonantes"].append(cont_cons)
        data["Vocales"].append(cont_vocal)
        cont_cons=0
        cont_vocal=0

    palabras=pd.DataFrame(data=data)
    #print(palabras)
    return palabras

def ejer_7():
    palabras=ejer_6()
    frase="La palabra {} tiene {} letras, de las cuales {} son vocales y {} consonantes."
    for palabra in palabras.itertuples():
        print(frase.format(palabra[1],palabra[2],palabra[3],palabra[4]))

def ejer_8():
    palabras=ejer_6()
    print(palabras.loc[palabras["Consonantes"]==palabras["Vocales"]])

def ejer_9():
    fotocasa_df = pd.read_csv("https://drive.google.com/uc?export=view&id=1DwvALe87aeDzTk7s6xGPDd6itJ65s4YE", index_col = 0)
    print(np.shape(fotocasa_df))

    print(fotocasa_df.info())

    print(fotocasa_df.describe())


#ejer_1()
#ejer_2()
#ejer_3()
#ejer_4()
#ejer_5()
#ejer_6()
#ejer_7()
#ejer_8()
ejer_9()