#!/usr/bin/python
import sys
import re

def check_email(email_list):
    email_pattern='^[0-9a-zA-Z-_]+@[0-9a-zA-Z]+\.[a-z]{2,3}$'
    final_list=filter(lambda x:re.match(email_pattern,x),email_list)
    print (sorted(final_list))
    
email_check_list=[]
test=int(input())
for _ in range(0,test):
    email_check_list.append(input().strip())
check_email(email_check_list)
