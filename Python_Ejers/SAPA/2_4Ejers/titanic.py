import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,  StandardScaler, FunctionTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn import set_config
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.metrics import accuracy_score
import joblib
import warnings
import math

set_config(display="diagram")

def age_name(function_transformer, feature_names_in):
    return ["age_group"]  #
def family_name(function_transformer, feature_names_in):
    return ["family"]  #
def sex_name(function_transformer, feature_names_in):
    return ["sex"]  #

def cat_age(X):
    X = pd.DataFrame(X,columns=["age"])
    X["age_group"] = pd.cut(X["age"],
                            bins = [-1,16,32,48,64,np.inf], # si ponemos el primer bin desde 0 el valor 0 lo asigna nulo
                            labels=[0,1,2,3,4])
    X=X.drop("age",axis=1)
    return X

# Función para transformar tamaño de familia

def trans_family(X):
    X['family'] = X['sibsp'] + X['parch'] #
    X=X.drop(['sibsp','parch'],axis=1)
    return X

def func_transform_sex(X):
    return np.where(X == "female", 1, 0)


def load_titanic_data(fichero):
    return pd.read_csv(fichero)
    
fichero=input("Introduce el nombre del fichero CSV con los datos:")

existe = False
while not existe:
    try:
        titanic_DF=load_titanic_data(fichero)
        existe = True
    except:
        fichero=input("Error. El fichero introducido no existe. Vuelve a intentarlo:")

existe=False
modelo='./titanic_model.pkl'
print("Cargando predicciones del modelo.")
while not existe:
    try: 
        model_reloaded = joblib.load(modelo)
        existe=True
    except:
        modelo=input("Error. Archivo pkl no encontrado. Vuelve a intentarlo:")
        exit()

nuevas_predicciones = model_reloaded.predict(titanic_DF)
print(nuevas_predicciones)


