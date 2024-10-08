def vocal(letra):
    is_vocal=False
    vocales=["A","a","E","e","I","i","O","o","U","u"]
    if letra in vocales:
        is_vocal=True
    return(is_vocal)

letra=input("Introduce un caracter:")

if len(letra)!=1:
    print("ERROR. Numero de caracteres no válido.")
    exit()
if not letra.isalpha():
    print("ERRROR. Caracter no válido introducido.")
    exit()

if vocal(letra):
    print("Es una vocal.")
else:
    print("Es una consonante.")