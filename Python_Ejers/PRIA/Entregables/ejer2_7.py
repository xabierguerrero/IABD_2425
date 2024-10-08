try:
    filas=int(input("Introduce el número de filas:"))
    columnas=int(input("Introduce el número de columnas:"))
except:
    print("Valor no valido introducido.")
    exit()
matriz=[]
matrizT=[]

for i in range(filas):
    linea=[]
    for j in range(columnas):
        print("Introduce el elemento [",i,"][",j,"]:")
        linea.append(int(input()))
    matriz.append(linea)

print("Matriz:",matriz)

for iT in range(columnas):
    lineaT=[]
    for jT in range(filas):
        lineaT.append(matriz[jT][iT])
    matrizT.append(lineaT)

print("Transpuesta",matrizT)