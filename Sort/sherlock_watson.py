#!/usr/bin/python
import sys

def sherlock_watson(input_list):
    length=input_list[0]
    rotate_count=input_list[1]
    elements=input_list[2]
    position_list=input_list[3]
    division=0
    modulus=0
    if rotate_count<=length:
        elements=elements[-rotate_count:]+elements[:-rotate_count]
    else:
        for i in range(0,rotate_count):
            elements.insert(0,elements[-1])
            elements=elements[:-1]
    for j in position_list:
        print (elements[j])
        
length,rotate,positions=input().split(' ')
elements=list(input().split(' '))
elements=[int(x) for x in elements]
position_list=[]
for i in range(0,int(positions)):
    position_list.append(int(input()))
position_list=[int(x) for x in position_list]
sherlock_watson([int(length),int(rotate),elements,position_list])
