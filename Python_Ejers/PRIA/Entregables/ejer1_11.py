total=0
cont=0
print("Introducee 2 numeros separados con una coma(,):")
try:
    ext_1,ext_2=input().split(",")
except:
    print("Datos no válidos introducidos.")
    exit()

if ext_1>ext_2:
    swap=ext_1
    ext_1=ext_2
    ext_2=swap


for i in range(int(ext_1),int(ext_2)+1):
    if i%3==0:
        total=total+i
        cont=cont+1
        media=total/cont
print("Suma de los multiplos del 3:",total)
print("Media de los multiplos del 3:",media)

