def vocales_consonantes(palabra):
    num_vocs=0
    num_cons=0
    vocales=["A","a","E","e","I","i","O","o","U","u"]
    for letra in range(len(palabra)):
        if letra in vocales:
            num_vocs +=1
        else:
            num_cons +=1
    if num_vocs>num_cons:
        return True
    else:
        return False
palabras=["Sal","Ala"]
masVocales = filter(palabras,v)
