#!/usr/bin/python
import sys

def find_next(elements,length):
    new_list={}
    sorted_elements=sorted(elements)
    for i in range(1,len(sorted_elements)):
        abs_difference=abs(sorted_elements[i]-sorted_elements[i-1])
        if abs_difference in new_list.keys():
            new_list[abs_difference].extend([sorted_elements[i-1],sorted_elements[i]])
        else:
            new_list[abs_difference]=[sorted_elements[i-1],sorted_elements[i]]
    temp=new_list[sorted(new_list.keys())[0]]
    print (''.join(str(elem)+' ' for elem in temp))
    
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
find_next(elements,length)
