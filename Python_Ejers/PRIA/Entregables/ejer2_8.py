print("Introduce un número natural:")
try:
    num=int(input())
    if num<0:
        print("Los numeros negativos no son naturales.")
        exit()
    dicc={}
    for i in range(num):
        dicc[i]=i*i*i
    print(dicc)
except:
    print("Valor no válido introducido.")

