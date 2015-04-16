#!/usr/bin/python
import sys
import string

def quick_sort_2(elements):
    if len(elements)>1:
        pivot=elements[0]
        left_elements=[]
        right_elements=[]
        for i in range(1,len(elements)):
            if elements[i]<pivot:
                left_elements.append(elements[i])
            else:
                right_elements.append(elements[i])
        quick_sort_2(left_elements)
        quick_sort_2(right_elements)
        elements[:]=left_elements+[pivot]+right_elements
        #print elements
        print (''.join(str(elem)+' ' for elem in elements))
        
        
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
quick_sort_2(elements)
#print (''.join(str(elem)+' ' for elem in new_elements))
