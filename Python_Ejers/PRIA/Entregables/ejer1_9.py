import math

presupuesto = 0

while presupuesto<=200:
    print("Introduce un precio: ")

    try:
        precio=float(input())
        
        precio=math.floor(precio*100)/100

        presupuesto=presupuesto+precio
        if precio==0:
            print("Presupuesto finalizado, el coste final es",presupuesto)
            exit()
    except:
        print("precio no valido introducido.")
        exit()
    
    

print("Presupuesto de 200€ excedido en",math.floor((presupuesto-200)*100)/100 ,"€")