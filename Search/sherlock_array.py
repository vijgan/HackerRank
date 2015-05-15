#!/usr/bin/python
import sys

def sherlock_array(elements,length):
    traverse_array=[0 for _ in range(length+1)]
    for i in range(1,length+1):
        traverse_array[i]=traverse_array[i-1]+elements[i-1]
    #print traverse_array
    for i in range(length):
        if traverse_array[i]==traverse_array[length]-traverse_array[i+1]:
            print ('YES')
            return
        else:
            continue
    print ('NO')
    return
    

test=int(input())
for _ in range(0,test):
    length=int(input())
    elements=list(input().strip().split())
    elements=[int(elem) for elem in elements]
    sherlock_array(elements,length)
