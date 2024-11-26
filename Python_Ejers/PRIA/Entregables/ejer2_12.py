num=int(input("Introduce el numero de palabras que desea introducir:"))
dicc={}

for i in range(num):
    num_vocales=0
    palabra=input("Escriba la palabra a introducir:")
    if " " in palabra:
        print("Error, has introducido más de una palabra.")
        exit()
    if not palabra.isalpha():
        print("Error has introducido algo que no es una palabra.")
        exit()
    for j in range(len(palabra)):
        
        vocales=["a","e","i","o","u"]
        if palabra[j].lower() in vocales:
            num_vocales=num_vocales+1
    dicc[palabra]=num_vocales

print(dicc)