#!/usr/bin/python
import sys
import string

def quick_sort_1(elements,length):
    right_elements=[]
    left_elements=[]
    pivot=elements[0]
    for i in range(1,length):
        if elements[i]>pivot:
            right_elements.append(elements[i])
        elif elements[i]<=pivot:
            left_elements.append(elements[i])
    return left_elements+[pivot]+right_elements
    
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
new_elements=quick_sort_1(elements,length)
print (''.join(str(elem)+' ' for elem in new_elements))
