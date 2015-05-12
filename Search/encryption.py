import math

def encryption(word):
    length=len(word)
    rows=int(math.floor(math.sqrt(length)))
    columns=int(math.ceil(math.sqrt(length)))
    if rows*columns<length: rows=columns
    arrays=[[None for _ in range(columns)] for _ in range(rows)]
    k=0
    for i in range(rows):
        for j in range(columns):
            if k<=length-1:
                arrays[i][j]=word[k]
                k+=1
    for i in range(columns):
        j=0
        string=''
        while j<rows:
            if arrays[j][i] is not None:
                string+=arrays[j][i]
                j+=1
            else:
                string+=''
                j+=1
        print (string,end=' ')
    #print(end='\n')
word=input()
encryption(word)
