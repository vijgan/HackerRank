from collections import Counter
def missing_numbers(elements1,length1,elements2,length2):
    missing_numbers=[]
    number_dict1=Counter(elements1)
    for i in range(length2):
        if elements2[i] in number_dict1 and number_dict1[elements2[i]]>0:
            number_dict1[elements2[i]]-=1
        else:
            if elements2[i] not in missing_numbers: missing_numbers.append(elements2[i])
    number_dict1={k:v for k,v in number_dict1.items() if v>0}
    if len(number_dict1)>0:
        for k,v in number_dict1.items():
            for i in range(v): missing_numbers.append(k)
    print (''.join(str(elem)+' ' for elem in sorted(missing_numbers)))
    return

length1=int(input())
elements1=list(input().strip().split())
elements1=[int(elem) for elem in elements1]
length2=int(input())
elements2=list(input().strip().split())
elements2=[int(elem) for elem in elements2]
missing_numbers(elements1,length1,elements2,length2)
