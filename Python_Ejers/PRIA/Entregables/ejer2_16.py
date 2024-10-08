frase=input("Introduce una frase:")
iniciales=set([])
palabras=frase.split(" ")
for palabra in palabras:
    if palabra.isalpha():
        iniciales.add(palabra[0].lower())
    else:
        print("Error alguna palabra tiene caracteres no válidos")
        exit()
print(iniciales)