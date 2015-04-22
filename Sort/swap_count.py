#!/usr/bin/python
import sys

def quicksort(elements,lo,hi):
    if lo<hi:
        p=partition(elements,lo,hi)
        quicksort(elements,lo,p-1)
        quicksort(elements,p+1,hi)
    
def partition(elements,lo,hi):
    global quick_swap
    pivot_index=hi
    store_index=lo
    elements[hi],elements[pivot_index]=elements[pivot_index],elements[hi]
    for i in range(lo,hi):
        if elements[i]<elements[pivot_index]:
            elements[store_index],elements[i]=elements[i],elements[store_index]
            quick_swap+=1
            store_index+=1
    elements[store_index],elements[hi]=elements[hi],elements[store_index]
    quick_swap+=1
    return store_index

def insertionsort(elements):
    swap_count=0
    for i in range(1,len(elements)):
        j=i
        while j>0:
            if elements[j-1]>elements[j]:
                elements[j],elements[j-1]=elements[j-1],elements[j]
                swap_count+=1
            j-=1
    return swap_count
                
length=int(input())
elements=list(input().split())
elements1=[int(x) for x in elements]
elements2=[int(x) for x in elements]
insertion_swap=insertionsort(elements1)
quick_swap=0
quicksort(elements2,0,length-1)
print (insertion_swap-quick_swap)
