print("¿Cuan largo va a ser el lado de los poligonos?")

try:
    num=int(input())
except:
    print("Valor no válido introducido")
    exit()
for i in range(num):
    linea =""
    for j in range(i+1):
        linea=linea+str(i+j+1)+" "
    
    for l in range(num-i):
        linea=linea+"  "

    for k in range(num):
        linea=linea+str(i+k+1)+" "
    print(linea)