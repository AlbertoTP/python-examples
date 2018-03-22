# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 23:23:30 2018

@author: alternatif
"""

import re

print ("\nPython Calculator")
print ("Type 'exit' to exit\n")

previous=0
run=True

def performMath():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter equation:\n>")
    else:
        equation=input(">"+str(previous))
        
    if equation=="exit":
        print ("Exit to Python Calculator...")
        run=False
    else:
        equation=re.sub(r'[a-zA-Z,:()" "]', '',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)
            
            
while run:
    performMath()