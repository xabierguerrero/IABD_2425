palabras=[]
while True:
    entrada=input("Introduce una palabra (dejar vacio para salir):")
    if entrada=="":
        break
    else:
        palabras.append(entrada)
t=tuple(palabras)
primera_palabra, *otras_palabras, ultima_palabra = t
print("Primera palabra:",primera_palabra)
print("Ultima palabra:",ultima_palabra) 
