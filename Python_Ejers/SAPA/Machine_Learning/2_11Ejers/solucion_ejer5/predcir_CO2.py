import joblib
import pandas as pd

def pedir_datos():
    Car = str(input("Introduzca la marca de su coche: "))
    Model = str(input("Introduzca el modelo de su coche: "))
    Volume = int(input("Introduzca el volumen de su coche (cm^3, creo): "))
    Weight = int(input("Introduzca el peso de su coche (kg): "))
    
    return {
        'Car': Car,
        'Model': Model,
        'Volume': Volume,
        'Weight': Weight,
        }

def cargar_modelo():
    try:
        return joblib.load("./modelo_CO2.pkl")
    except:
        print("ERROR: Modelo no encontrado.")


try:
    datos = pedir_datos()
except:
    print("ERROR. Por favor revise que los datos introducidos son correctos.")
try:
    
    modelo = cargar_modelo()
        
    columnas_esperadas = ['Car', 'Model', 'Volume', 'Weight']
    input_data = pd.DataFrame([datos], columns=columnas_esperadas)

    prediccion = modelo.predict(input_data)

    print("Prediccion:", prediccion)
    #if prediccion == 0:
    #    print("No va a devolver el prestamo.")
    #else:
    #    print("Va a devolver el prestamo")

except:
    print("uy, algo ha salido mal por nuestra parte, vuelve a intentarlo.")