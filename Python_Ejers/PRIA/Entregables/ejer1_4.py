print("introduce tu primer número: ")
try:
    num_g=int(input())
except:
    print("Número no valido introducido.")
    exit()

print("Introduce tu segundo número: ")
try:
    num_p=int(input())
except:
    print("Número no valido introducido.")
    exit()
    
if num_g<0 or num_p<0:
    print("No se permiten numeros negativos.")
    exit()

if num_p>num_g:
    swap=num_p
    num_p=num_g
    num_g=swap

if num_p==0:
        print("ningun numero es divisible por 0 >:(")
        exit()

if num_g%num_p==0:
    print(num_g,"es multiplo de",num_p)
else:
    print(num_g,"no es multiplo de",num_p)

