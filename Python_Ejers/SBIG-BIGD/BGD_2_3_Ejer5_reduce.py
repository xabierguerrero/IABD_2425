#!/usr/bin/python3 
from operator import itemgetter 
import sys 

currlett = None 
dicc={}
for line in sys.stdin: 
    line = line.strip() 
    currlett, count = line.split('\t', 1)
    count = int(count)
    if currlett in dicc:
        dicc[currlett]+=count
    else:
        dicc[currlett]=count

for clave in dicc:
    print(clave,"\t",dicc[clave])
