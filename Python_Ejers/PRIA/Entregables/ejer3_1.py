def divisores(entero):
    divis=[]
    for i in range(entero):
        if entero%(i+1)==0:
            divis.append(i+1)
    return(divis)

try:
    num=int(input("Introduce un número:"))
except:
    print("ERROR. El valor introducido no es un número")
    exit()

print(divisores(num))
