import joblib
import pandas as pd

def pedir_datos():
    petal_len = float(input("Introduzca la longitud del petalo: "))
    petal_wth = float(input("Introduzca la anchura del petalo: "))
    sepal_len = float(input("Introduzca la longitud del sepalo: "))
    sepal_wth = float(input("Introduzca la anchura del sepalo: "))
    
    return {
        'petal length (cm)': petal_len,
        'petal width (cm)': petal_wth,
        'sepal length (cm)': sepal_len,
        'sepal width (cm)': sepal_wth,
        }

def cargar_modelo():
    try:
        return joblib.load("./iris_model.pkl")
    except:
        print("ERROR: Modelo no encontrado.")


try:
    datos = pedir_datos()
except:
    print("ERROR. Por favor revise que los datos introducidos son correctos.")
try:
        
    modelo = cargar_modelo()
            
    columnas_esperadas = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
    input_data = pd.DataFrame([datos], columns=columnas_esperadas)

    prediccion = modelo.predict(input_data)


    match prediccion:
        case 0:
            print("Setosa")
        case 1:
            print("Versicolor")
        case 2:
            print("Virginica")
        
except:
    print("uy, algo ha salido mal por nuestra parte, vuelve a intentarlo.")