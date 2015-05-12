from itertools import combinations
'''
In this function,
1. We take all the input
2. Create tuple combination using combinations() functions from itertools from the list
3. If the sum of the tuple elements equals the actual amount, we will get the index of those 2 items
4. For getting the index, get the first index using list_name.index(value)
5. For getting the second index, use index() functions 
   optional paramater of start index e.g: list_name.index(value,last_index+1)
'''
def icecream_parlour(amount,flavours,element):
    flavour_combinations=combinations(element,2)
    for flavour in flavour_combinations:
        if flavour[0]+flavour[1]==amount:
            first_index=element.index(flavour[0])
            second_index=element.index(flavour[1],first_index+1)
            print (first_index+1,second_index+1,end=' ')
            print(end='\n')
            
test=int(input())
for _ in range(0,test):
    amount=int(input())
    flavours=int(input())
    elements=input().strip().split()
    elements=list(map(int,elements))
    icecream_parlour(amount,flavours,elements)
