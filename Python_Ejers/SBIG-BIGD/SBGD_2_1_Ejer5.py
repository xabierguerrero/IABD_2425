import math
#ejer 5

#aqui cada dato es es una ocurrencia distinta
#por eso el tratamiento para este array es distinto al anterior
datos=[15, 20, 15, 18, 22, 13, 13, 16, 15, 19, 18, 15, 16, 20, 16, 15, 18, 16, 14, 13] 
sumatorio=0
media=0
varianza=0
muestra=0
moda_count=0

datos.sort()
print(datos)
for x in range(len(datos)):
    sumatorio=sumatorio+datos[x]
    muestra=muestra+1

#sacamos la media:
media=round(sumatorio/muestra,2)


for y in range(max(datos)+1):
    if datos.count(y)!=0:
        #print(y,":",datos.count(y))
        if datos.count(y)>moda_count:
            moda_count=datos.count(y)
            moda=y

mediana_indice=int((len(datos)-1)/2)
mediana=datos[mediana_indice]

print("Sumatorio:",sumatorio)
print("muestra",muestra)
print("Media:",media)
print("Moda:",moda)
print("Mediana:",mediana)