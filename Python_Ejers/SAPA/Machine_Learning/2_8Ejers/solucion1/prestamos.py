import joblib
import pandas as pd

def pedir_datos():
    int_rate = float(input("Introduce la tasa de interés (int_rate): "))
    installment = float(input("Introduce el monto de la cuota mensual (installment): "))
    fico = float(input("Introduce el puntaje de crédito FICO (fico): "))
    revol_bal = float(input("Introduce el saldo de crédito revolvente (revol_bal): "))
    revol_util = float(input("Introduce el porcentaje de utilización del crédito revolvente (revol_util): "))
    inq_last_6mths = float(input("Introduce el número de consultas crediticias en los últimos 6 meses (inq_last_6mths): "))
    pub_rec = int(input("Introduce el número de registros públicos (pub_rec): "))
    purpose = input("Introduce el propósito del préstamo ('debt_consolidation', 'credit_card', 'all_other', 'home_improvement', 'small_business', 'major_purchase', 'educational'): ")
    credit_policy = float(input("Introduce la cantidad de política de crédito (credit_policy): "))
    return {
        'int.rate': int_rate,
        'installment': installment,
        'fico': fico,
        'revol.bal': revol_bal,
        'revol.util': revol_util,
        'inq.last.6mths': inq_last_6mths,
        'pub.rec': pub_rec,
        'purpose': purpose,
        'credit.policy': credit_policy
        }

def cargar_modelo():
    try:
        return joblib.load("./modelo_prestamos.pkl")
    except:
        print("ERROR: Modelo no encontrado.")


try:
    datos = pedir_datos()
except:
    print("ERROR. Por favor revise que los datos introducidos son correctos.")
try:
    
    modelo = cargar_modelo()
        
    columnas_esperadas = ['int.rate', 'installment', 'fico', 'revol.bal', 'revol.util', 'inq.last.6mths', 'pub.rec', 'purpose', 'credit.policy']
    input_data = pd.DataFrame([datos], columns=columnas_esperadas)

    prediccion = modelo.predict(input_data)

    print("Prediccion:", prediccion)
    if prediccion == 0:
        print("No va a devolver el prestamo.")
    else:
        print("Va a devolver el prestamo")

except:
    print("uy, algo ha salido mal por nuestra parte, vuelve a intentarlo.")