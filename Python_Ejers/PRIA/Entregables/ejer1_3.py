print("introduce tu primer número: ")
try:
    num_p=int(input())
except:
    print("Número no valido introducido.")
    exit()

print("Introduce tu segundo número: ")
try:
    num_g=int(input())
except:
    print("Número no valido introducido.")
    exit()

if num_p==num_g:
    print("Ambos números introducidos son iguales")
elif num_p>num_g:
    swap=num_p
    num_p=num_g
    num_g=swap
    print(num_g,"es mayor que",num_p)

if num_p==0:
        print("ningun numero es divisible por 0 >:(")
        exit()

if num_g%num_p==0:
    cociente=num_g/num_p
    print("La división es exacta \n Cociente:",int(cociente))
else:
    print("La división no es exacta \n Resultado:",num_g/num_p," \n Cociente:",num_g//num_p,"\n Resto:",num_g%num_p)