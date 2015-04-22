#!/usr/bin/python
import sys

def count_sort_1(elements):
    dictionary=dict.fromkeys(range(0,100),0)
    for i in elements:
        if i in dictionary:
            dictionary[i]+=1
    print (''.join(str(elem)+' ' for elem in dictionary.values()))
    
length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
count_sort_1(elements)
