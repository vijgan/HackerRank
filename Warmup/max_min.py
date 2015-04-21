#!/usr/bin/python
import sys

def find_fairness(actual_list,list_length,fairness_length):
    fairness=100000000000000000000
    for i in range(list_length-fairness_length):
        fairness_count=actual_list[i+fairness_length-1]-actual_list[i]
        if fairness_count<fairness: fairness=fairness_count
    return fairness

list_length=int(input())
fairness_length=int(input())
actual_list=[int(input()) for _ in range(0,list_length)]
fairness=find_fairness(sorted(actual_list),list_length,fairness_length)
print (fairness)
