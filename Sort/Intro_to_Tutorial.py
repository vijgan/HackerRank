#!/usr/bin/python
import sys
import string

def search_element(elements,size,search):
    for i in range(0,size):
        if search==int(elements[i]):
            return i
        else:
            pass
        
search=int(input())
size=int(input())
elements=list(input().split())
found=search_element(elements,size,search)
print (found)
