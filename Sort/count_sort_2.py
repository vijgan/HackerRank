#!/usr/bin/python
import sys

def count_sort_1(elements):
    new_list=[]
    dictionary=dict.fromkeys(range(0,100),0)
    for i in elements:
        if i in dictionary:
            dictionary[i]+=1
    for k in sorted(dictionary.keys()):
        for i in range(0,dictionary[k]):
            new_list.append(k)
    print (''.join(str(elem)+' ' for elem in new_list))
    
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
count_sort_1(elements)
