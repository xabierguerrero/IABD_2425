try:
    num=int(input("Introduce un número:"))
except:
    print("Valor no válido introducido.")
    exit()
    
divs=set([])
for i in range(num):
    if num%(i+1)==0:
        divs.add(i+1)

print("Los diviseros de",num,"son",divs)
