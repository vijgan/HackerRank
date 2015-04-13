#!/usr/bin/python
import sys
import string

def get_del_anagram_count(str1,str2):
    delete_count=0
    dict1={}
    dict2={}
    count1=1
    count2=1
    for i in str1:
        if len(dict1)==0 or i not in dict1:
            dict1[i]=count1
        elif i in dict1:
            dict1[i]=int(dict1.get(i))+1
    for j in str2:
        if len(dict2)==0 or j not in dict2:
            dict2[j]=count2
        elif j in dict2:
            dict2[j]=int(dict2.get(j))+1
    set1=set(dict1.keys())
    set2=set(dict2.keys())
    del_count1=sum(int(dict1[elem]) for elem in list(set1-set2))
    del_count2=sum(int(dict2[elem]) for elem in list(set2-set1))
    delete_count=del_count1+del_count2
    for k in list(set1-set2):
        del  dict1[k]
    for l in list(set2-set1):
        del dict2[l]
    common_count=dict1.keys() and dict2.keys()
    for m in common_count:
        diff=abs(int(dict1[m]-dict2[m]))
        delete_count+=diff
    return delete_count
string1=input()
string2=input()
count=get_del_anagram_count(string1,string2)
print (count)
