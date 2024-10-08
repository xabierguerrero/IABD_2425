print("Introduce una cadena de texto:")
texto=str(input())

caracteres=[]
linea=""
for x in range(len(texto)):
    caracteres.append(texto[x])

for y in range(len(texto)): 
    linea=linea+caracteres[len(texto)-(y+1)]

print(linea)
