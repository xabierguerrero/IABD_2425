print("Introduzca una letra: ")
letra = input()
vocales=["a","e","i","o","u"]

if len(letra)>1 or not(letra.isalpha()):
    print("Error, el dato no se puede procesar")
    exit()

if str.lower(letra) in vocales:
    print("Es una vocal.")
else:
    print("No es una vocal.")
