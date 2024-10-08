print("Introduce un numero entero: ")
matriz=""
try:
    num=int(input())
except:
    print("Tenias que introducir un ENTERO....")
    exit()

for x in range(num*num):
    if (x+1)%num==0:
        matriz=matriz+str(x)+"\n"
    else:
        if x<10:
            matriz=matriz+str(x)+"  "
        else:
            matriz=matriz+str(x)+" "

print(matriz)