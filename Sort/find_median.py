#!/usr/bin/python
import sys

def find_partition(elements,low,hi):
    if low<hi:
        pivot=partition(elements,low,hi)
        find_partition(elements,low,pivot-1)
        find_partition(elements,pivot+1,hi)
    
        
def partition(elements,low,hi):
    pivot_index=hi
    elements[pivot_index],elements[hi]=elements[hi],elements[pivot_index]
    store_index=low
    for i in range(low,hi):
        if elements[i]<elements[pivot_index]:
            elements[i],elements[store_index]=elements[store_index],elements[i]
            store_index+=1
    elements[store_index],elements[hi]=elements[hi],elements[store_index]
    return store_index

length=int(input())
elements=list(input().split())
elements=[int(x) for x in elements]
find_partition(elements,0,length-1)
print (elements[(len(elements)-1)//2])
