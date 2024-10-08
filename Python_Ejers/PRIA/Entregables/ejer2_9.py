
nombre=input("Introduzca su nombre:")

if not(nombre.isalpha()):
    print("Nombre no válido introducido.")
    exit()

edad=input("Introduzca su edad:")

if not(edad.isnumeric()):
    print("Edad no valida introducida.")
    exit()
    

telefono=input("Introduzca su numero de teléfono (sin espacios):")

if not(telefono.isnumeric()) or len(telefono)!=9:
    print("Numero de teléfono no valido introducido.")
    exit()


dicc={
    "nomb": nombre,
    "edad": edad,
    "telf": telefono
    }
print(dicc.get("nomb"),"tiene",dicc.get("edad"),"años y su número de teléfono es",dicc.get("telf"))