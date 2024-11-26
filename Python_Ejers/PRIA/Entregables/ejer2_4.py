print("Introduce una palabra:")
palabra=input()
check=True
if " " in palabra:
    print("Introduce una solo palabra -_-")
    exit()
for x in range(len(palabra)):
    if palabra[x] != palabra[len(palabra)-(x+1)]:
        check=False
if check:
    print("La palabra introducida es un palíndroma")
else:
    print("La palabra introducida no es un palíndroma")
