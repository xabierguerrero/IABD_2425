import math
grados=[]
#radianes=[]

while True:
    entrada=input("Introduce los grados del ángulo, sin decimales (Dejar en blanco para salir):")
    if entrada=="":
        break
    try:
        if int(entrada)>=0 and int(entrada)<=360:
            grados.append(int(entrada))
    except:
        print("ERROR. Valor no válido introducido.")
        exit()


for grado in grados:
    radian=round(grado*math.pi/180,2)
    #radianes.append(radian)
    t=tuple([grado,radian])
    print("Grados:",t[0],"Radianes:",t[1])
    
    
    
    
    
    
    
    