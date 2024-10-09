import numpy as np

acierto=False
adivinar=np.random.randint(1,10)
intentos=1
while not acierto:
    num=int(input("Introduce un número(1-10):"))
    if num==adivinar:
        print("¡¡¡ENHORABUENA!!! Has acertado el número que había pensado: el",num)
        print("Intento(s):",intentos)
        acierto=True
    else:
        print("¡Has fallado! ¡Prueba otra vez!")
        intentos+=1