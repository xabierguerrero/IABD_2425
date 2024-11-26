print("introduce tu nombre: ")
nombre = input()
try:
    if len(str(nombre)) > 10:
        print("El nombre", nombre ,"tiene más de 10 carácteres.")
    else:
        print("El nombre", nombre ,"tiene 10 o menos carácteres")
except:
    print("Nombre no valido?")
    exit()