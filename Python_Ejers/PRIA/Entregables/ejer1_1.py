while True:
    print("Introduce un Número: \n (0 para salir)")
    try:
        num = int(input())
    except:
        print("valor no válido introducido")
        break
    if num != 0:
        if num%2==0:
            print("es par \n")
        else:
            print("es impar \n")
    else:
        break
