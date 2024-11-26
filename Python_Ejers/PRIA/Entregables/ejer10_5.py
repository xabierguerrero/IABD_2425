import numpy as np
rng=np.random.default_rng()
adiviar=rng.choice(20, size=5, replace=False)
acierto=False
while not acierto:
    aciertos=0
    print("Introduce cinco numeros separados por coma(','):")
    nums=input().split(",")
    nums=np.array([eval(i) for i in nums])
    for idx in np.ndenumerate(nums):
        for ndx in np.ndenumerate(adiviar):
            if idx[1]==ndx[1]:           
                if idx[0]==ndx[0]:
                    print("has acertado el numero y posicion de:",idx[1])
                    aciertos+=1
                else:
                    print("Has acertado el numero:",idx[1])
    print(aciertos)
    if aciertos==5:
        print("¡¡¡ENHORABUENA!!! Has acertado el array que había pensado:",nums)
        acierto=True

"""
acierto=False
while not acierto:
    for num in nums:
        if num in adiviar:
            print(num,"está")
            
    
    acierto=True


"""
