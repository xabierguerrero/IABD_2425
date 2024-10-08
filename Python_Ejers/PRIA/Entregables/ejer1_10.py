positivos=0
negativos=0
try:
    while True:
        print("Introduce un número (0 para salir): ")
        num=int(input())

        if num>0:
            positivos=positivos+1
        elif num<0:
            negativos=negativos+1
        else:
            break

except:
    print("Valor no válido introducido")
    exit()

print("Numeros positivos introducidos:",positivos)
print("Numeros negativos introducidos:",negativos)