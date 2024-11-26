#!/usr/bin/python3 
import sys 
for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for word in words:
        for letter in word: 
            print("{}\t1".format(letter))
