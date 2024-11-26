import numpy as np
def palindromo(palabra):
    for x in range(len(palabra)//2):
        if palabra[x]!=palabra[len(palabra)-(x+1)]:
            return 
    return palabra

a=np.array([["ala", "delfín", "arroz"], ["cena", "kayak", "picnic"], ["hoja", "gato", "elle"]])


mis_palindromos=np.frompyfunc(palindromo,1,1)
print(a,"\n",mis_palindromos(a))
