#!/usr/bin/python
import sys

def quicksort(elements,low,hi):
    if low<hi:
        pivot=partition(elements,low,hi)
        print (''.join(str(elem)+' ' for elem in elements))
        quicksort(elements,low,pivot-1)
        quicksort(elements,pivot+1,hi)
    
        
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
quicksort(elements,0,length-1)
