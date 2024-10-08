frase=input("Introduce una frase:")
print("Palabra | Longitud | Inicial | Posicion")
palabras=frase.split(" ")
for palabra in palabras:
    if palabra.isalpha():
        longtud=len(palabra)
        inicial=palabra[0]
        posicion=palabras.index(palabra)
        t=(palabra,longtud,inicial,posicion)
        print(t)
    else:
        print("Error alguna palabra tiene caracteres no válidos")
        exit()
#print(iniciales)