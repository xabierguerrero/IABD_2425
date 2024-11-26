print("Introduce una linea de texto:")
vocales=["A", "a", "E", "e", "I","i","O","o","U","u"]
texto=input()
consonantes=[]
for x in range(len(texto)):
    if texto[x] not in vocales:
        consonantes.append(texto[x])
print(consonantes)