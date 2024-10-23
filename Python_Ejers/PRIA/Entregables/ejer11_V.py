import pandas as pd
import numpy as np
import matplotlib as plt
import os

#este es a su vez el ejercicio 1
def dataframe_numeros():
    data={"x":[],"y":[]}
    for i in range(15):
        data["x"].append(np.random.normal())
        data["y"].append(np.random.normal())

    puntos=pd.DataFrame(data=data)
    #print(points)
    return puntos

# este es a su vez el ejercicio 6
def dataframe_palabras():
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
    return palabras

def dataframe_pisos():
    fotocasa_df = pd.read_csv("https://drive.google.com/uc?export=view&id=1DwvALe87aeDzTk7s6xGPDd6itJ65s4YE", index_col = 0)
    return fotocasa_df


def ejer_2():
    puntos=dataframe_numeros()
    x_pos= puntos.loc[puntos["x"]>0] 
    return x_pos       

def ejer_3():
    puntos=dataframe_numeros()
    y_pos= puntos.loc[puntos["y"]>0] 
    return y_pos       

def ejer_4():
    puntos=dataframe_numeros()
    cuad_1= puntos.loc[puntos["y"]>0].loc[puntos["x"]>0]
    return cuad_1      

def ejer_5():
    puntos=dataframe_numeros()
    valores=[]
    
    for punto in puntos.itertuples():
        if punto[1]>0 and punto[2]>0:
            valores.append(True)
        else:
            valores.append(False)
        
    puntos.insert(loc=2,column="Primer_Cuadrante",value=valores)
    return puntos

def ejer_7():
    palabras=dataframe_palabras()
    frase="La palabra {} tiene {} letras, de las cuales {} son vocales y {} consonantes."
    for palabra in palabras.itertuples():
        print(frase.format(palabra[1],palabra[2],palabra[3],palabra[4]))
    
    return

def ejer_8():
    palabras=dataframe_palabras()
    print(palabras.loc[palabras["Consonantes"]==palabras["Vocales"]])

    return

def ejer_9():
    fotocasa_df = dataframe_pisos()
    print(np.shape(fotocasa_df))
    print(fotocasa_df.describe())
    for titulo in fotocasa_df.keys():
        print(fotocasa_df[titulo].value_counts()) 

    return   

def ejer_10():
    fotocasa_df = dataframe_pisos()
    print(fotocasa_df.head())

    return

def ejer_11():
    fotocasa_df = dataframe_pisos()
    print(fotocasa_df.tail())
    print(fotocasa_df[["Inmobiliaria","Tipo de inmueble"]].tail(3))

    return

def ejer_12():
    fotocasa_df = dataframe_pisos()
    a_borrar=["Domótica","Pista de Tenis","Alarma","Mascotas","Energía Solar","Gimnasio"]
    fotocasa1_df=fotocasa_df.drop(a_borrar,axis=1)
    return fotocasa1_df

def ejer_13():
    fotocasa1_df = ejer_12()
    fotocasa2_df = fotocasa1_df.rename(columns={"Tipo de inmueble":"Tipo"})
    return fotocasa2_df

def ejer_14():
    fotocasa2_df=ejer_13()
    fotocasa3_df=fotocasa2_df.dropna(subset="Precio")
    fotocasa3_df = fotocasa3_df.drop(fotocasa3_df[fotocasa3_df['Precio'] == 'A consultar'].index)
    return fotocasa3_df
    
def ejer_15():
    fotocasa3_df = ejer_14()
    fotocasa4_df=fotocasa3_df.astype({'Tipo':'category',
                                      'Orientación':'category',
                                      'Estado':'category',
                                      'Parking':'category'})
    return fotocasa4_df

def ejer_16():
    # el enlace no va
    #fichero ='https://raw.githubusercontent.com/ainaramu-icjardin/big_data/main/ciudades_ejemplo.csv'
    fichero='./Recursos/ciudades_ejemplo.csv'
    ciudades_df = pd.read_csv(fichero)
    ciudades_df.to_excel("./Recursos/ciudades_ejemplo.xlsx")

    return

def ejer_17():
    # el enlace no va
    #fichero ='https://raw.githubusercontent.com/ainaramu-icjardin/big_data/main/parocomunidades.csv'
    fichero='./Recursos/parocomunidades.csv'
    paro_df = pd.read_csv(fichero,encoding='latin1')
    print(paro_df.loc[paro_df["Periodo"]==2019])
    print(paro_df.loc[paro_df["Total"]>15])
    print(paro_df.loc[paro_df["Periodo"]==2019].loc[paro_df["Total"]>15])
    
    return

salir=False
while salir==False:
    print("Introduce el número de ejercicio a revisar(1-17)[0 para salir]:")
    ejer=int(input())
    match ejer:
        case 0:
            salir=True
        case 1:
            print("Ejer1")
            print(dataframe_numeros().info())
            print(dataframe_numeros().describe())
        case 2:
            print(ejer_2())
        case 3:
            print(ejer_3())
        case 4:
            print(ejer_4())
        case 5:
            print(ejer_5())
        case 6:
            print(dataframe_palabras())
        case 7:
            ejer_7()
        case 8:
            ejer_8()
        case 9:
            ejer_9()
        case 10:
            ejer_10()
        case 11:
            ejer_11()
        case 12:
            print(ejer_12().info())
            print(ejer_12().describe())
        case 13:
            print(ejer_13().info())
            print(ejer_13().describe())
        case 14:
            print(ejer_14().info())
            print(ejer_14().describe())
        case 15:
            print(ejer_15().info())
            print(ejer_15().describe())
        case 16:
            ejer_16()
        case 17:
            ejer_17()
        case _:
            None