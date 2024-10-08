dicc={}
linea_final="Total:"
total=0
while True:
    articulo=input("Introduce el articulo:")
    if articulo == "0":
        break
    precio=int(input("Introduce el precio:"))
    if precio == 0:
        break

    
    
    dicc[articulo]=precio

for key,value in dicc.items():
    total=total+value
    linea=key
    linea=linea+":"
    for i in range(max(map(len, dicc))*2-len(str(value))-len(key)):
        linea=linea+" "

    linea=linea+str(value)
    print(linea)

for j in range(max(map(len, dicc))*2-len(str(total))-len("Total")):
        linea_final=linea_final+" "

linea_final=linea_final+str(total)
print(linea_final)
    


