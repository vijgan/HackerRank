#!/usr/bin/python
import sys

def sherlock_parris(elements,length):
    add=0
    number_dict=dict.fromkeys(elements,[])
    for i in range(0,length):
        if number_dict[elements[i]]==[]:
            number_dict[elements[i]]=[i] 
        else:
            number_dict[elements[i]].extend([i])
    number_dict={k: v for k,v in number_dict.items() if len(v)>1}
    for i in number_dict.keys():
        num=len(number_dict[i])
        val=num*(num-1)
        add+=val
    print (add)

test=int(input())
for i in range(0,test):
    length=int(input())
    elements=list(input().split())
    elements=[int(elem) for elem in elements]
    sherlock_parris(elements,length)
