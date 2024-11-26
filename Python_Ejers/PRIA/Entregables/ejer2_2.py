print("Introduce dos cadenas de texto de la misma longitud:")
texto_1=input()
texto_2=input()

if len(texto_1)==len(texto_2):
    caracteres=[]
    linea=""
    for x in range(len(texto_1)):
        caracteres.append(texto_1[x])
        caracteres.append(texto_2[x])

    for y in range(len(caracteres)):
        linea=linea+caracteres[y]

    print(linea)
else:
    print("La longitud de las cadenas introducidas no coincide.")