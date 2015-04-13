#!/usr/bin/python
import sys
import string

def check_panagram(sentence):
    alpha_dict={}
    count=1
    raw_sent=''.join(elem for elem in sentence.split()).lower().strip()
    for elem in raw_sent:
        if len(alpha_dict)==0 or elem not in alpha_dict:
            alpha_dict[elem]=count
        elif elem in alpha_dict:
            alpha_dict[elem]=int(alpha_dict.get(elem))+1
    if sorted(alpha_dict.keys())==sorted(map(chr, range(97, 123))):
        return'pangram'
    else: return 'not pangram'
sentence=input()
panagram=check_panagram(sentence)
print (panagram)
