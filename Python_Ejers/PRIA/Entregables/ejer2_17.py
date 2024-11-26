print("¿Cuantos numero va a introducir?")

try:
    num=int(input())
except:
    print("Valor no válido introducido")
    exit()

for i in range(num):
    try:
        ind=int(input("Introduce un numero:"))
    except:
        print("Valor no válido introducido")
        exit()
    if ind%2==0:
        paridad="Par"
    else:
        paridad="Impar"
    t=(ind,paridad)
    print(t)