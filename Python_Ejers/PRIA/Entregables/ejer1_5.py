print("Introduzca una palabra: ")
palbra = input()
if not(palbra.isalpha()):
    print("no es texto")

else:
    if str.lower(palbra[0]) == palbra[0]:
        print("Empieza por minuscula")
    else:
        print("Empieza por mayuscula")

