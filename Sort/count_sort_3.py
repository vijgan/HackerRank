#!/usr/bin/python
import sys

def count_sort_3(elements):
    new_list=[]
    dictionary=dict.fromkeys(range(0,100),0)           
    for i in elements:
        if i in dictionary:
            dictionary[i]+=1
    for i in dictionary.values():
        new_list.append(i)
    for i in range(1,len(new_list)):
        new_list[i]=new_list[i]+new_list[i-1]
    print (''.join(str(elem)+' ' for elem in new_list))

length=int(input())
elements=[]
for i in range(0,length):
    num,word=input().split()
    elements.append(int(num))
count_sort_3(elements)
