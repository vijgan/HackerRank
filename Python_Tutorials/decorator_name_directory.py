#!/usr/bin/python
import sys
from operator import itemgetter

def age_decorator(function_name):
    def add_salutations(dictionary):
        for i in range(0,len(dictionary)):
            if dictionary[i][3]=='M': dictionary[i]=('Mr. '+dictionary[i][0]+' '+dictionary[i][1],dictionary[i][3],dictionary[i][2])
            elif dictionary[i][3]=='F': dictionary[i]=('Ms. '+dictionary[i][0]+' '+dictionary[i][1],dictionary[i][3],dictionary[i][2])
        return function_name(dictionary)
    return add_salutations

@age_decorator
def sort_by_age(dictionary):
    dictionary.sort(key=itemgetter(2))
    dictionary=[dictionary[i][0] for i in range(0,len(dictionary))]
    return dictionary

dictionary=[]
length=int(input())
for _ in range(0,length):
    (fname,lname,age,gender)=input().strip().split()
    dictionary.append((fname,lname,age,gender))
    
new_dict=sort_by_age(dictionary)
print (''.join(elem+'\n' for elem in new_dict))
