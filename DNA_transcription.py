#!/usr/bin/env python3 

seq = input("Enter a DNA sequence in 5' to 3' order: ")

fixed=seq.upper() 

forward=[]

for c in fixed:
    if c == "A":
        forward.append("U")
    elif c == "C":
        forward.append("G")
    elif c == "G":
        forward.append("C")
    elif c == "T":
        forward.append("A")

translate=''.join(forward)
print("5'",translate,"3'")
