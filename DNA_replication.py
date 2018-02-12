#!/usr/bin/env python3 

seq = input("Enter a DNA sequence in 5' to 3' order: ")

fixed=seq.upper() 

forward=[]

for c in fixed:
    if c == "A":
        forward.append("T")
    elif c == "C":
        forward.append("G")
    elif c == "G":
        forward.append("C")
    elif c == "T":
        forward.append("A")


reverse=forward[::-1]
str1 = ''.join(reverse)
print(str1)
