def contar_letras(palabra):
    dicc={}
    for x in range(len(palabra)):
        if palabra[x] in dicc.keys():
            dicc[palabra[x]] += 1
        else:
            dicc[palabra[x]] = 1
    
    return(dicc)

print("Introduce una cadena de carecteres.")
cadena=str(input())
print(contar_letras(cadena))
