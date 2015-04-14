#!/usr/bin/python
import sys
import string

def insertion_sort_2(elements,length):
    for i in range(1,length):
        j=i
        while j>0:
            if elements[j]<elements[j-1]:
                elements[j],elements[j-1]=elements[j-1],elements[j]
            j-=1
        print (''.join(str(elem)+' ' for elem in elements))
            
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
insertion_sort_2(elements,length)
