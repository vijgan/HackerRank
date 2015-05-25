#!/usr/bin/python
import sys

def get_twod_hash(twod_list,substring_width,substring_length):
    twod_hash=[]
    for i in range(substring_length):
        value=0
        for j in range(substring_width):
            value+=ord(twod_list[i][j])
        twod_hash.append(value)
    return twod_hash

def get_hash_value(string):
    hash_value=0
    for i in range(len(string)):
        hash_value+=ord(string[i])
    return hash_value

def grid_search(twod_string,twod_substring,substring_width,substring_length,string_length,string_width):
    twod_hash=get_twod_hash(twod_substring,substring_width,substring_length)
    flag=0
    for i in range(string_length):
        for j in range(string_width-substring_width+1):
            current_string=twod_string[i][j:j+substring_width]
            if get_hash_value(current_string)==twod_hash[0] and current_string==twod_substring[0]:
                for k in range(1,substring_length):
                    if get_hash_value(twod_string[i+k][j:j+substring_width])==twod_hash[k] and twod_string[i+k][j:j+substring_width]==twod_substring[k]:
                        flag=1
                        pass
                    else:
                        flag=0
                        break
                if flag==1: 
                    print ('YES')
                    return
    print ('NO')
    return

test_length=int(input())
for _ in range(test_length):
    (string_length,string_width)=input().strip().split()
    (string_length,string_width)=(int(i) for i in (string_length,string_width))
    twod_string,twod_substring=[],[]
    for i in range(string_length):
        twod_string.append(input().strip())
    (substring_length,substring_width)=input().strip().split()
    (substring_length,substring_width)=(int(i) for i in (substring_length,substring_width))
    for i in range(substring_length):
        twod_substring.append(input().strip())
    grid_search(twod_string,twod_substring,substring_width,substring_length,string_length,string_width)
