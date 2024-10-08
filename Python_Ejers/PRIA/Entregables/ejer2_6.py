try:
    filas=int(input("Introduce el número de filas:"))
    columnas=int(input("Introduce el número de columnas:"))
except:
    print("Valor no valido introducido.")
    exit()
matriz=[]
tester=0
tester_old=0
for i in range(filas):
    linea=[]
    for j in range(columnas):
        print("Introduce el elemento [",i,"][",j,"]:")
        linea.append(int(input()))
    matriz.append(linea)

for k in range(filas):
    tester=0
    for l in range(columnas):
        tester=tester+matriz[filas-(l+1)][k]
        #print(matriz[filas-(l+1)][k])
    
    if tester_old !=0:
        if tester!=tester_old:
            print("La suma de las colunas no coincide")
            exit()
    tester_old=tester
print("La suma de todas las columnas es igual:", tester)




