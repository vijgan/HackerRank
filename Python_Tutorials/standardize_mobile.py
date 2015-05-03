#!/usr/bin/python
import sys

def number_decorator(function_name):
    def number_changer(elements):
        return function_name(['+91 '+str(elem[:5])+' '+str(elem[5:]) for elem in elements])
    return number_changer
    
@number_decorator
def sort_numbers(elements):
    return sorted(elements)

elements=[]
test=int(input())
for _ in range(0,test):
    elements.append(input().strip())
elements=[elem[-10:] for elem in elements]
elements=sort_numbers(elements)
print (''.join(elem+'\n' for elem in elements))
