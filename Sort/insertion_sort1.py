#!/usr/bin/python
import sys
import string

def insertion_sort_1(elements,length):
    insert_elem=int(elements[-1])
    for i in range(len(elements)-2,-1,-1):
        if int(elements[i])>insert_elem:
            elements[i+1]=elements[i]
            print (''.join(str(elem)+' ' for elem in elements))
        else:
            elements[i+1]=insert_elem
            print (''.join(str(elem)+' ' for elem in elements))
            break
    if insert_elem not in elements:
        elements[0]=insert_elem
        print (''.join(str(elem)+' ' for elem in elements))
            
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
insertion_sort_1(elements,length)
