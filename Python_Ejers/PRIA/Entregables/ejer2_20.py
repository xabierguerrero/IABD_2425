
palabras=["prueba","ejemplo","largo","funcionar"]
longitudes=[]
for palabra in palabras:
    longitudes.append(len(palabra))
dicc=dict(zip(palabras,longitudes))
print(dicc)