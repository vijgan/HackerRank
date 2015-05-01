#!/usr/bin/python
import sys

def almost_sorted(elements,length):
    remaining=[]
    temp=[]
    left_index=0
    right_index=0
    if sorted(elements)==elements:
        print ('yes')
        sys.exit(1)
    else:
        for i in range(1,length):
            if elements[i-1]<=elements[i]:
                pass
            else:
                left_index=i-1
                break
        for j in range(length-1,-1,-1):
            if elements[j]>elements[j-1]:
                pass
            else:
                right_index=j+1
                break
        remaining=elements[left_index:right_index]
        if len(remaining)==1: 
            print ('no')
            sys.exit(1)
        sorted_remaining=sorted(remaining)
        k=0
        l=len(remaining)-1
        while k<l:
            temp=remaining[:]
            if swap(temp,k,l)==sorted_remaining:
                print ('yes')
                print ('swap %d %d'%(left_index+k+1,left_index+l+1))
                sys.exit(1)
            else:
                k+=1
                l-=1
                continue
        if reverse(remaining)==sorted_remaining:
            print ('yes')
            print ('reverse %d %d'%(left_index+1,right_index))
            sys.exit(1)
    print ('no')
    return

def swap(elements,i,j):
    elements[i],elements[j]=elements[j],elements[i]
    return elements

def reverse(items):
    new_items=list(reversed(items))
    return new_items

length=int(input())
elements=list(input().split(' '))
elements=[int(x) for x in elements]
almost_sorted(elements,length)
