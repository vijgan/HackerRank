'''
This function,
1. Takes the original array and 2 generated arrays (left_array and right_array)
2. left_array and right_array are the exact length as the original array
3. It calls 2 functions get_left_index and get_right_index.
4. Each of these functions will calculate the left and right value (greater than current or 0)
   for the current index
5. Print that maximum value 
'''
def find_max_index_product(array,length):
    maximum=0
    if length<3: 
        print (0)
        sys.exit(1)
    for i in range(1,length-1):
        get_left_index(array,array[i],i)
        get_right_index(array,array[i],i,length)
        value=left_array[i]*right_array[i]
        if value>maximum: maximum=value
    print (maximum)

'''
This function,
1. Takes in current_value, current_index and the array
2. Here, we will update the left_index array with index of the first element greater than current element 
3. To do this, we will consider 3 criterias,
     i. If the previous element is less than the current, 
        we can set the start_index (for iteration) to the index returned for previous element.
        By, this we can skip elements which are already computed.
     ii. If the previous element is equal to current element, assign the left_index to value 
         of the previous element and return
     iii. If none of the condition is set, we can set start to index of previous element
'''    
def get_left_index(array,current,index):
    global left_array
    if array[index-1]<current:
        start=left_array[index-1]
    elif array[index-1]==current:
        left_array[index]=left_array[index-1]
        return
    else:
        start=index-1
    for i in range(start,-1,-1):
        if array[i]>current:
            left_array[index]=i+1
            return
        else: continue

'''
This function is very similar to get_left_index,
1. Takes in current_value, current_index, array and last_index
2. Here, we will update the right_index array with index of the first element greater than current element 
3. To do this, we will consider 3 criterias,
     i. If the next element is less than the current, 
        we can set the start_index (for iteration) to the index returned for next element.
        By, this we can skip elements which are already computed.
     ii. If the next element is equal to current element, assign the right_index to value 
         of the previous element and return
     iii. If none of the condition is set, we can set start to index of next element
'''  
def get_right_index(array,current,index,length):
    global right_array
    if array[index+1]<current:
        start=right_array[index+1]
    elif array[index+1]==current:
        right_array[index]=right_array[index+1]
        return
    else:
        start=index+1
    for i in range(start,length):
        if array[i]>current:
            right_array[index]=i+1
            return
        else: continue

length=int(input())
left_array=[0]*length
right_array=[0]*length
array=list(input().split())
array=[int(elem) for elem in array]
find_max_index_product(array,length)
