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


def load_titanic_data():
    try:
        return pd.read_csv("datos/titanic.csv") # el fichero no existe, va a saltar error pero de existir se haria así
    except:
        print("Fichero no encontrado, cargando datos genericos.") 
        return sns.load_dataset('titanic')


def pclass_name(function_transformer, feature_names_in):
    return ["pclass"]  #

def sex_name(function_transformer, feature_names_in):
    return ["sex"]  #

def age_name(function_transformer, feature_names_in):
    return ["age_group"]  #

def family_name(function_transformer, feature_names_in):
    return ["family"]  #

def fare_name(function_transformer, feature_names_in):
    return["fare"]

def embarked_name(function_transformer, feature_names_in):
    return[ 'embarked_C', 'embarked_Q', 'embarked_S']


def survived_pipe(X):
    X['survived'].fillna(X['survived'].mode()[0], inplace=True) #
    return X

def class_pipe(X):  
    X['pclass'].fillna(X['pclass'].mode()[0], inplace=True) #
    return X

def fare_pipe(X):
    X['fare'].fillna(X['fare'].mean(), inplace=True) #
    X['fare']=(X['fare']-X['fare'].mean())/X['fare'].std() #
    return X

def family_pipe(X):
    X['sibsp'].fillna(X['sibsp'].mode()[0], inplace=True) #
    X['parch'].fillna(X['parch'].mode()[0], inplace=True) #
    X['family'] = X['sibsp'] + X['parch'] #
    X=X.drop(['sibsp','parch'],axis=1)
    return X

def sex_pipe(X):
    X['sex'].fillna(X['sex'].mode()[0], inplace=True) #
    X['sex'] = X['sex'].replace({'male': 0, 'female': 1}) #
    return X

def embarked_pipe(X):
    X['embarked'].fillna(X['embarked'].mode()[0], inplace=True) #
    x_cats = X[["embarked"]] #
    cat_encoder=OneHotEncoder() #
    x_1hot=cat_encoder.fit_transform(x_cats) #
    x_1hot.toarray() #
    x_output = pd.DataFrame(cat_encoder.transform(x_cats).toarray(), columns=cat_encoder.get_feature_names_out(), index=x_cats.index) #
    X = pd.concat([X,x_output],axis=1) #
    X=X.drop('embarked',axis=1)
    return X

def age_pipe(X):
    X['age'].fillna(X['age'].mean(), inplace=True) #
    X["age_group"] = pd.cut(X['age'],
                            bins = [-1,16,32,48,64,np.inf], # si ponemos el primer bin desde 0 el valor 0 lo asigna nulo
                            labels=[0,1,2,3,4])
    X=X.drop('age',axis=1)
    return X

pipeline = ColumnTransformer([
        ("pclass", FunctionTransformer(class_pipe,feature_names_out=pclass_name),["pclass"]),
        ("sex", FunctionTransformer(sex_pipe,feature_names_out=sex_name),["sex"]),
        ("age_group", FunctionTransformer(age_pipe,feature_names_out=age_name),["age"]),
        ("family", FunctionTransformer(family_pipe,feature_names_out=family_name),["sibsp", "parch"]),
        ("fare", FunctionTransformer(fare_pipe,feature_names_out=fare_name),["fare"]),
        ("embarked", FunctionTransformer(embarked_pipe,feature_names_out=embarked_name),["embarked"])
    ], 
    remainder='passthrough',
    verbose_feature_names_out=False
)


        

new_titanic_df  = load_titanic_data()

"""
Si los datos vinieran en un CSV con todo bien tal y como nos pides 
este bloque de limpiar y ajustar datos no seria necesario. Pero no es el caso.
"""

# borramos datos excedentes
a_borrar=["class","who","adult_male","deck","embark_town","alive","alone"]
new_titanic_df=new_titanic_df.drop(a_borrar,axis=1)

# arreglamos la columana age
new_titanic_df["age"].fillna(float(new_titanic_df["age"].mode()), inplace=True)
new_titanic_df['age']=new_titanic_df['age'].astype(int)

# dividimos datos
new_titanic_df_train, new_titanic_df_test = train_test_split(new_titanic_df, test_size=0.2, stratify=new_titanic_df['pclass'], random_state=17)

new_titanic_df_train_y=new_titanic_df_train['survived'].copy()
new_titanic_df_train_x=new_titanic_df_train.drop('survived',axis=1)

new_titanic_df_test_y=new_titanic_df_test['survived'].copy()
new_titanic_df_test_x=new_titanic_df_test.drop('survived',axis=1)

full_pipeline = Pipeline([
    ("preprocessing", pipeline),
    ("random_forest", RandomForestClassifier(n_estimators=100)),
])

param_dist = {
    'random_forest__n_estimators': randint(10, 200),
    'random_forest__max_features': ['sqrt', 'log2', None]
}
rndm_search = RandomizedSearchCV(full_pipeline, param_dist, cv=3, scoring='accuracy')
rndm_search.fit(new_titanic_df_train_x, new_titanic_df_train_y)
params=list(rndm_search.best_params_.values())


modelo_RF_opti=make_pipeline(pipeline,RandomForestClassifier(max_features=params[0],n_estimators=params[1]))
modelo_RF_opti.fit(new_titanic_df_train_x,new_titanic_df_train_y)

predic_RF_opti = modelo_RF_opti.predict(new_titanic_df_test_x)
prec_RF_opti = accuracy_score(new_titanic_df_test_y,predic_RF_opti)

print("La precision del modelo es:",prec_RF_opti)
