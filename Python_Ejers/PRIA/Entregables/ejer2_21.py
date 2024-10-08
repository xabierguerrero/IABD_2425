try:
    mayor=int(input("Introduce el número mayor:"))
    menor=int(input("Introduce el número menor:"))
except:
    print("ERROR. Formato de los datos no válido.")
    exit()

if mayor>=menor:
    cociente=mayor//menor
    resto=mayor%menor
    t=(mayor,menor,cociente,resto)
    print("Dividendo:",t[0],"\nDivisor:",t[1],"\nCociente:",t[2],"\nResto:",t[3])
else:
    print("ERROR. Has introducido los valores al reves.")
    exit()