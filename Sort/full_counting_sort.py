#!/usr/bin/python
import sys
import functools
def full_count_sort(elements,length):
    sorted_elements=actual_sort(elements,length)
    for elem in sorted_elements:
        if elem[2]>=length//2:
            print (elem[1],end=" ")
        else: print ('-',end=" ")
    
def actual_sort(elements,length):
    new_list=[]
    '''
    a dictionary is created with 0-100 as key and empty list for individual value
    '''
    dictionary=dict.fromkeys(range(0,100),[])
    '''
    The logic here is updating the dictionary with key as the number(from input) and 
    value as a tuple with the number, word and its position in the original input-array
    e.g: (0,tw,3)
    '''
    for i in range(0,length):  
        if elements[i][0] in dictionary.keys():
            if dictionary[elements[i][0]]==[]:
                '''
                If the value is empty just add the tuple (number,word,position) as a list
                '''
                dictionary[elements[i][0]]=[(elements[i][0],elements[i][1],i)]
                '''
                If there is a value there already, extend the list with your new tuple
                '''
            else: dictionary[elements[i][0]].extend([(elements[i][0],elements[i][1],i)])
    '''
    Once you create this dictionary, remove elements which has empty list as values
    '''            
    dictionary={k: v for k, v in dictionary.items() if len(v)>=1}
    '''
    Combine all sub-lists as one list
    '''
    new_list=functools.reduce(lambda x,y:x+y,dictionary.values())
    return new_list

length=int(input())
elements=[]
for i in range(0,length):
    num,word=input().split()
    elements.append((int(num),str(word)))
full_count_sort(elements,length)
