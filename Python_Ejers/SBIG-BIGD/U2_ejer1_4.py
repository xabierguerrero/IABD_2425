import math
#ejer 4
#la posicion del array tambien aporta informacion ya que es el numero de hijos tambien, por eso NO lo ordenamos
datos=[5,6,8,4,2] 
sumatorio=0
media=0
varianza=0
muestra=0



for x in range(len(datos)):
    sumatorio=sumatorio+x*datos[x]
    muestra=muestra+datos[x]

#sacamos la media:
media=media+round(sumatorio/muestra,2)

#varianza
for z in range(len(datos)):
    varianza=varianza+(datos[z]*pow((z-media),2))/muestra
    print(z,":",datos[z])
varianza=round(varianza,2)

#Desviacion estandar
desviacion=round(math.sqrt(varianza),2)

print("Sumatorio:",sumatorio)
print("Muestra:",muestra)
print("Media:",media)
print("Varianza:",varianza)
print("Desviacion:",desviacion)