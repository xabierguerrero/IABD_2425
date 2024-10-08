
dicc={}
notas=[]
while True:
    nombre=input("Introduce el nombre del alumno (dejar vacio para salir):")
    if nombre == "":
        break
    else:
        while True:
            nota=int(input("Introduce una nota del alumno (-1 para salir):"))
            if nota==-1:
                notas=[]
                break
            else:
                notas.append(nota)
                dicc[nombre]=notas
    media=dicc[nombre]
for key,value in dicc.items():
    media=round(sum(value)/len(value),2)
    notas_str=""
    for x in range(len(value)):
        notas_str=notas_str+", "+str(value[x])
    print(key, "Sus notas son",notas_str,"con una media de",media)
