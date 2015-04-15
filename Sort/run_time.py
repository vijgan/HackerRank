#!/usr/bin/python
import sys
import string

def insertion_sort_2(elements,length):
    count=0
    for i in range(1,length):
        j=i
        while j>0:
            if elements[j]<elements[j-1]:
                elements[j],elements[j-1]=elements[j-1],elements[j]
                count+=j-(j-1)
            j-=1
    return count
        
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
count=insertion_sort_2(elements,length)
print (count)
